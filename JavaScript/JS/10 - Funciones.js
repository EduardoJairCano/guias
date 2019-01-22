/* --------------------------------------- 10 - Funciones -----------------------------------------

   Una función es un bloque de codigo que ejecuta una serie de instrucciones cuando es mandada a
      llamar.

   function <nombre>() {
      <.....>
   }

*/

//    Funcion saludar()
function saludar(){
   console.log("Hola a todos")
}
//    Llamado de la función
saludar();

//    Funcion con parámetros con retorno de un valor
function cuadrado(numero) {
   return numero*numero;
   // Nada se ejecutara despues de un return
}
//    Asignación de una variable con valor de una función
let resultado = cuadrado(2);
console.log(resultado);
console.log(cuadrado(4));
