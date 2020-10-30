import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';

const EMPLOYEES = [
  {
    name: "Parker Green",
  },
  {
    name: "Jordan Richards",
  },
  {
    name: "Alex Stevens",
  },
  {
    name: "Avery Scott",
  },
  {
    name: "Riley Miller",
  },
  {
    name: "Charlie Green",
  },
];

ReactDOM.render(<App employees={EMPLOYEES}/>, document.getElementById('root'));
registerServiceWorker();
