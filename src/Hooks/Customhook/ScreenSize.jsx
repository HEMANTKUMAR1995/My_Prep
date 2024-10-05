import React from "react";
import useScreenSizeCustom from "./useScreenSizeCustom";

const ScreenSize = () => {
  const { width, height } = useScreenSizeCustom();
  return (
    <div>
      <p>{`width : ${width}`}</p>
      <p>{`height: ${height}`}</p>
    </div>
  );
};

export default ScreenSize;
