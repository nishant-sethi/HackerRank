import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { render, fireEvent, cleanup } from '@testing-library/react';

import 'jest-dom/extend-expect';

const renderApp = (employees) => render(<App employees={employees} />);

const testIds = {
  filterInput: "filter-input",
  employeesList: "employees-list",
};

const employees = [
  {
    name: "Alex Jones",
  },
  {
    name: "Avery Green",
  },
  {
    name: "Parker Hawking",
  },
  {
    name: "Jordan Richards",
  },
  {
    name: "Charlie Green",
  },
  {
    name: "Riley Miller",
  },
];

beforeEach(() => {
});

afterEach(() => {
  cleanup();
});

test('Initial UI renders correctly', () => {
  const { getByTestId, getAllByTestId } = renderApp(employees);

  const filterInput = getByTestId(testIds.filterInput);
  expect(filterInput).toBeVisible();
  expect(filterInput).toHaveValue("");

  const renderedEmployees = getAllByTestId('employee');

  expect(renderedEmployees.length).toBe(employees.length);
  renderedEmployees.forEach((employee, i) => {
    expect(employee.textContent).toBe(employees[i].name);
  });
});

test('Filtering for not matching phrase shows no emplyees', () => {
  const { getByTestId, queryAllByTestId } = renderApp(employees);

  const filterInput = getByTestId(testIds.filterInput);

  fireEvent.change(filterInput, { target: { value: 'z' } });
  const renderedEmployees = queryAllByTestId('employee');
  expect(renderedEmployees.length).toBe(0);
});

test('Filtering for not matching phrase that contains at least one name as a proper substring shows no employees', () => {
  const { getByTestId, queryAllByTestId } = renderApp(employees);

  const filterInput = getByTestId(testIds.filterInput);

  fireEvent.change(filterInput, { target: { value: 'Greens' } });
  const renderedEmployees = queryAllByTestId('employee');
  expect(renderedEmployees.length).toBe(0);

});

test('Filtering for one character query renders correct matches', () => {
  const { getByTestId, queryAllByTestId } = renderApp(employees);

  const filterInput = getByTestId(testIds.filterInput);

  fireEvent.change(filterInput, { target: { value: 'e' } });

  const expectedNames = [
    "Alex Jones",
    "Avery Green",
    "Parker Hawking",
    "Charlie Green",
    "Riley Miller",
  ];
  const renderedEmployees = queryAllByTestId('employee');
  expect(renderedEmployees.length).toBe(expectedNames.length);
  renderedEmployees.forEach((employee, i) => {
    expect(employee.textContent).toBe(expectedNames[i]);
  });
});


test('Filtering for expected matches with lower and uppercase matched substrings', () => {
  const { getByTestId, queryAllByTestId } = renderApp(employees);

  const filterInput = getByTestId(testIds.filterInput);

  fireEvent.change(filterInput, { target: { value: 'ch' } });

  const expectedNames = [
    "Jordan Richards",
    "Charlie Green",
  ];
  const renderedEmployees = queryAllByTestId('employee');
  expect(renderedEmployees.length).toBe(expectedNames.length);
  renderedEmployees.forEach((employee, i) => {
    expect(employee.textContent).toBe(expectedNames[i]);
  });
});

test('Filtering with query containing uppercase letters renders correct matches', () => {
  const { getByTestId, queryAllByTestId } = renderApp(employees);

  const filterInput = getByTestId(testIds.filterInput);

  fireEvent.change(filterInput, { target: { value: 'gReEN' } });

  const expectedNames = [
    "Avery Green",
    "Charlie Green",
  ];
  const renderedEmployees = queryAllByTestId('employee');
  expect(renderedEmployees.length).toBe(expectedNames.length);
  renderedEmployees.forEach((employee, i) => {
    expect(employee.textContent).toBe(expectedNames[i]);
  });
});
