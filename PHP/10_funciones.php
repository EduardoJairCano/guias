<?php
/* ------------------------------------------- Funciones -------------------------------------------

    Una función es un conjunto de pasos que se emplean con la finalidad de realizar una tarea en específico, dichos pasos pueden ser iteraciones u operaciones con valores que se les hacen llegar a dicha función (parámetros).

    La declaración de una función es de la siguiente manera:

    function <nombre> (<parámetros>) {

      <bloque de codigo>
      <posible retorno de valores>

    }

*/
function suma ($a, $b) {
  $resultado = $a + $b;
  return $resultado;
};

$valor01 = 10;
$valor02 = 20;
echo "El resultado de ".$valor01." más ".$valor02." es igual a: ".suma($valor01, $valor02)."</br></br>";

/* ------------------------------------ Parámetros por default -------------------------------------

    En ocasiones no se reciben parámetros en las funciones, esto ocacionará que las funciones no reaccionen de la manera correcta, para ello, es necesario ingresar valores por default, los cuales ayudaran a evitar esta problematica.

*/

function nombreCompleto($nombre, $apellido, $imprimir=false ) {
  $nombreCompleto = $nombre." ".$apellido;
  if ($imprimir == false) {
    return $nombreCompleto;
  }
  else {
    echo "El nombre completo del sujeto es: ".$nombreCompleto."</br>";
  }
}

  // Maneras de ejecutar la función, primero sin ingresar algun valor para el parámetro por default
  $nombre = "Jair";
  $apellido = "Cano";
  echo "El nombre completo es: ".nombreCompleto($nombre, $apellido)."</br></br>";
  
  // Función con parámetro para el valor default
  nombreCompleto($nombre, $apellido, true);


/* -------------------------------------- Funciones anónimas ---------------------------------------

    Son funciones, las cuales se ingresan en alguna variable en específico, se crea una función como normalmente se realiza y al mandarla a llamar se utilizan () al finalizar.

*/
$mensaje = function (){
  echo "Esta es una función anónima </br></br>";
};
$mensaje();


/* ------------------------------------- Funciones con closure -------------------------------------

    Son funciones, en las cuales se puede dar como parámetro alguna otra función.

*/
// Función Padre
function funcionClosure(Closure $funcionHija, $parametro) {
  return $funcionHija($parametro);
};

// Funciones Hijas, deben ser funciiones anónimas
$saludo = function($parametro) {
  return "Hola ".$parametro.", Bienvenido al curso</br>";
};

$despedida = function($parametro) {
  return "Hasta luego ".$parametro.", Gracias por estar en el curso</br>";
};
echo funcionClosure($saludo, "Jair");
echo funcionClosure($despedida, "Jair Cano");


?>
