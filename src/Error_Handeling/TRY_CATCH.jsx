import React, { useState } from "react";

const TRY_CATCH = () => {
  const [first, setfirst] = useState(0);

  const tryCatch = () => {
    try {
      const value = first - first === 0;
      return value;
    } catch (e) {
      console.log(e);
    } finally {
      return <h2>{first}</h2>;
    }
  };
  return (
    <div>
      <button onClick={tryCatch}>ilugl</button>
    </div>
  );
};

export default TRY_CATCH;
