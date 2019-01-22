/* ------------------------------- 22 - Funciones constructoras -----------------------------------

   La funcion constructora sirve para declarar a un nuevo objeto, contemplando los atributos y
      funciones que esta pueda tener

*/

//   Estas Funciones declaran y definen los objetos
function Curso(){
   this.titulo = "Curso Profesional de javaScript";
   this.inscribir = function(usuario){
      console.log(usuario + " se ha inscrito");
   }
}

/*    Al declarar una función que construye a un objeto, se debe asignar a una variable, denominando
         que dicha variable es un nuevo constructor del objeto
*/
let cursoJavaScript = new Curso();
cursoJavaScript.inscribir("Jair Cano");

/*    Para que una función constructara cumpla con su cometido, sera neccesario que la función reciba
         los parametros debidos.
*/
function Alumno(nombre, apellido){
   this.nombre = nombre;
   this.apellido = apellido;
   this.nombrar = function(){
      console.log("El alumno es " + this.nombre + " " + this.apellido);
   }
}
let alumnoNuevo = new Alumno("Jair", "Cano");
alumnoNuevo.nombrar();
