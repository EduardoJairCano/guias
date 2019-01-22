/* --------------------------------------- 04 - Booleanos  ----------------------------------------

   Los valores Booleanos son los datos que representan "True" o "False".
   Utilizados como banderas.

*/

//    Es posible declarar una valor numérico por medio de la palabra reservada "let" y "var"
let notificacionesActivas = true;
let recibirCorreos = false;
let activo = true;

//    Para saber el valor de una variable booleana es de la siguiente manera
let booleano = new Boolean(1);
console.log(booleano.toString());   // Casting variable a string

booleano = new Boolean(0);
console.log(booleano.toString());

booleano = new Boolean(true);
console.log(booleano.toString());

booleano = new Boolean("");
console.log(booleano.toString());

booleano = new Boolean(".");
console.log(booleano.toString());

/* Los valores falsos en javaScript, son los siguientes
   - undefined
   - NaN
   - null
   - 0
   - .0
   - ""
   - false
*/
