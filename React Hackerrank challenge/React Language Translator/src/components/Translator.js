import React from "react";

class Translator extends React.Component {
  state = {
    output: "",
  };
  translate(translations, value) {
    this.setState({
      output:
        typeof translations.get(value) === "undefined"
          ? ""
          : translations.get(value),
    });
  }
  render() {
    const { translations } = this.props;
    return (
      <React.Fragment>
        <div className="controls">
          <div className="input-container">
            <span>input:</span>
            <input
              type="text"
              className="text-input"
              data-testid="text-input"
              onChange={(e) => this.translate(translations, e.target.value)}
            />
          </div>
          <div className="input-container">
            <span>output:</span>
            <input
              type="text"
              className="text-output"
              data-testid="text-output"
              value={this.state.output}
              readOnly
            />
          </div>
        </div>
      </React.Fragment>
    );
  }
}

export default Translator;
