/* ---------------------------------- 14 - Funciones anónimas -------------------------------------

   Las Funciones pueden retornar Funciones, las funciones anonimas pueden ser consideradas como Las
      funciones principales, que suele tener una funcion que se llama dentro de otra función.

*/

//    Función ejecutadora
function executor(funcion){
   funcion();
}
//    Función anonima
function saludar(){
   console.log("Hola");
}
executor(saludar());
