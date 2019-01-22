/* ------------------------------------ 12 - let, const y var --------------------------------------

   let   - Menor alcancce, se limita a solo el bloque más próximo en que se declara
            scope local
   const - Menor alcancce, se limita a solo el bloque más próximo en que se declara

   var   - Alcance medio, solo es utilizable dentro de la function() en que se delcara
            scope global o scope local de una función
*/

function mayor_de_edad(edad){
   if(edad >= 18){
      var resultado = "Eres mayor de edad";
      //let resultado = "Eres mayor de edad"; // Marca error, resultado is not defined
   }
   else{
      var resultado = "Eres menor de edad";
      //let resultado = "Eres menor de edad";
   }
   console.log(resultado);
}

mayor_de_edad(26);
