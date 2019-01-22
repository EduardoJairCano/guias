/* --------------------------------- 05 - Operadores comparativos ---------------------------------

   Utilizados para realizar comparativas entre variables
   > (Mayor menor
   >= (Mayor o igual)
   < (Menor mayor)
   <= (Menor o igual)
   == (Igual)
   || (Or o "o")
   && (And o "y")
   ! (Negado)

*/

//    Operaciones para obtener una respuesta verdadera o falsa
let edad = 25;

console.log("\nedad == 25");
console.log(edad == 25);
console.log("\nedad != 18");
console.log(edad != 18);
console.log("\nedad == 20");
console.log(edad == 20);
console.log("\nedad < 19");
console.log(edad < 19);
console.log("\nedad > 19");
console.log(edad > 19);
console.log("\nedad <= 30");
console.log(edad <= 30);
console.log("\nedad >= 30");
console.log(edad >= 30);

/*    Como las variables no son identificables en javaScript, la siguiente operacion dara como
       resultado verdadero */
console.log("\nedad == 25");
console.log(edad == "25");
/*    Entonces se debe utilizar un triple igual "===" para ver si tanto el valor como la variable
       Son iguales */
console.log("\nedad === 25");
console.log(edad === "25");
//    Es posible utilizar la misma lógica para la negacion "¡==" para itear tanto tipo como valor
