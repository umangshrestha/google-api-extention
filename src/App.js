import { useEffect, useState } from 'react';
import './App.css';
import Button from './components/button';
import Table from './components/table';

function App() {
  
  const [message, setMessage] = useState("");
  const [url, setURL] = useState([]);

  useEffect(()=> {
    document.title ="Google Console Extention"
  })

  const handleInput = (event) => {
    const urlList = [...url];
    const files = event.target.files;
    setMessage(`${files.length} file uploaded`)
    for (let file of event.target.files) {
      let reader = new FileReader();
      reader.readAsText(file);
      
      reader.onload = (ev) => {
        ev.target.result
          .split(/\r\n|\n/)
          .forEach(line => urlList.push(line));
      }

      reader.onerror = (event) => {
        alert(event.target.error.name);
      };
    }
    setURL(urlList);
    setMessage(`${url.length} url found`);
  
  }

  return (
    
    <div className="App">
       <div className="BoxFiles">
        <label htmlFor="upload">Url File: </label>
        <input type="file" id="upload" name="upload" multiple="multiple" onChange={handleInput} /> 
        <label for="upload">Json Directory</label>
        <input type="file" id="uploadJson" directory="" webkitdirectory="" />
        <div className="Message"> {message} </div>
      </div>
      <div className="BoxButtons">
        <button id="stop"  >Stop Process</button>
        <button id="start" >Start</button>
      </div>
      <div className="BoxTable"> 
        <Table />
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
