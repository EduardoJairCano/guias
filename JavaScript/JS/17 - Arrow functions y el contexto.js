/* ---------------------------- 17 - Arrow functions y el contexto --------------------------------

   Dado que las arrows functions no modifican el valor de "this" y son funciones cortas, se opta
      por emplearlas en funciones dentro de objetos, para que al utilizar "this", los atributos del
      objeto no sufran modificaciones

*/

/*    Tenemos un objeto, el cual cuenta con atributos privados, y una función que itera dichos
         atributos, para que no sean modificados, se emplea una función arrow
*/
let estudiante = {
   nombre: "Jair",
   apellido: "Cano",
   nombreCompleto: function(){
      /* - setTimeout() - es una funcion propia del lenguaje que retrasa la ejecucion

         - 1) Si se utilza una función dentro de una función de un objeto, es probable que al querer
            itera con las variables del objeto, estans tengan un valor indefinido

         - 2) Lo correcto es utilizar una función arrow para que las variables del objeto sean correctas
            setTimeout(()=>{ .....})
      */
       // 1) setTimeout(function(){
      setTimeout(()=>{ // 2) Manera correcta
         console.log(this.nombre + " " + this.apellido)
      },1000);
   }
}

estudiante.nombreCompleto();
