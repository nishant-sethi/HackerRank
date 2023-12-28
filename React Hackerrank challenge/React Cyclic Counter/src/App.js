import React, { Component } from 'react';
import './App.css';

import CycleCounter from './components/CycleCounter';

function App({ cycle }) {
  return (
    <div className='App'>
      <CycleCounter cycle={cycle} />
    </div>
  );
}

export default App;
