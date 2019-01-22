/* --------------------------------- 28 - Herencia de Prototipos ----------------------------------

      Se crea un objeto con valor null y se asigna a una variable

*/
let animal = Object.create(null);

//    Se le asignan al objeto un atributo y una función
animal.vivo = true;
animal.estaVivo = function(){
   if (this.vivo) console.log("El animal esta vivo.");
}
console.log(animal.vivo);
animal.estaVivo();

/*    Se creara un prototipo en base al objeto animal, el cual contará con todos los atributos y
         funciones que la clase o prototipo base o padre
*/
let perro = Object.create(animal);

/*    Al mandar llamar una función en el nuevo prototipo, conocido como delegación, el interprete
         realizara la busqueda en el prototipo que se manda llamar, al no encontrarlo buscara en el
         objeto padre, y asi secuencialmente hasta encontrarlo, a esto se le conoce como CADENA DE
         PROTOTIPOS.
      En caso de buscar algun atributo que no exsita, el interprete buscara por todos los prototipos
         en caso de no encotrar dicho valor, regresera "undefind".
*/
perro.estaVivo();
