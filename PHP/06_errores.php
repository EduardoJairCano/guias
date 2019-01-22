<?php
/* -------------------------------------- Errores en Archivos --------------------------------------

    Contemplando a los errores como la manera en que el sistema nos muestra las posibles fallas en      el código. Estas alertas de errores deben ser mostradas de cierta manera, estos errores no      deben ser vistos por los usuarios en general, sino que deben ser ocultos.

*/

/* --------------------------------------- error_reporting() ---------------------------------------

    Desactivar notificaciones de errores. Normalmente estas funciones van declaradas en el archivo      php.ini

    Dentro de los parámetros de las funciones, es posible ingresar tanto el número 0 para indicar       que mo se desea que se imprima ningun error, como el nombre del tipo de error que se desea      mostrar unicamente.

*/
error_reporting(0);
$variable = 'Hola mundo';
echo $variables;


/* ------------------------------------------ ini_set() -------------------------------------------

    Es posible almacenar los errores en un archivo llamado log de errores, primero se debe              inicializar con la función ini_set("<nombreArchivo>", 1) con el número 1 para inicializar.
    Previo a ello se debe proponer la localización del archivo ini_set("error_log", "<direccion>")

*/
ini_set("log_errors", 1);
ini_set("error_log", "/tmp/php-error.log");
error_log("Hay un error");

?>