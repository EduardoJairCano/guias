<?php
/* ---------------------------------- Variables, Operadores y Datos --------------------------------

    Se les denomina variables a cualquier dato que comparte un conjunto común de características. Las variables en php pueden ser de distintos tipos.
      Tipo ESCALAR, dado que solo pueden representar un solo valor:
        - Enteros
        - Flotantes
        - Cadenas
        - Booleanos

        - Arreglos
        - Objetos
        - Nulos
        - Recursos

*/

$string01 = "Cadena 01";
$string02 = "Otra cadena, pero tiene que estar entre comillas";
$booleano01 = true;
$booleano02 = FALSE;
$entero01 = 10;
$entero02 = -5;
$flotante01 = 132.34;
$flotante02 = 3.1416;

echo "Variables String: $string01", " - $string02</br>";
echo "Variables Bool: $booleano01", " - $booleano02</br>";
echo "Variables Int: $entero01", " - $entero02</br>";
echo "Variables Flot: $flotante01", " - $flotante02</br>";


/* ------------------------------------ gettype() y var_dump() -------------------------------------
 
    La función gettype() regresa el tipo de valor que emplea un variable.
    La función var_dump() regresa el tipo de valor, el valor y otros datos más.

*/
echo gettype($string01), " - String - ", var_dump($string01), "</br>";
echo gettype($booleano01), " - Bool - ", var_dump($booleano01), "</br>";
echo gettype($entero01), " - Int - ", var_dump($entero01), "</br>";
echo gettype($flotante01), " - Float - ",var_dump($flotante01), "</br>";


/* ------------------------------------- Variables Constantes --------------------------------------

    Las variables de tipo constantes son un espacio en memoria que no puede ser cambiado durante la interpretación del código.

*/
define('URL', 'https://www.youtube.com');
echo URL, '</br>';


/* ------------------------------------- Valor por Referencia --------------------------------------

    Es posible asignar datos por referencia entre variables, solo es necesario emplear el caracter & antes de la variable que se desea igualar.

*/
$variable = "El dato";
$variableReferencia = &$variable;
echo $variableReferencia, "</br>";

?>