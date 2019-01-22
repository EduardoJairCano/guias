<?php
/* ------------------------------------ Operadores aritméticos -------------------------------------
 
    Operadores aritméticos:
    
    +  Suma
    -  Resta
    *  Multiplicación
    /  División
    %  Módoulo

*/
$a = 2;
$b = 4;
$c = 10;

echo 'Suma: ', $a + $b, '</br>';
echo 'Resta: ', $c - $b, '</br>';
echo 'Multiplicación: ', $a * $b, '</br>';
echo 'Division: ', $c / $a, '</br>';
echo 'Módulo: ', $b % $c, '</br>';


/* ----------------------------------- Operadores de asiganción  -----------------------------------
 
    Operadores asignación:
    
    =  Igualar una variable a algun valor.
    +=  Igualar y sumar un valor.
    *=  Igualar y multilpicar.
    /=  Igualar y dividir.
    .=  Concatenar.

*/
$a = 10;
echo 'Valor = ', $a, '</br>';
$a += 5; // Es iguala a 'a = a + 5' 
echo 'Valor += 5: ', $a, '</br>';
$a *= 2;
echo 'Valor *= 2: ', $a, '</br>';
$a /= 6;
echo 'Valor /= 6: ', $a, '</br>';
$a .= 5; // Es igual $a = 'a'.'5'
echo 'Valor .= .5: ', $a, '</br>';


/* ---------------------------- Operadores de incremento - decremento  -----------------------------
 
    Operadores de incremento:
        pre-incremento:   ++$variable - Primero incrementa variable
        post-incremento:  $variable++ - Variable más 1

    Operadores de decremento:
        pre-decremento:   --$variable - Primero decrementa variable
        post-decremento:  $variable-- - Variable menos 1
*/
$b = 5;
echo '</br>Valor:  ', $b, '</br>';
$nuevo = ++$b;
echo 'Pre-incremento:  ', $nuevo, '</br>';
$b = 5;
$nuevo = $b++;
echo 'Post-incremento: ', $nuevo, '</br>';
$b = 5;
$nuevo = --$b;
echo 'Pre-decremento:  ', $nuevo, '</br>';
$b = 5;
$nuevo = $b--;
echo 'Post-decremento: ', $nuevo, '</br>';


/* ----------------------------------------- Evaluadores -----------------------------------------
 
    Evaluadores para concatenar dos condicionales:
    and   - Para agregar dos o más condicionales que se tiene o no que cumplir ambas
            ejemplo: $edad == 26 and $nombre == "juan"
    
    or    - Para agregar dos o más condicionales, de las cuales solo tiene que cumplir una al menos.
            ejemplo: $edad > 0 or $respira == TRUE

    Tipos de igualaciones:
    ==    - Para corroborar que el valor de una variable es igual a otro.
            "207" == 207; TRUE

    ===   - Para corroborar que tanto el valor, como el tipo de dato de una variable es igual a             otro.
            "207" == 207; FALSE
             207 === 207; TRUE
*/
?>