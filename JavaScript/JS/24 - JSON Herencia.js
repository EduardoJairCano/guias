/* ---------------------------------------- 24 - Herencia -----------------------------------------

   El objetivo de la herencia es el poder reutilizar la misma funcionalidad, resptenado el diseño de
      las soluciones de los objetos.

   Existira una clase padre, y de él se desprenderan las clases hijos, las cuales tendran ciertos
      atributos y funciones como el padre.

*/

//    Clase padre o base
class Usuario{
   // Atributos
   constructor(nombre){
      this.nombre = nombre;
   }
   // Funciones
   ingresar(){
      console.log(this.nombre + " esta ingresando al sistema");
   }
}

//    Clases hijos, se anexa la palabra reservada "extends"
class Alumno extends Usuario{
   /* Atributos, se emplea un constructor para declarar estos valores, y se utiliza super en caso
         de no existir atributos nuevos */
   constructor(nombre){
      super(nombre);
   }
   // Funciones
   ingresar(){
      // Iteracion de funciones de la clase padre("super"), mandandolas llamar
      super.ingresar();
      console.log("Se ingreso como alumno");
   }
}

class Profesor extends Usuario{
   ingresar(){
      console.log("Ingresando al sistema");
      console.log("Se ingreso como Profesor");
   }
}
let nuevoAlumno = new Alumno("Jair");
nuevoAlumno.ingresar();
let nuevoProfesor = new Profesor();
nuevoProfesor.ingresar();


//    Es posible que exista la herencia desde un constuctor como clase padre
