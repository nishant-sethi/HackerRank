import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { render, fireEvent, cleanup } from '@testing-library/react';

import 'jest-dom/extend-expect';

const renderApp = (cycle) => render(<App cycle={cycle} />);

const testIds = {
  wordInput: "word-input",
  appendButton: "append-button",
  undoButton: "undo-button",
  textField: "text-field",
};

beforeEach(() => {
});

afterEach(() => {
  cleanup();
});

test('Initial UI renders correctly', () => {
  const { getByTestId } = renderApp();

  const textField = getByTestId(testIds.textField);
  expect(textField).toBeVisible();
  expect(textField).toHaveTextContent("");

  const wordInput = getByTestId(testIds.wordInput);
  expect(wordInput).toBeVisible();
  expect(wordInput).toHaveValue("");

  const appendButton = getByTestId(testIds.appendButton);
  expect(appendButton).toBeVisible();
  expect(appendButton).toBeDisabled();

  const undoButton = getByTestId(testIds.undoButton);
  expect(undoButton).toBeVisible();
  expect(undoButton).toBeDisabled();
});

test('Append button becomes enabled when the word input is non-empty', () => {
  const { getByTestId } = renderApp();

  const wordInput = getByTestId(testIds.wordInput);
  fireEvent.change(wordInput, { target: { value: 'foo' } });

  const appendButton = getByTestId(testIds.appendButton);
  expect(appendButton).toBeEnabled();
});

test('Append button becomes disabled when the word input is emptied', () => {
  const { getByTestId } = renderApp();

  const wordInput = getByTestId(testIds.wordInput);

  fireEvent.change(wordInput, { target: { value: 'foo' } });
  fireEvent.change(wordInput, { target: { value: '' } });

  const appendButton = getByTestId(testIds.appendButton);
  expect(appendButton).toBeDisabled();
});

test('Undo button becomes enabled when the text is not empty', () => {
  const { getByTestId } = renderApp();

  const wordInput = getByTestId(testIds.wordInput);
  fireEvent.change(wordInput, { target: { value: 'foo' } });

  const appendButton = getByTestId(testIds.appendButton);
  fireEvent.click(appendButton);

  const undoButton = getByTestId(testIds.undoButton);
  expect(undoButton).toBeEnabled();
});

test('Undo button becomes disabled when the text is emptied', () => {
  const { getByTestId } = renderApp();

  const wordInput = getByTestId(testIds.wordInput);
  fireEvent.change(wordInput, { target: { value: 'foo' } });

  const appendButton = getByTestId(testIds.appendButton);
  fireEvent.click(appendButton);

  const undoButton = getByTestId(testIds.undoButton);
  fireEvent.click(undoButton);
  expect(undoButton).toBeDisabled();
});

test('Word input is emptied when the word is appended', () => {
  const { getByTestId } = renderApp();

  const wordInput = getByTestId(testIds.wordInput);
  fireEvent.change(wordInput, { target: { value: 'foo' } })

  const appendButton = getByTestId(testIds.appendButton);
  fireEvent.click(appendButton);

  expect(wordInput).toHaveValue("");
});

test('Append appends words correctly to text', () => {
  const { getByTestId } = renderApp();

  const appendButton = getByTestId(testIds.appendButton);
  const wordInput = getByTestId(testIds.wordInput);

  const words = ["foo", "Bar", "bAz"];
  for (const word of words) {
    fireEvent.change(wordInput, { target: { value: word } });
    fireEvent.click(appendButton);
  }

  const textField = getByTestId(testIds.textField);

  const text = words.join(" ");
  expect(textField).toHaveTextContent(text);
});

test('Undo removes the last appended word correctly from text', () => {
  const { getByTestId } = renderApp();

  const appendButton = getByTestId(testIds.appendButton);
  const wordInput = getByTestId(testIds.wordInput);

  const words = ["foo", "Bar", "bAz"];
  const textField = getByTestId(testIds.textField);

  for (const word of words) {
    fireEvent.change(wordInput, { target: { value: word } });
    fireEvent.click(appendButton);
  }

  const undoButton = getByTestId(testIds.undoButton);
  for (let i = words.length-1; i >= 0; --i) {
    const text = words.slice(0, i).join(" ");
    expect(textField).toHaveTextContent(text);
    fireEvent.click(undoButton);
  }
  expect(textField).toHaveTextContent("");
});

test('Appending after undo appends correctly', () => {
  const { getByTestId } = renderApp();

  const appendButton = getByTestId(testIds.appendButton);
  const wordInput = getByTestId(testIds.wordInput);

  let words = ["foo", "Bar", "bAz"];
  const textField = getByTestId(testIds.textField);

  for (const word of words) {
    fireEvent.change(wordInput, { target: { value: word } });
    fireEvent.click(appendButton);
  }

  const undoButton = getByTestId(testIds.undoButton);
  fireEvent.click(undoButton);

  words.pop();
  const newWord = "AbaKan";
  words.push(newWord);
  fireEvent.change(wordInput, { target: { value: newWord } });
  fireEvent.click(appendButton);

  const text = words.join(" ");
  expect(textField).toHaveTextContent(text);
});
