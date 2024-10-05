import "./App.css";
// import TRY_CATCH from "./Error_Handeling/TRY_CATCH";
// import FormikForm from "./Form_Validation/FormikForm";
// import ReactForm_Yup from "./Form_Validation/ReactForm_Yup";
// import { useFetchApi } from "./CustomHooks/CustomHook";
// import ExpensiveCalculationComponent from "./Hooks/usememohook";
// import Parent from "./Hooks/useCallback/Parent";
import Counter from "./Redux/Counter";
// import PraticeGrid from "./Responsive/Grid/Grid-Layout/PraticeGrid";
import ScreenSize from "./Hooks/Customhook/ScreenSize";
// import Prominse from "./Promises/Prominse";

function App() {
  // const userData = { name: "hemant", age: 29, phone: 8117832556 };
  // const { name, age, phone } = useFetchApi(userData);
  // console.log(ExpensiveCalculationComponent(30));

  return (
    <div>
      {/* <ReactForm_Yup /> */}
      {/* <FormikForm /> */}
      {/* <p>{name}</p>
      <p>{age}</p>
      <p>{phone}</p> */}
      {/* <ExpensiveCalculationComponent number={23} /> */}
      {/* <Parent />
      {/* <Prominse /> */}
      <ScreenSize />
      {/* <PraticeGrid /> */}
      {/* <Counter /> */}
    </div>
  );
}

export default App;
