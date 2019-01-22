/* --------------------------------- 04 - Múltplies promesas --------------------------------------

   Para ejecutar un calculo o procesar datos, es necesario esperar a que ciertas funciones terminen,
      al emplear CallBacks resulta provechos ante dicha situación, es posible emplear el método
      estático "all" para ejecutar varias promesas.

   Primero se declararán varias promesas.

   ** Para ejecutar este script desde cmd en la carpeta contendora "node <archivo.js>"
*/
let p1 = new Promise((resolve,reject)=>setTimeout(resolve,500,'Hola mundo P1'));
let p2 = new Promise((resolve,reject)=>setTimeout(resolve,600,'Segundo hola mundo P2'));
let p3 = Promise.reject(); // promesa con fallo por deafult
let saluda = ()=> console.log("Hola a todos");

// Aqui se ejecutaría el resolve para la promesa 1 despues de 500 milisegundos or setTimeout
p1.then(console.log);

/* En caso de querer que cada uno de la promesas se vea ejecutada consecuentemente,puede emplearse
      de la siguiente manera:
*/
p1.then(function(){
   p2.then(function(){
      saluda();
   })
})
/* Aunque viendolo de la manera anterior, no es la manera correcta de encadenar o ejecutar varias
      promesas, aunque funcione, se ha caido en el CallBack Hell, con funciones ejecutandose dentro
      de otras funciones.

   La manera correcta seria ejecutando el método estático "all", el cual recibe como parámetros un
      iterable (arreglo de promesas), el método genera una nueva promesa que se ejecuta hasta que
      todas las promesas del arreglo han sido resultas o falla, en caso de que alguna de las promesas
      del arreglo falle.
*/
Promise.all([p1,p2]).then(resultados=>{
   console.log(resultados); // para visualizar las promesas.
   saluda();
})

/* Para demostrar que Promise.all falla con al menos una promesa del arreglo falle, se coloca p3 en
   el arreglo, de esta manera se podra visualizar que el Promise.all falla y se ejecuta el reject
*/
Promise.all([p1,p2,p3]).then(resultados=>{
   console.log(resultados);
   saluda();
}).catch(()=>console.log('La promesa fallo....'));
