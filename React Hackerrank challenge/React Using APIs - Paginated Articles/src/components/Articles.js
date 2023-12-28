import React, { useEffect, useState } from 'react';

function Articles() {
  const [totalPages, setTotalPages] = useState(1);
  const [currentPage, setCurrentPages] = useState(1);
  const [articles, setArticles] = useState([]);

  useEffect(() => {
    const fn = () => {
      fetch(`https://jsonmock.hackerrank.com/api/articles?page=${currentPage}`)
        .then((res) => res.json())
        .then((data) => {
          setTotalPages(data.total_pages);
          setArticles(data.data);
          setCurrentPages(data.page);
        });
    };
    fn();
  }, []);
  function getArticles(page) {
    if (page !== currentPage) {
      fetch(`https://jsonmock.hackerrank.com/api/articles?page=${page}`)
        .then((res) => res.json())
        .then((data) => {
          setTotalPages(data.total_pages);
          setArticles(data.data);
          setCurrentPages(data.page);
        });
    }
  }
  return (
    <>
      <div className='pagination'>
        {Array(totalPages)
          .fill()
          .map((_, i) => (
            <button
              data-testid='page-button'
              key={`page-button-${i + 1}`}
              onClick={() => getArticles(i + 1)}
            >
              {i + 1}
            </button>
          ))}
      </div>
      <ul className='results'>
        {articles
          .filter(
            (article) => article.title !== null && article.title.length > 0
          )
          .map((article, i) => (
            <li key={`title-${i}`} data-testid='result-row'>
              {article.title}
            </li>
          ))}
      </ul>
    </>
  );
}

export default Articles;
