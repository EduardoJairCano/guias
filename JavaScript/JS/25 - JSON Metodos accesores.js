/* ------------------------------------ 25 - Métodos accesores ------------------------------------

   Conocidos normalmente como los métodos get and set, son los métodos que proporcionan los valores
      con los que cuenta cada uno de los atributos de algún objeto, es necesario que se realice de
      esta manera, dado que es la menra correcta

*/

class usuario {
   constructor(nombre) {
      this._name = nombre; // los atributos que seran privados se colocan con _ al principio
   }

   // Método get para algun atributo, mostrar
   get name() {
      return this._name;
   }

   // Método set para algun atributo, para modificar
   set name(nombre) {
      this._name = nombre;
   }
}

let user = new usuario('jair');

// Se accede a la funcción get como si fuera un atributo
console.log(user.name);


// Pra modificar el nombre con la función set
user.name = "Eduardo";
console.log(user.name);
