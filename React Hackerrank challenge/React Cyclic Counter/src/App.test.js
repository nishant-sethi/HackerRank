import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { render, fireEvent, cleanup } from '@testing-library/react';

import 'jest-dom/extend-expect';

const renderApp = (cycle) => render(<App cycle={cycle} />);

const testIds = {
  cycleCounter: "cycle-counter",
};

const testWithCycleLength = (cycle) => {
  const { getByTestId } = renderApp(cycle);

  const counter = getByTestId(testIds.cycleCounter);
  expect(counter).toBeVisible();

  let count = 0;

  for (let i = 0; i < 10*cycle+10; ++i) {
    const counter = getByTestId(testIds.cycleCounter);
    let value = counter.textContent || counter.innerText;
    value = parseInt(value);
    expect(value).toBe(count);
    fireEvent.click(counter);
    count = (count+1) % cycle;
  }
};

afterEach(() => {
  cleanup();
});

test('Testing for cycle length 1', () => {
  testWithCycleLength(1);
});

test('Testing for cycle length 2', () => {
  testWithCycleLength(2);
});

test('Testing for cycle length 3', () => {
  testWithCycleLength(3);
});

test('Testing for cycle length 7', () => {
  testWithCycleLength(7);
});

test('Testing for cycle length 31', () => {
  testWithCycleLength(31);
});
