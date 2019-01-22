/* ------------------------------------ 26 - Métodos Estáticos ------------------------------------

   Existen métodos que no necesitan de un objeto para ser ejecutados, llamados métodos estaticos o
      métodos de clase.

   Se debe anteponer la palabra "static" a la función, la cual itera con datos dentro de la clase

   Es posible que el método estatico pueda crear a otro objeto, dicho función se conocer como
   * FACTORY, cuando un objeto crea otro objeto
*/

class Usuario{

   constructor(permisos = "lectura"){
      this.permisos = permisos;
   }

   // Metodos estaticos
   static createAdmin(){
      let admin = new Usuario("Administrador"); // Factory, objeto crea objeto
      return admin;
   }
}

let administrador = Usuario.createAdmin();
