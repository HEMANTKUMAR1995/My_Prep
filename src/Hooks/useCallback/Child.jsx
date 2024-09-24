import React from "react";

const rafce = ({ update }) => {
  console.log("Child Updated");

  return (
    <div>
      <button onClick={update}>Update</button>
    </div>
  );
};

export default React.memo(rafce);
