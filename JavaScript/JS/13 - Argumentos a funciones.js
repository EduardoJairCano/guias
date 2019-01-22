/* -------------------------------- 13 - Argumentos a funciones -----------------------------------

   Argumentos  -  Es la variable que se envia a una función, el valor actual previo a la función

   Parámetros  -  La variable que colocamos en la definición de la funcion, tiene que ser llenado
               -  Tip, puede recibir cualquier tipo de argumento.
               -  Se pueden enviar mas de un argumento

*/

/* es posible dar valores por default para los parametros, en caso de que envie un argumento, este
      se ignoraría */
function cuadrado(numero = 0){
   return numero*numero;
}
cuadrado(2);

/*    En caso de existir varios parametros para un función, y se opte por utilizar alguno con valor
         por default, es recomndable que dicho parametro sea colocado al final */
function hola(apellido, nombre = ""){
   console.log(nombre + apellido);
}
nombre("Cano");

/*    Se puede utilizar un parametro de tipo arreglo para declarar que son demasiados los Argumentos
         que se puedan utilizar */
function summa(){
   return arguments[0] + arguments[1];
}
console.log(suma(1,2,3,4));
