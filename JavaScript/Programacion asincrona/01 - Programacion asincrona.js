/* -------------------------------- 01 - Programacion asincrona -----------------------------------

   Conocido tambien como ciclo de vida o event loop, la Programacion asincrona, es la ejecucion de
      varias tareas de manera eventual, turnando las ejecuciones de cada unas de las tareas, con el
      fin de que la finalización de cada una de ellas sea en tiempos parecidos

*/

/* ---- CallBack ----------------------------------------------------------------------------------

   Es una función que se pasa como argumento a una operación asincrona, con la idea de que dicha
      función se ejectue cuando el proceso asincrono termine.

   Como ejemplo, se realizara una operación que pueda tardar más tiempo de lo esperado, con el fín
      de aprovechar la programación asincrona. La función que se empleará en esta ocación sera ir a
      la página de google.

   Para realizar esta función se instalar la libreria "request", situandonos desde la temrinal en
      la carpeta donde se ejecutara dicho programa, por medio del manejador de paquetes de NodeJS y
      el comando "npm install request", para las dependencias necesarias.

   Se asignara la función request a una constante, en la cual se importara la libreria           */
const request = require('request');

/* Para la función request se da como parametros, primero la función que se desea realizar y despues
      la función CallBack que se ejecutará para saber donde ha terminado la primera función
*/
request('http://google.com', function(){
   console.log("Se termino la petición de Google");
})

/* Esta linea se ejecutara alternadamente con la petición request, dado que se emplea la programación
      asincrona, y las funciónes cumplen con el event loop
*/
console.log(" Que más puedo hacer para usted?");
