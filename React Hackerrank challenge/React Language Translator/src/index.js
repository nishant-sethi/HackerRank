import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';

const TRANSLATIONS = new Map([
  ['ball', 'pelota'],
  ['house', 'casa'],
  ['dog', 'perro'],
  ['dogs', 'perros'],
  ['milk', 'leche'],
  ['orange', 'naranja'],
]);

ReactDOM.render(<App translations={TRANSLATIONS} />, document.getElementById('root'));
registerServiceWorker();
