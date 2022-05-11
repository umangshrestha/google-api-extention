from urllib import response
from oauth2client.service_account import ServiceAccountCredentials
import httplib2
from flask import Flask, current_app, g, request, Response
from datetime import datetime
import requests
import json
import time
import pandas as pd
from csv import writer
from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify, make_response


SCOPES = ["https://www.googleapis.com/auth/indexing"]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
STATES = ('successfully indexed, wait a while for google to refresh',
          'failed to be indexed')
URLS = []
LOAD = 0
CURRENT_INDEX = 0
CREDENTIAL_LIST = []

app= Flask(__name__)
CORS(app, resources={ r"*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/')
def hello():
    """ Displays the index page accessible at '/'
    """
    print("-----------------")
    response =  jsonify({"Message": "Hello"})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/api', methods=["POST", "GET"], strict_slashes=False)
def index():
    ob = Credential()
    url = request.json["url"]
    json_key = request.json["json_data"]
    write_json(json_key)
    ob.process_url("temp.json",url)
    response = jsonify(ob.process_url("temp.json",url))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


def write_json(json_data):
    with open("temp.json", "w") as f:
        f.write(json.dumps(json_data))
        
class Credential:
    def _init_(self):
        self._request_responses = []
        self.isHeader = True

    def process_url(self, json_path, url_list):
        final_response_list = []
        for url in url_list:
            if not url:
                continue
            self._json_key_file = json_path
            body_content = "{url: \"%s\", type: \"URL_UPDATED\"}" % url
            cred = ServiceAccountCredentials.from_json_keyfile_name(
                self._json_key_file, scopes=SCOPES)
            http = cred.authorize(httplib2.Http())
            try:
                response, content = http.request(
                    ENDPOINT, method="POST",body=body_content)
                final_response_list.append({"url": url, "time": datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), "status":response.status})
            except Exception as e:
                print(e)
                final_response_list.append({"url": url, "time": datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),'status': -1})
        print(final_response_list)
        return final_response_list


if __name__ == '__main__':
    app.debug=True
    app.run(port=5000)
