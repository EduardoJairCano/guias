/* ------------------------------------- 15 - El contexto -----------------------------------------

   This  -  Representa al codigo que se esta ejecutando en ese momento, es flexible y muy dinámico,
            es posible cambiar el paradigma de programación.

*/

/*    En función de un objeto, se puede considerar como la creación de variables privadas, al
         emplear "this", se puede considerar como la selección del contexto en que se manda llamar
*/
let usuario = {
   nombre : "Jair",
   apellido : "Cano",
   nomreCompleto: function(){
      console.log(this.nombre + " " + this.apellido);
   }
}

usuario.nomreCompleto();
