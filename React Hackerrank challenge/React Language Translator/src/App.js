import React, { Component } from 'react';
import './App.css';

import Translator from './components/Translator';

class App extends Component {
  render() {
    const { translations } = this.props;
    return (
      <div className="App">
        <Translator translations={translations} />
      </div>
    );
  }
}

export default App;
