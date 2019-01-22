/* ---------------------------------- 18 - Call Apply y Bind --------------------------------------

   call  -  Ejecuta una función de inmediato, argumentos acomodados por orden
   apply -  Ejecuta una función de inmediato, argumentos se envian por medio de un arreglo
   bind  -  No invoca directamente a la función sino que devuelve una copia que hace referencia al 
            objeto this que se especifique, junto con los argumentos proporcionados:


   Call: https://developer.mozilla.org/es/docs/Web/JavaScript/Referencia/Objetos_globales/Function/call
   Apply: https://developer.mozilla.org/es/docs/Web/JavaScript/Referencia/Objetos_globales/Function/apply
   Bind: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind
*/

/*    Se cuenta con un objeto con funciones propias, el cual sera ejecutado por alguna función
         auxilar, como el objeto cuenta con contexto propio, al querer iterar dicho contexto fuera
         del objeto, los valores seran indefinidos.
*/
function executor(funcion){
   funcion();
}
let estudiante = {
   nombre : "Jair",
   apellido: "Cano",
   nombreCompleto: function(){
      console.log(this.nombre + " " + this.apellido);
   }
}
executor(estudiante.nombreCompleto);


/*    Para que los valores o el contexto del objeto pueda ser utilizado fuera del objeto, sera
         necesario implementar ciertos métodos.
      .call() - es un metodo de una función en la cual sera neccesario dar como argumento el nombre
         del objeto que se desea obtener el contexto

         <funcion>.call(<argumentos1, argumento2, ... >);

      .apply() - funciona de la misma manera, solo que lo argumentos son declarados en un arreglo

         <funcion>.call(< [argumento1, argumento2, ... ] >);
*/
function executor2(funcion){
   funcion.call(tutor);
}
let tutor = {
   nombre : "Jair",
   apellido: "Cano",
   nombreCompleto: function(){
      console.log(this.nombre + " " + this.apellido);
   }
}
executor2(tutor.nombreCompleto);


/*    El método bind emplea el paso de una función exactamente igual, en la cual el contexto no
         sufre alteraciones.
      En esta opción, bind es delcarado como método en el argumento empleado al llamar la función
         auxiliar.

      .bind() - se emplea el paso de argumentos conforme al contexto que sea desea obtener

         <funcionAuxiliar(<argumento>.bind( <contexto> ))>

      La función auxiliar no sufre ningun cambio o el empleo de un metodo
*/
function executor3(funcion){
   funcion();
}
let profesor = {
   nombre : "Jair",
   apellido: "Cano",
   nombreCompleto: function(){
      console.log(this.nombre + " " + this.apellido);
   }
}
 // bind se declara al llamar la función auxiliar
executor3(tutor.nombreCompleto.bind(profesor));
