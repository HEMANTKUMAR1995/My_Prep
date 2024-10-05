import { configureStore } from "@reduxjs/toolkit";
import countReducer from "./Redux/Slices/counterSlice";

export const store = configureStore({
  reducer: {
    counter: countReducer,
  },
});
console.log(store);

