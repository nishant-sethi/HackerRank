import React from "react";

class Articles extends React.Component {
  state = {
    totalPages: 1,
    currentPage: 1,
    articles: [],
  };
  componentDidMount() {
    fetch(
      `https://jsonmock.hackerrank.com/api/articles?page=${this.state.currentPage}`
    )
      .then((res) => res.json())
      .then((data) =>
        this.setState({
          totalPages: data.total_pages,
          articles: data.data,
          currentPage: data.page,
        })
      );
  }
  getArticles(page) {
    if (page !== this.state.currentPage) {
      fetch(`https://jsonmock.hackerrank.com/api/articles?page=${page}`)
        .then((res) => res.json())
        .then((data) => {
          this.setState({
            totalPages: data.total_pages,
            articles: data.data,
            currentPage: page,
          });
        });
    }
  }
  render() {
    const { totalPages, articles } = this.state;
    return (
      <React.Fragment>
        <div className="pagination">
          {Array(totalPages)
            .fill()
            .map((_, i) => (
              <button
                data-testid="page-button"
                key={`page-button-${i + 1}`}
                onClick={() => this.getArticles(i + 1)}
              >
                {i + 1}
              </button>
            ))}
        </div>
        <ul className="results">
          {articles
            .filter(
              (article) => article.title !== null && article.title.length > 0
            )
            .map((article, i) => (
              <li key={`title-${i}`} data-testid="result-row">
                {article.title}
              </li>
            ))}
        </ul>
      </React.Fragment>
    );
  }
}

export default Articles;
