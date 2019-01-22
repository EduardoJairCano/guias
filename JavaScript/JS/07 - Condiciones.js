/* -------------------------------------- 07 - Condiciones ----------------------------------------

   Siguiendo la logica que establecen las condiones, se emplea
      - if() {}
      - else if() {}
      - esle {}

*/

/*    La declaracion de las condicones se ejectuan de la siguiente manerda, de las cuales solo se
       ejecutara solo una */
let edad = 25;

if (edad > 18) {
   console.log(" Eres mayor de edad");
}
else if(edad == 18) {
   console.log(" Justa la edad para ser mayor de edad");
}
else { // Caso por defecto
   console.log(" Eres menor de edad aun");
}
