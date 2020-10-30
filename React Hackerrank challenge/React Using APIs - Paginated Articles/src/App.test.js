import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { render, fireEvent, cleanup, wait } from '@testing-library/react';

import fetchMock from 'fetch-mock';

import 'jest-dom/extend-expect';

const renderApp = () => render(<App />);

const testIds = {
  pageButton: "page-button",
  resultRow: "result-row",
};

beforeEach(() => {
});

afterEach(() => {
  // restore fetch() to its native implementation
  fetchMock.restore();
  cleanup();
});

test('Renders the correct number of page buttons', async () => {
  const url = `https://jsonmock.hackerrank.com/api/articles?page=1`;
  const response = {
    page:1,per_page:1,total:6,total_pages:6,data:[{title:"example title"}],
  }
  fetchMock.getOnce(url, JSON.stringify(response));
  const { getByTestId, queryByTestId, queryAllByTestId } = renderApp();

  await wait(() => {
    const pageButtons = queryAllByTestId(testIds.pageButton);
    expect(pageButtons).toHaveLength(response.total_pages);

    pageButtons.forEach((button, i) => {
      expect(button).toHaveTextContent((i+1).toString());
    });
  });
});

test('Renders articles correctly on app did mount', async () => {
  const url = 'https://jsonmock.hackerrank.com/api/articles?page=1';
  const response = {
    page:1,per_page:5,total:5,total_pages:1,data:[
      {title:"example title 1"},
      {title:null},
      {title:"example title 2"},
      {title:""},
      {title:"example title 3"},
    ],
  };
  fetchMock.getOnce(url, JSON.stringify(response));

  const { getByTestId, queryByTestId, queryAllByTestId } = renderApp();

  await wait(() => {
    const expectedTitles = response.data.map(entry => entry.title).filter(title => title !== null && title.length > 0);
    const results = queryAllByTestId(testIds.resultRow);
    expect(results).toHaveLength(expectedTitles.length);

    results.forEach((result, i) => {
      expect(result).toHaveTextContent(expectedTitles[i]);
    });
  });
});

test('Renders articles correctly after page button click', async () => {
  const urlFirstPage = 'https://jsonmock.hackerrank.com/api/articles?page=1';
  const responseFirstPage = {
    page:1,per_page:6,total:16,total_pages:3,data:[
      {title:"example title 1"},
      {title:null},
      {title:"example title 2"},
      {title:""},
      {title:"example title 3"},
      {title:""},
    ],
  };
  fetchMock.getOnce(urlFirstPage, JSON.stringify(responseFirstPage));

  const { getByTestId, queryByTestId, queryAllByTestId } = renderApp();
  let secondPageButton = null;
  await wait(() => {
    const pageButtons = queryAllByTestId(testIds.pageButton);
    secondPageButton = pageButtons[1];
    expect(secondPageButton).toHaveTextContent("2");
  });

  const urlSecondPage = 'https://jsonmock.hackerrank.com/api/articles?page=2';
  const responseSecondPage = {
    page:2,per_page:6,total:16,total_pages:3,data:[
      {title:"example title 2.1"},
      {title:""},
      {title:"example title 2.2"},
      {title:"example title 2.3"},
      {title:null},
      {title:"example title 2.4"},
    ],
  };
  fetchMock.getOnce(urlSecondPage, JSON.stringify(responseSecondPage));
  fireEvent.click(secondPageButton);

  await wait(() => {
    const expectedTitles = responseSecondPage.data.map(entry => entry.title).filter(title => title !== null && title.length > 0);
    const results = queryAllByTestId(testIds.resultRow);
    expect(results).toHaveLength(expectedTitles.length);

    results.forEach((result, i) => {
      expect(result).toHaveTextContent(expectedTitles[i]);
    });

  });
});
