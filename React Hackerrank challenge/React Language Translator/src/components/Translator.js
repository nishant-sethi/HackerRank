import { useState } from 'react';

function Translator({ translations }) {
  const [output, setOutput] = useState('');

  function translate(translations, value) {
    const result =
      typeof translations.get(value) === 'undefined'
        ? ''
        : translations.get(value);
    setOutput(result);
  }
  return (
    <>
      <div className='controls'>
        <div className='input-container'>
          <span>input:</span>
          <input
            type='text'
            className='text-input'
            data-testid='text-input'
            onChange={(e) => translate(translations, e.target.value)}
          />
        </div>
        <div className='input-container'>
          <span>output:</span>
          <input
            type='text'
            className='text-output'
            data-testid='text-output'
            value={output}
            readOnly
          />
        </div>
      </div>
    </>
  );
}

export default Translator;
