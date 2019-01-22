<?php
/* ----------------------------------------- Condicionales -----------------------------------------

    Contemplando como una estructura de control, las condicionales y ciclos son una serie de instrucciones lógicas que determinan un bloque de código.
    
    La forma básica de las condicionales es la siguiente:

      if (<condición>) {

        <bloque de codigo>

      } else if (<condición>) {
        
        <bloque de codigo>

      }
      else {

        <bloque de codigo>

      }
*/
$numero = 6;
if ($numero ==  0) {
  echo "El número es igual a 0</br>";
} 
else if($numero > 0 and $numero <= 10) { // 'and' 'or' para agregar más condicionales
  echo "El número es mayor a 0 pero menor a 10</br>";
}
else{
  echo "El número es mayor a 10</br>";
}

/* ------------------------------ Condicionales con operador ternario ------------------------------

    Es posible ingresar una estructura en una sola linea de código, la cual se determina como condicionales con operador ternario, en ella es necesario ingresar la condicional al principio, se agregar un sigo de pregunta, despues la primera respuesta posible, y en segunda instancia alguna operación para el else:

      <variable a donde se asignará> = ($variable y condicional) ? <primera igualación> : <else>

    Esta operación solo se suele emplear para una conficional if-else.
*/
$operadorTernario = ($numero == 1) ? 1:"no es uno";
echo "El número es ", $operadorTernario, "</br>";


/* ----------------------------------------- Switch - Case -----------------------------------------

    Contemplando como la elección propia entre diferentes posibles iteraciones, switch-case es una de las condicionales empleadas para la selección de algun caso en específico.

    Estructura básica switch-case:

      switch( <condicion> ) {
        case X:
          
          <bloque de codigo>
          
          break;
        
        default: // valor por default, en caso de que no sea posible alguno de los anteriores.
          
          <bloque de codigo>

          break;
      }
*/
$condicion = 3;
switch( $condicion ) {
  case 1:
    echo "Se ingreso a la opción ", $condicion, "</br>";
    break;
  case 2:
    echo "Se ingreso a la opción ", $condicion, "</br>";
    break;
  case 3:
    echo "Se ingreso a la opción ", $condicion, "</br>";
    break;
  default:
    echo "Se ingreso a la opcion por default </br>";
    break;
}

?>