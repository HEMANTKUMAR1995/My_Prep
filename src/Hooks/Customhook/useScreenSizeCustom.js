const { useEffect } = require("react");
const { useState } = require("react");

const useScreenSizeCustom = () => {
  const [size, setSize] = useState({
    width: "",
    height: "",
  });

  useEffect(() => {
    function screenUpdate() {
      setSize({ width: window.innerWidth, height: window.innerHeight });
    }
    screenUpdate();
    window.addEventListener("resize", screenUpdate);

    return () => {
      window.removeEventListener("rezise", screenUpdate);
    };
  }, []);
  return size;
};

export default useScreenSizeCustom;
