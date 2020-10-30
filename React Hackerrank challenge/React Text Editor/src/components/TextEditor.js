import React from "react";

class TextEditor extends React.Component {
  state = {
    input: "",
    content: [],
  };
  appendValue = () => {
    const { content, input } = this.state;
    content.push(input);
    this.setState({ content, input: "" });
    console.log(this.state.content);
  };
  removeValue = () => {
    const { content } = this.state;
    content.pop();
    this.setState({ content, input: "" });
  };
  render() {
    return (
      <React.Fragment>
        <div className="controls">
          <input
            className="word-input"
            type="text"
            data-testid="word-input"
            onChange={(e) => this.setState({ input: e.target.value })}
            value={this.state.input}
          />
          <button
            data-testid="append-button"
            onClick={this.appendValue}
            disabled={this.state.input.length === 0}
          >
            Append
          </button>
          <button
            data-testid="undo-button"
            onClick={this.removeValue}
            disabled={this.state.content.length === 0}
          >
            Undo
          </button>
        </div>
        <div className="text-field" data-testid="text-field">
          {this.state.content.join(" ")}
        </div>
      </React.Fragment>
    );
  }
}

export default TextEditor;
