/* ------------------------------- 20 - Metodos de los arreglos -----------------------------------

   forEach  -  Sirve para recorrer un arreglo
   filter   -  Elimina elementos del arreglo basados en un filtro
   find     -  Busca algun elemeto en el arreglo
   map      -  Realiza operaciones con los elementos y los asigna en un nuevo arreglo

*/

//    Arreglo de lenguajes
let arreglo = ["Python", "Java", "JavaScript", "C++"];

//    filter() -  Crea un nuevo arreglo, eliminando los criterios que se otorgen para el filtro
arreglo = arreglo.filter(function(el){
   return el != "Java";
});
/*    Empleando la metodología arrows functions, se podria emplear la funcion de la siguiente manera:
         arreglo = arreglo.filter((el)=> el != "Java");
*/

//    forEach()  -   Selecciona cada uno de los elementos del arreglo
arreglo.forEach(function(elemento){
   console.log(elemento);
});

//    find()   -     Localiza un elemento en el arreglo
let elemeto = arreglo.find(el => el == "JavaScript");
console.log(elemeto);

//    map()    -     En esta ocacion realizara el cuadrado a un arreglo de números
let numeros = ["2", "54", "7", "12", "5"];
let cuadrados = numeros.map(numero => numero * numero);
console.log(cuadrados);
//    map()    -     En esta ocacion realizara un castinig de tipo de datos
let enteros = numeros.map(numero => parseInt(numero));
console.log(enteros);
