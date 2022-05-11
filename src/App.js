import { useEffect, useState } from 'react';
import './App.css';
import Button from './components/button';
import Table from './components/table';


const MAX_COUNT = 400;
function App() {
  
  const [message, setMessage] = useState("");
  const [url, setURL] = useState([]);
  const [jsonData, setJSON] = useState({});
  const [btn, setBtn] = useState("start");

  useEffect(()=> { 
    document.title ="Google Console Extention"
  })

  const handleUpload = (event) => {
    const files = event.target.files;
    let  urlList = [...url];
    setMessage(`${files.length} file uploaded`)
    for (let file of event.target.files) {
      let reader = new FileReader();
      reader.readAsText(file);
      
      reader.onload = (ev) => {
        ev.target.result
          .split(/\r\n|\n/)
          .forEach(line =>urlList.push(line));

      if (urlList.length >= MAX_COUNT) {
        setMessage(`Attempting ${urlList.length} urls, Daily threshold ${MAX_COUNT}`)
        return
      } else {
        console.log(urlList)
        setURL(urlList);
        console.log(url.length, urlList.length)
        setMessage(`${urlList.length} url found`);
      }
      }

      reader.onerror = (event) => {
        alert(event.target.error.name);
      };
    }
   
  }

   

  const handleJSONUpload = (event) => {
    const file = event.target.files[0];
    let reader = new FileReader();
    reader.readAsText(file);
    reader.onload = (ev) => { 
      console.log(typeof ev.target.result); 
      try{
        let json = JSON.parse(ev.target.result);
        setJSON(json)
      } catch(e){
        setMessage(`${e}`)
      }
    }
    reader.onerror = (ev) =>setMessage(`error loading ${event.target.files[0].name}: ${ev}`)
    
  }

  // fetch("http://127.0.0.1:5000/", {
  //   methods: "GET",
  //   headers: {
  //     'Accept': 'application/json',
  //     'Content-Type': 'application/json',
  //     'Access-Control-Allow-Origin': '*'
  //   },
  // }).then(e => e.json())
  // .then(e=> console.log("data",e))
  // .catch(e=> console.log("err",e))
      
 

  const handleStart = () => {
    console.log("start");
    if (url.length === 0 || Object.keys(jsonData).length === 0) { 
      setMessage("Error: url or jsonFile not uploaded!"); 
      return;
    }
    setMessage("Waiting...");
    setBtn("Stop");
    const data = {
      "url":url, 
      "json_data": jsonData
    }

   
   
 fetch('http://127.0.0.1:5000/api', {
      method: 'POST',
      body: JSON.stringify(data),
      mode: "cors",
      dataType: 'json',

      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
      })
    .then(e => e.json())
    .then(e=> e)
    .catch(err => console.log("err",err))

  setBtn("Start");
    
  }

  return (
    
    <div className="App">
       <div className="BoxFiles">
        <label htmlFor="upload">Url File: </label>
        <input type="file" id="upload" name="upload" multiple="multiple" onChange={handleUpload} /> 
        <label htmlFor="upload">Json Directory</label>
        <input type="file" id="uploadJson" onChange={handleJSONUpload} />
      </div>
      <div className='BoxMessage'> {message} </div>
      <div className="BoxTable"> 
        <Table />
      </div>
      <div className="BoxButtons">
        <Button id="start"  name={btn}  onClick={handleStart}/>
      </div>
      <div className="right">
        <label htmlFor="num"> number of API connections </label>
        <input type="text" id="num" name="name" required minLength={0} maxLength={4} size={10} defaultValue={10} />
        <Button name="Save Settings" />

        <h2>Actions and Details</h2>
        <Button name="Download CSV" label="Download/Export Saved Data"/>
        <Button name="Delete saved items" id="delete" label="Clean saved keywords data" />
                      
      </div>
    </div>
  );
}

export default App;
