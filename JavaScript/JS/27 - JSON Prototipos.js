/* --------------------------------------- 27 - Prototipos ----------------------------------------

   JavaScript es un lenguaje Orientado a Prototipos, esto quiere decir que las clases no existen,
      lo que lleva a que los objetos se crean apartir de otros objetos.

   Visto de otra manera, siempre existira una clase u objeto base, el cual, en vez de ser iterado,
      se construira un objeto copia, o un prototipo, en el cual se declarán las nuevas modificaciones.

   Tomando como consideración la formula JSON para crear un nuevo objeto, se considera que dicho
      objeto sea definido como un prototipo de un objeto, por que cuenta con al atributo __proto__,
      el cual defino como es que se creeo dicho objeto

*/


// Sintaxis básica para crear objetos JSON
let user = {
   nombre : "Jair"
};

// Que tipo de dato es "user"
console.log(typeof user);

// Deriva como es que se compone el objeto "user"
console.log(user.__proto__);
