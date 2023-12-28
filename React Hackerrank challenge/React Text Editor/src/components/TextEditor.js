import React, { useState } from 'react';

function TextEditor() {
  const [input, setInput] = useState('');
  const [content, setContent] = useState([]);

  const appendValue = () => {
    setContent([...content, input]); // Create a new array with the old content plus the new input
    setInput(''); // Reset the input field
  };

  const removeValue = () => {
    setContent(content.slice(0, -1)); // Create a new array without the last element
    setInput(''); // Reset the input field
  };

  return (
    <>
      <div className='controls'>
        <input
          className='word-input'
          type='text'
          data-testid='word-input'
          onChange={(e) => setInput(e.target.value)}
          value={input}
        />
        <button
          data-testid='append-button'
          onClick={appendValue}
          disabled={input.length === 0}
        >
          Append
        </button>
        <button
          data-testid='undo-button'
          onClick={removeValue}
          disabled={content.length === 0}
        >
          Undo
        </button>
      </div>
      <div className='text-field' data-testid='text-field'>
        {content.join(' ')}
      </div>
    </>
  );
}

export default TextEditor;
