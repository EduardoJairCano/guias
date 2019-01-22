/* ------------------------------------ 21 - Objetos JSON ----------------------------------------

   JavaScript es un lenguaje orientado a prototipos

*/

//    Estructura de JSON
let curso = {
   titulo: "Curso de JavaScript",
   duracion: 2.45,
   formato: "video",
   bloque: ["Introduccion", "Funciones"],
   inscribir: function(usuario){
      console.log(usuario + " esta inscrito");
   }
}
//    Se puede llamar al atributo de diferentes maneras
console.log(curso.titulo);
console.log(curso["formato"]);
console.log(curso.inscribir('Jair Cano'));

/*    Modificar atributos - Es posible realizar el cambio de atributos, asignandolo como si fuese
      una variable cualquiera */
curso.formato = "Podcast";
console.log(curso.formato);

/*    Modificar funciones - Es posible realizar el cambio de la función */
curso["inscribir"] = function() {
   console.log("nueva operacion")
};
curso.inscribir();
