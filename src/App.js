import { useEffect } from 'react';
import './App.css';
import Button from './components/button';

function App() {
  useEffect(()=> {
    document.title ="Google Console Extention"
  })
  return (
    <div className="App">
      <header className="App-header">
        <label htmlFor="num"> number of API connections </label>
        <input type="text" id="num" name="name" required minLength={0} maxLength={4} size={10} defaultValue={10} />
        <Button name="Save Settings" />

        <h2>Actions and Details</h2>
        <Button name="Download CSV" label="Download/Export Saved Data"/>
        <Button name="Delete saved items" id="delete" label="Clean saved keywords data" />
                      
      </header>
    </div>
  );
}

export default App;
