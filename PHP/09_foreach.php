<?php
/* ------------------------------------------- foreach() -------------------------------------------

    Esta función es de uso exlusivo para iterar sobre los arreglos, emplea el uso de asignación para una variable que se estará iterando.

*/

/* ------------------------------- foreach() en arreglos sin indices -------------------------------

    Solo se emplea el elemento que se desea imprimir.

    foreach(<arreglo> as <elemento>) {
      
    }
*/
$arreglo = ["Dato01", "OtroDato", TRUE, 04, "Uno mas", 10.5];
foreach($arreglo as $item) {
  echo $item."</br>";
}


/* ------------------------------- foreach() en arreglos con indices -------------------------------

    Contemplando que exista un arreglo con indices, es necesario ingresar un valor por default para el compo indice del arreglo.

    foreach(<arreglo> AS <campoIndice> => <elemento>) {

    }

*/
$arregloConIndices = [
  "Nombre"=>'Jair', 
  "Apellido"=>'Cano', 
  "Edad"=>26, 
  "Ocupacion"=>'Desarrollador', 
  "Salario"=>10000];
foreach($arregloConIndices AS $llave => $item) {
  echo $llave.": ".$item."</br>";
}


?>