THis code is used for running continous client side outh authentication in background with predefined restriction. 

`[This is a prototype and not used in any production]`
We have a google extention with frontend made from react, and backend RESTful framework built from django. We are using sqlite3 as the db. 



# To create a extention
* To compile the google extention.
```
$ cd react_ui
# to install dependencies
$ npm install
# to create build folder that acts as unloaded extention
$ yarn run build 
```
* Go to chrome and add the following to url.
```
chrome://extensions/
```
* You need to enable developer mode in chrome.
* Click Load unpacked
* Then select build folder


# Run the server
```
$ pip install -r requirements.txt
$ python3 manage.py runserver
$ python3 app.py
```

