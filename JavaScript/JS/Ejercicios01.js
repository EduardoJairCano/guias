/*
   1. Tomando como entrada un número entero, imprimir si es par o impar.
*/
let numero = prompt(" Escriba un numero: ")
if (numero%2 == 0){
   console.log("1. El numero ingresado es par\n");
}
else{
   console.log("1. El numero ingresado es impar\n");
}


/*
   2. Recibir dos números usando prompt y sumarlos, restarlos, dividirlos y multiplicarlos
*/
let a = prompt(" Ingrese un primer numero: ")
let b = prompt(" Ingrese un segundo numero: ")
let resultado = a;
resultado = a+b;
console.log("\n2. La suma de " + a + " mas " + b + " es: " + resultado);
resultado = a-b;
console.log("   La resta de " + a + " menos " + b + " es: " + resultado);
resultado = a/b;
console.log("   La division de " + a + " entre " + b + " es: " + resultado);
resultado = a*b;
console.log("   La multiplicacion de " + a + " por " + b + " es: " + resultado);


/*
   3. Imprimir la sucesión fibonacci el número de veces que indicó el usuario
*/
numero = prompt(" Ingrese un numero para Don Fibonacci: ")
a = 0;
b = 1;
let c;
console.log("3.\n")
for(let i=0; i<numero; i++) {
   c = a+b;
   a = b;
   b = c;
   console.log("   " + a);
}


/*
   4. Programar el juego del "Número Mágico" en el que se define un número y el usuario trata de
      adivinarlo, si el número que ingresó el usuario es menor, imprimir la pista
      "El número mágico es mayor", si el número que ingresó el usuario es mayor,
      imprimir la pista "El número mágico es menor".
*/
