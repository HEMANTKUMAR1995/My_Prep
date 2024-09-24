import { useEffect, useState } from "react";

export const useFetchApi = (uri) => {
  const [data, setdata] = useState({});

  useEffect(() => {
    try {
      const userData = uri;
      setdata(userData);
    } catch (error) {
      console.log(error);
    }
  }, []);
  console.log(uri);
  return data;
};
// export default useFetchApi;
