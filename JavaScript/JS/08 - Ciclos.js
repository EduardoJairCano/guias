/* ----------------------------------------- 08 - Ciclos ------------------------------------------

   Ciclo for()
      break    - Rompe el ciclo
      continue - Ejectua la iteracion siguiente

   Ciclo while(<expresion booleana>)

   Ciclo do { --- } while (<expresion booleana>)

*/

//    for() - imprime los números del 0 al 10
for(let i=0; i<=10; i++) {
   console.log(i);
}
console.log("\n");

//    Solo se imprime hasta el numero igual o menor que 5 por medio de la palabra reservada "break"
for(let i=0; i<=10; i++) {
   if(i > 5) break;
   console.log(i);
}
console.log("\n");

//    Solo se imprimen los números impares por medio de la palabra reservada "continue"
for(let i=0; i<=10; i++) {
   if(i%2 == 0) continue;
   console.log(i);
}
console.log("\n");


//    whike() - imprime el valor de i hasta que la condición cambie de valor a false
let i = 0;
while(i <= 10) {
   console.log(i);
   i++;
}
console.log("\n");

//    do{} while() - En este ciclo se realizara la función, dado que la condicion se realiza despues
i = 0;
do{
   i++;
   console.log(i);
}while (i <= 10)
