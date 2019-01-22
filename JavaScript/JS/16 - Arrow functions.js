/* ------------------------------------ 16 - Arrow functions --------------------------------------

   Es posible definir una función de otra manera, en este caso se puede declarar una función dentro
         de una variable. Se utilizan para funciones rápidas que se ejecutan en un solo renglon.

   let <variable> = ()=> {
      <......>
   }

   let <variable> = ()=> <......>;

*/
//    Función en varios renglones
let hola_mundo = ()=>{
   console.log("Hola mundo");
}

//    Función en una sola linea
let hola = ()=> console.log("Hola nada mas");


//    Equivalencia de funciones
function suma(a,b){
   return a+b;
}
console.log(suma(2,3));

suma_arrow = (a,b)=> a+b
console.log(suma_arrow(2,3));
