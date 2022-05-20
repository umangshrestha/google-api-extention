// import './App.css';
// import Uploader from './components/uploader';
// import CountTable from './components/countTable';
// import URLTable from './components/urlTable';
// import "./components/removeButton";

// import {useState, useEffect} from 'react';

// const URL_UPLOAD_FILE = 'http://127.0.0.1:8000/api/url/';
// const URL_JSON_FILE = 'http://127.0.0.1:8000/api/auth/';
// const URL_GET_DATA = 'http://127.0.0.1:8000/api/data/';


// const DEFAULT_URL = 'http://127.0.0.1:8000/';

// const Headers = {
//   'Accept': 'application/json',
//   'Content-Type': 'application/json',
//   'Access-Control-Allow-Origin': '*'
// };


import './App.css';
import Uploader from './components/uploader';
import CountTable from './components/countTable';
import URLTable from './components/urlTable';
import MissingKey from './settings/header';
import {useState, useEffect} from 'react';
import {URL_DEFAULT, URL_GET_DATA, URL_JSON_FILE, URL_UPLOAD_FILE} from './settings/urls';

const Headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Access-Control-Allow-Origin': '*'
};

function App() {
  const [message, setMessage] = useState("Upload Files");
  const [errMessage, setErrMessage] = useState("");
  const [count, setCount] = useState({"json":0, "url":0, "processed":0, "success": 0});
  const [data, setData] = useState(undefined)

  const AddErrorMessage = (emsg, {name}) =>  setErrMessage(`${emsg}:"${name}"`)

  useEffect(()=>{
    getCount();
    document.title = "google-extention"
  }, [])
 
  const getCount = () => 
    fetch(URL_GET_DATA, {
      method: 'POST',
      mode: "cors",
      headers: Headers})
    .then(resp => resp.json())
    .then(data => setCount(data))
    .catch(data=> setErrMessage(`${data}`))

  const handleURLUpload = (event) =>  {
    setErrMessage("")
    setMessage("")
    for (const file of  event.target.files) {
      let reader = new FileReader();
      reader.readAsText(file);

      reader.onerror = (ev) => AddErrorMessage("FileUploadError",file)

      reader.onload = async (ev) =>  {
        const urls = ev.target.result
                .split(/\r\n|\n/)
                .filter(x => x.indexOf("http") !== -1);
        
        if (urls.length === 0)  
            return AddErrorMessage("FileIsEmptyError",file);
        setMessage(`Uploading ${file.name}...`)
        console.log(urls)
        fetch(URL_UPLOAD_FILE, {
              method: 'POST',
              body: JSON.stringify({urls: urls}),
              mode: "cors",
              dataType: 'json',
              headers: Headers})
        .then(resp => resp.json())
        .then(data => {getCount(); setMessage(`FileUpload:${data.status}`)})
        .catch(data=> {
          setMessage("")
          setErrMessage(`${data}`)
        })
      }
    }
  }

  const handleJSONUpload = (event) =>  {
    setErrMessage("")
    setMessage("")
    for (const file of event.target.files) {
      let reader = new FileReader();
      reader.readAsText(file);

      reader.onerror = (ev) => AddErrorMessage("FileUploadError",file)

      reader.onload = async (ev) =>  {
        try{
          let json = JSON.parse(ev.target.result);
          const key = MissingKey(json)
          if (key !== undefined) {
              return  AddErrorMessage(`KeyError:${key}`, file);
          } 
          setMessage(`Uploading ${file.name}...`)
          fetch(URL_JSON_FILE, {
            method: 'POST',
            body: JSON.stringify(json),
            mode: "cors",
            dataType: 'json',
            headers: Headers})
          .then(resp => resp.json())
          .then(data => {
            setMessage(`FileUpload:${data.status}`)
          })
          .catch(data=> {
            setMessage("")
            setErrMessage(`${data}`)
          })
        } catch(e){
          AddErrorMessage(e, file);
        }          
      }
    }
  }

  const handleOnClick = (path) => 
    fetch(URL_DEFAULT + path, {
      method: 'GET',
      mode: "cors",
      headers: Headers})
    .then(resp =>resp.json())
    .then(data => setData(data))

    const ClearData = (type) => {
      if (!window.confirm(`warning! clearning all data for:"${type}"`)) return 
      let url = "";       
      switch (type) {
          case "url":
            url = URL_UPLOAD_FILE
            break;
          case "auth":
            url = URL_JSON_FILE;
            break;
          case "status":
            url = URL_GET_DATA
            break;
          case "success":
            url = URL_UPLOAD_FILE;
            break;
          default:
            break;
      }

      fetch(url, {
        method: 'DELETE',
        mode: "cors",
        headers: Headers})
      .then(resp => resp.json())
      .then(_  =>   {getCount(); setMessage(`data removed:"${type}"`)})
      .catch(data=> setErrMessage(`${data}`))
                          
    }


  return (
    <div className="App">
      {/* message */}
      <div className='Message'> {message} </div>
      <div className='ErrMessage'> {errMessage} </div>

      <div className="BoxButton">
        <Uploader func={handleURLUpload} text="Upload URL Files" name="url-upload" />
        <Uploader func={handleJSONUpload} text="Upload JSON Files" name="json-upload" />
      </div>
      <CountTable data={count} onClick={(path) => handleOnClick(path)} remove={ClearData}/>
      <URLTable data={data} />
    </div>
    
  );
}

export default App;
