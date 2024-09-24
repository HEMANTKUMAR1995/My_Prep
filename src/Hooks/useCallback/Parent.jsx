import React, { useCallback, useState } from "react";
import Child from "./Child";

const Parent = () => {
  const [parentData, setparentData] = useState([]);

  const parentUpdation = useCallback(() => {
    setparentData(parentData.push(1 * 2));
  }, []);

  return (
    <div>
      <h2>{`parent updated "${parentData}" times`}</h2>
      <Child update={parentUpdation} />
    </div>
  );
};

export default Parent;
