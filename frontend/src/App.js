import './App.css';
import React, {useRef} from 'react';
import axios from 'axios';

function App() {

  const uploadedFile = useRef();

  const onImageUpload = (event) => {
        const file = event.target.files[0];
        const data = new FormData();
        data.append('file', file);
        axios.post('http://localhost:5000/isthisacat', data)
          .then(response => {
            alert(response.data.message);
            uploadedFile.current.value = '';
          })
          .catch(error => alert(error))
    };
  return (
    <div className="App">
      <header className="App-header">
        <p>
          Upload an image.
        </p>
        <button onClick={(e) => uploadedFile.current.click()}>Upload</button>
        <input type="file"
                   ref={uploadedFile}
                   onChange={onImageUpload}
                   hidden/>
      </header>
    </div>
  );
}

export default App;
