export const promises = (args) => {
  const firstPromise = async (resolve, reject) => {
    const response = await args;
    console.log(response);
    const data = response.data;

    if (data) {
      resolve(data);
    } else {
      reject(data);
    }
  };

  return firstPromise;
};

// export default promises();
