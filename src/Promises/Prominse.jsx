import React from "react";
import promises from "./promises";

const Prominse = () => {
  const args = { data: ["sunday", "monday"] };
  console.log(args);
  setTimeout(()=>{
     promises(args)
    .then((msg) => console.log(".then block executed"))
    .catch((err) => console.log(".Catch executed", err));
  },1000)
 
  return <div>Promise</div>;
};

export default Prominse;
