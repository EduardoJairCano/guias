package paquete;
// Libreria para realizar un escaneo de texto
import java.util.Scanner;

	/**
	 * > (Mayor menor
	 * >= (Mayor o igual)
	 * < (Menor mayor)
	 * <= (Menor o igual)
	 * == (Igual)
	 * || (Or o "o")
	 * && (And o "y")
	 * ! (Negado)
	 */

public class Main {

	public static void main(String[] args) {

        System.out.println (" Introduce un n�mero: ");
		int var;
		// Creaci�n de un objeto Scanner
		Scanner entrada01 = new Scanner(System.in);
		// Invocamos un m�todo sobre un objeto Scanner
		var = entrada01.nextInt();
		if(var == 10) {
			System.out.println(" La variable es igual a 10 ");
		}
		else if (var < 10) {
			System.out.println(" La variable es menor a 10 ");
		}
		else if (var > 10){
			System.out.println(" La variable es mayor a 10  ");
		}


		System.out.println ("\n Introduce otro numero: ");
		Scanner entrada02 = new Scanner(System.in);
		var = entrada02.nextInt();
		boolean condicion = false;
		if(var > 0 && var < 10) {
			System.out.println(" El numero puede estar entre el 0 y 10 ");

			if (var > 0 && var < 5 ) {
				condicion = true;
			}
			else {
				System.out.println(" El numero puede estar entre el 5 y 10 ");
			}
		}

		else {
			System.out.println(" El numero es mayor que 10 ");
		}

		if (condicion) {
			System.out.println(" El numero es menor que 5 ");
		}
	}
}
