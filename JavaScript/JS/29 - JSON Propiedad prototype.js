/* ---------------------------------- 28 - Propiedad prototype ------------------------------------

   La funcion prototype cuenta con el mismo valor que la palabra reservada __proto__, a diferencia
      que la funcion prototype se emplea cuando, al crear una clase o función primaria, la cual
      tendra objeto o prototipos hijos, y se le desea modificar algún valor, atributo o funcion en
      específico.

*/

// Función padre llamada User()
function User(){}
// Se crea un nuevo tipo de funcion llamado Admin, el cual sera un prototipo de User
function Admin(){}
// por medio de la función prototype, se asigna Admin como hijo de User

Admin.prototype = new User();
// Se modifica algún valor, atributo o función a la clase padre, por medio de la función prototype

User.prototype.saludar = function(){
   console.log("Hola");
}
// Se asigna una variable para un nuevo Admin() y despues se ejecuta la funcion propia de User
let jair = new Admin();
jair.saludar();
