/* ---------------------------------------- 23 - Clases -------------------------------------------

   Tal cual, las clases no existen, en javaScript se emplean prototipos, aunque existe una sintaxis
      alternativa, la cual realiza la misma acción.

*/

//    Declaración de una clase, dentro de las llaves van los metodos y atributos
class Curso{
   // Función constructor, para los atributos
   constructor(titulo){
      this.titulo = titulo;
   }
   // Función
   inscribir(usuario){
      console.log(usuario + " se ha suscrito");
   }
}
//    Para declara una variable de tipo "class", es necesario asignarla a una variable como nueva
let javaScriptCurso = new Curso("Curso Profesional de JavaScript: Clases");
console.log(javaScriptCurso.titulo)
javaScriptCurso.inscribir("Jair Cano");

/*    Class Expression
   - let Curso = class{}
   - let Usuario = class Usuario{}
*/


/*----------------------------------------- Constructor /*-----------------------------------------

   Al generar un nuevo objeto para cada clase (instanciar), es necesario inicializar el objeto

*/
class Usuario {
   constructor(nombre, apellido, status = 'Activo' ){ // status como valor por default
      this.nombre = nombre;
      this.apellido = apellido;
      this.status = status;
   }
}
