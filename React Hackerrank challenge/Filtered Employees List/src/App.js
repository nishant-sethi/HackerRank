import React, { Component } from 'react';
import './App.css';

import EmployeesList from './components/EmployeesList';

function App({ employees }) {
  return (
    <div className='App'>
      <EmployeesList employees={employees} />
    </div>
  );
}
export default App;
