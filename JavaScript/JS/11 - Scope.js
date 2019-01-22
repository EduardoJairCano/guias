/* ----------------------------------------- 11 - Scope -------------------------------------------

   Scope o alcance, es una coleccion de variables, funciones y objetos que se enceuntran al alcance
      en algun punto específico del código.

   Scope Global: variables declaradas fuera de las funciones

*/

//    Scope Global
let nombre = "Jair";
/*    Es posible acceder a las variables globales dentro de funciones, pero las variables que sean
       declaradas internamente en una función, solo existen dentro de la misma */
function saludar(){
   // Scope local
   let apellido = "Cano";
   console.log("Hola " + nombre + apellido);
}
saludar();
console.log(nombre);
/*    Al descomentar la siguiente linea, producira un error, dado que la variable es de origen Scope
         local, perteneciente unicamente a la funcion saludar() */
// console.log(apellido);
