from concurrent.futures import thread
from urllib import response
from oauth2client.service_account import ServiceAccountCredentials
import httplib2
from flask import Flask, request, Response, send_file
from datetime import datetime
import requests
import json
import time
import pandas as pd
from threading import Thread
import os
import csv
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
    data = ob.process_url("temp.json",url)
    response = jsonify(data)
    write_csv(data,"url.csv")
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_csv')
def get_csv():
    csv_file = "url.csv" 
    if not os.path.isfile(csv_file):
        return "ERROR: file %s was not found on the server" % csv_file
    return send_file(csv_file, as_attachment=True, attachment_filename=csv_file)


def write_json(json_data):
    with open("temp.json", "w") as f:
        f.write(json.dumps(json_data))

def write_csv(data,csv_path):
    keys = data[0].keys()
    with open(csv_path, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)
        
class Credential:
    def _init_(self):
        self._request_responses = []
        self._json_key_file = ""
        self.final_response_list = []
        self.isHeader = True

    def process_url(self, json_path, url_list):
        self.final_response_list = []
        self._json_key_file = json_path
        self.index = 0
        for url in url_list:
            if not url:
                continue
            self.index += 1
            t = Thread(target= self.process, args=(url,))
            t.setDaemon(True)
            t.start()
        print(self.final_response_list)
        while(self.index>0):
            time.sleep(0.05)
        return self.final_response_list

    def process(self, url):
        body_content = "{url: \"%s\", type: \"URL_UPDATED\"}" % url
        cred = ServiceAccountCredentials.from_json_keyfile_name(
            self._json_key_file, scopes=SCOPES)
        http = cred.authorize(httplib2.Http())
        try:
            response, content = http.request(
                ENDPOINT, method="POST",body=body_content)
            print({"url": url, "time": datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), "status":response.status})
            self.final_response_list.append({"url": url, "time": datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), "status":response.status})
        except Exception as e:
            print(e)
            self.final_response_list.append({"url": url, "time": datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),'status': -1})
        self.index -=1



if __name__ == '__main__':
    app.debug=True
    app.run(port=5000)
