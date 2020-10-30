import React from "react";

class CycleCounter extends React.Component {
  state = {
    count: 0,
  };
  incrementCounter = (cycle) => {
    if (this.state.count + 1 === (this.props.cycle || 4)) {
      this.setState({ count: 0 });
    } else {
      this.setState({ count: this.state.count + 1 });
    }
  };
  render() {
    const { cycle } = this.props;

    return (
      <button
        data-testid="cycle-counter"
        style={{ fontSize: "1rem", width: 120, height: 30 }}
        onClick={() => this.incrementCounter(cycle)}
      >
        {this.state.count}
      </button>
    );
  }
}

export default CycleCounter;
