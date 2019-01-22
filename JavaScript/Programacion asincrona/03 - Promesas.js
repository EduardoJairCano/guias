/* -------------------------------------- 03 - Promesas -------------------------------------------

   Es un objeto que representa la terminación o el fracaso eventual de una operación asíncrona. Una
      promesa puede ser creada usando su constructor.

   Esencialmente, una promesa es un objeto devuelto al cual enganchas las funciones callback, en vez
      de pasar funciones callback a una función.

   La estructura básica de una promesa se combonte de una argumento tipo función conocido como
      executor,la cual tiene dos tipos de parametros, uno para resolver y otro para rechazar

      Promise( function( resolve, reject)){

         resolve("Mensaje de que la promesa fue cumplida");

         reject(new Error("Mensjae que no se pudo completar"));
      }

   Cargamos la libreria request en el archivo para simular un CallBack
*/
const request = require('request');
/*
   Creamos nuestra función asincrona, la cual leerá una url y regresara un mensjae de confirmación
      o de negación de la tarea
*/
function leer(url){
   return new Promise(function(resolve, reject){
      // Función asincrona
      request(url, function(err, response){
         if(err){
            reject(err);
         }
         else{
            resolve(response);
         }
      });
   });
}
/*
   Al ejecutar la función, como es una función asincrona, declararemos métodos .then y .catch para
      asignar cada uno a las funciones responsivas resolve y reject

   Al ejecutar el programa lo declararemos como "node 32 - promesas.js" desde consola.
*/
leer('http://codigofacilito.com')
   .then(function(response){
      console.log(response);
   })
   .catch(function(err){
      console.log(err);
   })
