import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { render, fireEvent, cleanup } from '@testing-library/react';

import 'jest-dom/extend-expect';

const renderApp = (translations) => render(<App translations={translations} />);

const testIds = {
  textInput: "text-input",
  textOutput: "text-output",
};

const translations = new Map([
  ['cat', 'gato'],
  ['cats', 'gatos'],
  ['man', 'hombre'],
  ['men', 'hombres'],
  ['vine', 'vino'],
  ['strawberry', 'fresa'],
  ['strawberries', 'fresas'],
]);

const nonExistingTranslations = ['ca, ma', 'x', 'vines', 'mans', 'trawberry'];

beforeEach(() => {
});

afterEach(() => {
  cleanup();
});

test('Initial UI renders correctly', () => {
  const { getByTestId } = renderApp(translations);

  const textInput = getByTestId(testIds.textInput);
  expect(textInput).toBeVisible();
  expect(textInput).toHaveValue("");

  const textOutput = getByTestId(testIds.textOutput);
  expect(textOutput).toBeVisible();
  expect(textOutput).toHaveValue("");
  expect(textOutput).toHaveAttribute('readOnly');
});


test('Test with existing translations', () => {
  const { getByTestId } = renderApp(translations);

  const textInput = getByTestId(testIds.textInput);
  const textOutput = getByTestId(testIds.textOutput);

  translations.forEach((value, key) => {
    fireEvent.change(textInput, { target: { value: key }});
    expect(textOutput).toHaveValue(value);
  });
});

test('Test with non-existing translations', () => {
  const { getByTestId } = renderApp(translations);

  const textInput = getByTestId(testIds.textInput);
  const textOutput = getByTestId(testIds.textOutput);

  for (let key of nonExistingTranslations) {
    fireEvent.change(textInput, { target: { value: key }});
    expect(textOutput).toHaveValue("");
  }
});

test('Test with existing translation followed by non-existing translations', () => {
  const { getByTestId } = renderApp(translations);

  const textInput = getByTestId(testIds.textInput);
  const textOutput = getByTestId(testIds.textOutput);

  const existing = 'cat';
  const nonExisting = 'vines';

  fireEvent.change(textInput, { target: { value: existing }});
  expect(textOutput).toHaveValue(translations.get(existing));

  fireEvent.change(textInput, { target: { value: nonExisting }});
  expect(textOutput).toHaveValue("");
});

test('Test with non-existing translation followed by existing translations', () => {
  const { getByTestId } = renderApp(translations);

  const textInput = getByTestId(testIds.textInput);
  const textOutput = getByTestId(testIds.textOutput);

  const existing = 'cat';
  const nonExisting = 'vines';

  fireEvent.change(textInput, { target: { value: nonExisting }});
  expect(textOutput).toHaveValue("");

  fireEvent.change(textInput, { target: { value: existing }});
  expect(textOutput).toHaveValue(translations.get(existing));

});
