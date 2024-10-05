console.log(a);
var a = 10;
// undefedined

// console.log(b);
// let b = 20;
// refference type error: can't acces variable before accessing

function test() {
  console.log(x);
  var x = 5;
  console.log(x);
}
test();
// undefined
// 5

function hoistExample() {
  console.log(foo);
  var foo = "bar";
  console.log(foo);
}
hoistExample();
// undefined
// bar

console.log(foo);
var foo = function () {
  console.log("Hello!");
};
foo();
// undefined
// Hello!

console.log(foo);
function foo() {
  console.log("Hello!");
}
foo();

// function foo() {
//   console.log('Hello!');
// }
// Hello!

var a = 1;
function b() {
  a = 10;
  return;
  function a() {}
}
b();
console.log(a);
//
