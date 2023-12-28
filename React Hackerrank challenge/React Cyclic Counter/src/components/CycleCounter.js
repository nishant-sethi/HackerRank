import { useState } from 'react';

function CycleCounter({ cycle }) {
  const [count, setCount] = useState(0);
  const incrementCounter = (cycle) => {
    if (count + 1 === (cycle || 4)) {
      setCount(0);
    } else {
      setCount(count + 1);
    }
  };
  return (
    <button
      data-testid='cycle-counter'
      style={{ fontSize: '1rem', width: 120, height: 30 }}
      onClick={() => incrementCounter(cycle)}
    >
      {count}
    </button>
  );
}

export default CycleCounter;
