<?php
/* ------------------------------------- Funciones en Arreglos -------------------------------------

    Conocidas como funciones nativas, son funciones bativas propias del lenguaje, con las cuales se     puede aplicar en los arreglos.

*/
$cadena = '';
$arreglo = [];
$dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes'];

/* -------------------------------------------- empty() --------------------------------------------

    Función del tipo Bool, corrobora si el arreglo esta vacio o no.

*/
var_dump(empty($arreglo));
echo '</br>';
var_dump(empty($dias));
echo '</br>';

/*  ------------------------------------------- isset() --------------------------------------------

    Función de tipo Bool, corrobora si se encuentre en el arreglo algun dato en cierto indice.

*/
var_dump(isset($dias[2])); // existe elemento en la posicion 2?
echo '</br>';

/* -------------------------------------------- count() --------------------------------------------

    Devuelve el número total de elementos elementos del arreglo.

*/
echo count($dias);
echo '</br>';
// Obtener el penultimo elemento del arreglo
$contador = count($dias) - 2;
echo $contador, " = ", $dias[$contador];
echo '</br>';

/* -------------------------------------------- sort() ---------------------------------------------

    Ordena el arreglo original en orden alfabética, es decir, se pierde el orden original.

*/
echo '</br>';
var_dump($dias);
echo '</br>';
sort($dias);
var_dump($dias);
echo '</br>';

/* -------------------------------------------- rsort() --------------------------------------------

    Ordena el arreglo original en orden inverso alfabético, es decir, se pierde el orden original

*/
echo '</br>';
var_dump($dias);
echo '</br>';
rsort($dias);
var_dump($dias);
echo '</br>';

/* -------------------------------------------- asort() --------------------------------------------

    Ordena el arreglo en orden alfabética, pero conserva el orden del indice.

*/
echo '</br>';
var_dump($dias);
echo '</br>';
asort($dias);
var_dump($dias);
echo '</br>';


/* ------------------------------------------- arsort() --------------------------------------------

    Ordena el arreglo en orden inverso alfabético, pero conserva el orden del indice.

*/
echo '</br>';
var_dump($dias);
echo '</br>';
arsort($dias);
var_dump($dias);
echo '</br>';

/* ------------------------------------------ array_sum() ------------------------------------------

    Suma todos los elementos numéricos de un arreglo.

*/
echo '</br>';
$numeros = [1, 2, 3, 4];
echo array_sum($numeros);
echo '</br>';

/* ----------------------------------------- array_diff() ------------------------------------------

    Encontrar las diferencias entre arreglos, solamente agrega a un nuevo arreglo los elementos del   primer arreglo que no se encuentran en el segundo arreglo

*/
echo '</br>';
$a = [2, 4, 6, 8, 10];
$b = [2, 3, 6, 7, 10];
$dif = array_diff($a, $b);
var_dump($dif);
echo '</br>';

/* ----------------------------------------- array_chunk() -----------------------------------------

    Dividir el arreglo en un número especficio de elementos.

*/
echo '</br>';
$serie = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
$dividir = array_chunk($serie, 3);
var_dump($dividir);
echo '</br>';

/* ----------------------------------------- array_merge() -----------------------------------------

    Unir dos arreglos.

*/
echo '</br>';
$nombres = ['Eduardo', 'Jair'];
$apellidos = ['Cano', 'López'];
var_dump(array_merge($nombres, $apellidos));
echo '</br>';

/* ----------------------------------------- array_ pop() ------------------------------------------

    Eliminar el último elemento del arreglo.

*/
echo '</br>';
$nombres = ['Eduardo', 'Jair', 'Cano', 'López'];
var_dump($nombres);
echo '</br>';
array_pop($nombres);
var_dump($nombres);
echo '</br>';

/* ----------------------------------------- array_ push() -----------------------------------------

    Agregar un último elemento del arreglo.

*/
echo '</br>';
$nombres = ['Eduardo', 'Jair', 'Cano', 'López'];
var_dump($nombres);
echo '</br>';
array_push($nombres, 'Extra');
var_dump($nombres);
echo '</br>';

/* ---------------------------------------- array_ search() ----------------------------------------

    Buscar un elemento especifico en el arreglo. La función regresa un int con la posicion del        elemento.

*/
echo '</br>';
$nombres = ['Eduardo', 'Jair', 'Cano', 'López'];
var_dump($nombres);
echo '</br>';
$find = array_search('Jair', $nombres);
var_dump($find);
echo '</br>';
echo $find;
echo '</br>';

?>
