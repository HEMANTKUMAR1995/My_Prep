// import React from "react";
// const PraticeGrid = () => {
  //   return (
    //     <div className="grid-container">
    
    //       <div className="grid-item">1</div>
    //       <div className="grid-item">2</div>
    //       <div className="grid-item">3</div>
    //       <div className="grid-item">4</div>
    //       <div className="grid-item">5</div>
    //       <div className="grid-item">6</div>
    //       <div className="grid-item">7</div>
    //       <div className="grid-item">8</div>
    //       <div className="grid-item">9</div>
    //     </div>
    //     /* <div class="grid-container">
    //   <div class="item1">Header</div>
    //   <div class="item2">Menu</div>
    //   <div class="item3">Main</div>
    //   <div class="item4">Right</div>
    //   <div class="item5">Footer</div>
    // </div> */
    //   );
    // };
    
    // export default PraticeGrid;
    import React from "react";
    import "./PraticeGrid.css";

const PraticeGrid = () => {
  let a = [1, 2, 3, 4, 5, 6];
  return (
    <div className="parent">
      {/* <p>Pratice Grid</p> */}
      {a.map((val, id) => {
        return (
          <div className="child" key={id}>
            child{val}
          </div>
          );
      })}
    </div>
  );
};

export default PraticeGrid;
