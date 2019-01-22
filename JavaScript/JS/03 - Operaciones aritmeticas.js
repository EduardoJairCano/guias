/* --------------------------------- 03 - Operaciones aritméticas ---------------------------------

   Los valores numéricos son declarados como cualquier otra variable, no es necesario asignar si es
      un tipo entero o flonte

   Operadores aritmeticos + - * / %
*/

//    Es posible declarar una valor numérico por medio de la palabra reservada "let" y "var"
let a = 5;
var b = 10;
var c = 2.5;
console.log(a + ", " + b + ", " + c);

//    Como las variables son identificadas por el interprete, es posible modificar su valor
let resultado = a + b;
console.log(" El resultado es de " + a + " mas " + b + " es: "+ resultado);
resultado = c - a;
console.log(" El resultado es de " + c + " menos " + a + " es: "+ resultado);
resultado = c * b;
console.log(" El resultado es de " + c + " por " + b + " es: "+ resultado);
resultado = a / b;
console.log(" El resultado es de " + b + " entre " + a + " es: "+ resultado);

//    Es posible implementar una librerias para Operaciones aritmeticas pre cargadas, se llama Math
let pi = Math.PI;
console.log(" El valor de PI es: " + pi);

//    Math.pow() - Una potencia con Math
let d = Math.pow(a,3);
console.log(" 5 al cubo es: " + d);

//    Math.round() - Para redondear un número
console.log(Math.round(6.5));
console.log(Math.round(7.2));
console.log(Math.round(7.89));

//    Math.sqrt() - Raiz cuadrada de un número
console.log(Math.sqrt(9));

//    Más Operaciones matemáticas en www.w3schools.com/js/js_math.asp
