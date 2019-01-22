<?php
/* -------------------------------------------- Ciclos ---------------------------------------------

    Contemplado como las secuencias repetitivas de código, en los ciclos de propgramación se emplean para obtener ciertas iteraciones en el código hasta que suceda cierta condición.

*/

/* --------------------------------------- while (mientras) ----------------------------------------

    Se ejecutará el codigo hasta que se cumpla la condicional, puede finalizar antes de lo esperado.

*/
$i = 0;
while($i < 5) {
  echo "El numero es: ".$i."</br>";
  $i++;
}

// Ciclos con valores bandera
$frutas = ["naranja", "melon", "platano", "uva", "fresa"];
$banderaEncontrado = FALSE;
$i = 0;
while(!$banderaEncontrado) {
  if ($frutas[$i] == 'platano') {
    echo "Si hay ".$frutas[$i]. " en el refrigerador </br>";
    $banderaEncontrado = TRUE;
  }
  else 
  {
    echo "Encontramos ".$frutas[$i]." en el refrigerador </br>";
  }
  $i++;
}


/* ------------------------------------- do - while (mientras) -------------------------------------

    Se ejecutará el código hasta que se concluya el total de los las iteraciones contempladas.

*/
$i = 0;
do {
  echo "La cuenta va en: ".$i."</br>";
  $i++;
} while($i < 5);


/* ------------------------------------------ for (para) -------------------------------------------

    Contemplando 3 aspectos necesario para este ciclo, la primera inicializa la iteración, la segunda evalua la misma, y la tercera determina el final del ciclo

*/
for($i=0; $i<5; $i++) {
  echo "Estamos en la iteración ".$i."</br>";
}

/* ------------------------------------- Sucecion de Fibonacci -------------------------------------
*/

echo "</br> Fibonacci con While() </br>";
$a = 0;
$b = 1;
$n = 0;
while($n < 50) {
  $n = $a + $b;
  $a = $b;
  $b = $n;
  echo $n."</br>";
}

echo "</br>  Fibonacci con Do-While() </br>";
$a = 0;
$b = 1;
$n = 0;
do {
  $n = $a + $b;
  $a = $b;
  $b = $n;
  echo $n."</br>";
} while($n < 50);

echo "</br>  Fibonacci con For() </br>";
$a = 0;
$b = 1;
$n = 0;
for( $n=0; $n<50; $n=$a+$b){
  $a = $b;
  $b = $n;
  echo $n."</br>";
}


?>