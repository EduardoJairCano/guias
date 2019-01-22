/* --------------------------------- 09 - Undefined, null y nan -----------------------------------

   Undefined - Indica que una variable no se le ha asignado valor o no se ha declarado
      Valor booleano = false
      Tipo = Undefined

   null - Indica la ausencia de valor
      valor booleano = false
      Tipo = Object

   NaN - No es un numero

*/

//
dadada;
typeof dadada;
typeof 2;

//    Se crea una variable, pero no se le asigna un valor entonces es Undefined
let numero;
typeof numero; // Undefined
console.log(numero);

//    Se asigna un valor null para la variable y cambiara el tipo de la variable
numero = null;
typeof numero; // "object"

//    NaN - una posible operacion que no puede ser realizada
"adada" * 3;   // NaN
