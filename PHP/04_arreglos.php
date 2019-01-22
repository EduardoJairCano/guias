<?php
/* ------------------------------------------- Arreglos -------------------------------------------
 
    Colección finita de datos múltiples ordenados en filas (unidimencionales) o en columnas y filas (multidimencionales). Pueden ser indexados o asociativos.

    Maneras de crear un arreglo:
      $nombreArreglo = [0, 1, 2, 3, 4];
      $otroArreglo = array('a', 'b', 'c');
*/

/* ------ Arreglos indexados ----------------------------------------------------------------------
    
    Utilizan indices [0, 1, 2, ... , n].
    Empiezan en el 0 y su total siempre empieza en el 1.

*/
$arreglo = array(0, 1, 2, 3, 4, 5);
echo $arreglo[3], '</br>';
echo $arreglo[5], '</br>';
echo $arreglo[1], '</br>';

// Para imprimir todo un arreglo se emplear var_dump() o print_r()
var_dump($arreglo);
echo '</br>';
print_r($arreglo);
echo '</br>';

// Agregar un nuevo valor en la última posición
$arreglo[] = "seis";
echo $arreglo[6], '</br>';
var_dump($arreglo);
echo '</br>';

// Modificar o agregar en una posicion específica
$arreglo[2] = "dos";
echo $arreglo[2], '</br>';
var_dump($arreglo);
echo '</br>';


/* ------ Arreglos asociativos ---------------------------------------------------------------------
    
    Serie de espacios que almacenan datos.
    Se le debe indicar la relación con una llave, clave o nombre.

      $arreglo = ["llave01" => 'Elemento01', "llave02" => 'Elemento02']:
      $arreglo = array("clave01" => 'Dat001', "Clave02" => 'Dato02');

*/
echo '</br>';
$lenguajes = ["lenguaje01" => 'PHP', "lenguaje02" => 'JavaScript', "clave" => 'tuto03'];
echo $lenguajes["lenguaje01"], '</br>';
echo $lenguajes["lenguaje02"], '</br>';
echo $lenguajes["clave"], '</br>';
var_dump($lenguajes);
echo '</br>';


/* ------ Arreglos multidimensional ----------------------------------------------------------------
    
    Interpretadas como matricez, los arreglos multidimensionales cuentan con x número de filas(abajo) y x número de columnas(derecha).

      $matriz [<filas>] [<columnas>]
      echo $matriz[1][3];
      echo $matriz[0][2];

*/
echo '</br>';
$matriz = array(
  //     Col0 - Col1 - Col2
  array('Juan', 23, 'Mexico'),      // fila 0
  array('Fernanda', 22, 'Brasil'),  // fila 1
  array('Mateo', 24, 'España')      // fila 2
);
echo $matriz[0][2], '</br>';
echo $matriz[2][0], '</br>';
var_dump($matriz);
echo '</br>';

$mAsociativa = [
  ["nombre" => 'Jair', "edad" => 26, "pais" => 'Brasil' ],
  ["nombre" => 'Karla', "edad" => 26, "pais" => 'Colombia' ],
  ["nombre" => 'Brayan', "edad" => 15, "pais" => 'Mexico' ]
];
echo '</br>';
echo $mAsociativa[1]["nombre"], '</br>';
echo $mAsociativa[0]["pais"], '</br>';
echo $mAsociativa[2]["edad"], '</br>';
var_dump($mAsociativa);
echo '</br>';

//  Agregar un dato a algun elemento
echo '</br>';
$mAsociativa[0]["Curso"] = 'PHP';
var_dump($mAsociativa[0]);
?>