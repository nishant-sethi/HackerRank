import React, { Component } from 'react';
import './App.css';

import EmployeesList from './components/EmployeesList';

class App extends Component {
  render() {
    const { employees } = this.props;
    return (
      <div className="App">
        <EmployeesList employees={employees} />
      </div>
    );
  }
}

export default App;
