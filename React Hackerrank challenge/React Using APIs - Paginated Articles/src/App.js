import React, { Component } from 'react';
import './App.css';

import Articles from './components/Articles';

class App extends Component {
  render() {
    return (
      <div className="App">
        <Articles />
      </div>
    );
  }
}

export default App;
