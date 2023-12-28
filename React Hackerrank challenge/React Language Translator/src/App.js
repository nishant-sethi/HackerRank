import React, { Component } from 'react';
import './App.css';

import Translator from './components/Translator';

function App({ translations }) {
  return (
    <div className='App'>
      <Translator translations={translations} />
    </div>
  );
}

export default App;
