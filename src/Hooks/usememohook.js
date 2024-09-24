import React, { useMemo } from "react";

const ExpensiveCalculationComponent = ({ number }) => {
  // Function to perform an expensive calculation
  const expensiveCalculation = (num) => {
    console.log("Calculating...");
    let result = 0;
    for (let i = 0; i < 1000000000; i++) {
      result += num;
    }
    return result;
  };

  // Memoize the result of the expensive calculation
  const memoizedValue = useMemo(() => expensiveCalculation(number), [number]);

  return (
    <div>
      <h1>Expensive Calculation Result: {memoizedValue}</h1>
    </div>
  );
};

export default ExpensiveCalculationComponent;
