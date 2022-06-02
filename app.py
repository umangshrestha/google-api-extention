import requests
from pprint import pprint
from urllib import response
from oauth2client.service_account import ServiceAccountCredentials
import httplib2
from datetime import datetime
import time
import json
from threading import Thread


URL_GET = "http://0.0.0.0:8000/api/data/"
URL_POST = "http://0.0.0.0:8000/api/upload/"
SCOPES = ["https://www.googleapis.com/auth/indexing"]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"


START=0
END=100

class Authentication:

    def _init_(self):
        self._request_responses = []
        self._json_key_file = ""
        self.final_response_list = []
        self.isHeader = True
        self.is_running = True

    def get_url(self):
        self.final_response_list = []
        received_jsons=0
        received_urls=0
        while(1):
            current_time= time.time()
            data = requests.get(
                URL_GET,
                headers={"Content-Type": "application/json"},
                data=json.dumps({"startJson": received_jsons, "startURL": received_urls})).json()
            if len(data["url"]) == 0 or len(data["json"]) ==0:
                time.sleep(2)
                continue 
            received_urls += len(data["url"])
            received_jsons += len(data["json"])
            print(f"Received urls: {received_urls}")
            response_data=self.process_url(data)
            self.post_csv(response_data)
            sleep_time=60-(time.time()-current_time)
            print(f"sleeping for {sleep_time}s")
            if sleep_time>0:
                time.sleep(sleep_time)

    def post_csv(self, response_data):
        print(response_data)
        try:
            requests.post(
                URL_POST,
                headers={"Content-Type": "application/json"},
                data=json.dumps({"data": response_data})).json()
        except Exception as E:
            print(E)


    def process_url(self, data):
        json_list = data["json"]
        url_list = data["url"]
        self.index = 0
        for json_dict in json_list:
            json_name = json_dict.pop("name")
            for url in url_list:
                if not url:
                    continue
                self.index += 1
                t = Thread(target= self.process, args=(url,json_dict,json_name))
                t.setDaemon(True)
                t.start()
        while(self.index>0):
            time.sleep(0.05)
        return self.final_response_list

    def process(self, url, json_dict, json_name):
        body_content = "{url: \"%s\", type: \"URL_UPDATED\"}" % url
        cred = ServiceAccountCredentials.from_json_keyfile_dict(keyfile_dict=json_dict, scopes=SCOPES)
        http = cred.authorize(httplib2.Http())
        try:
            response, _ = http.request(
                ENDPOINT, method="POST",body=body_content)
            status = response.status
            self.final_response_list.append({"url": url, "file_name":json_name, "date": datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), "status":response.status})
        except Exception as e:
            status = -1
        self.final_response_list.append({"url": url, "file_name":json_name, "date": datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),'status': status})
        self.index -=1


if __name__ == "__main__":
    a=Authentication()
    a.get_url()
