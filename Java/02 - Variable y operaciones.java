public class Main {

	/**
	 * short   - numeros cortos
	 * int     - numeros enteros
	 * long    - numeros enteros largos
	 * float   - numeros flotantes
	 * double  - numeros dobles
	 * byte    - se maneja en bytes
	 * char    - caracteres
	 * boolean - boleanos, verdaderos o falsos
	 * string  - cadenas de texto
	 * operadores aritmeticos + - * / %
	 */

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		int a, b, c, resultado;
		a = 5;
		b = 10;
		c = 2;
		resultado = a + b;
		System.out.println("\n El resultado es de " + a + " mas " + b + " es: "+ resultado);
		resultado = c - a;
		System.out.println(" El resultado es de " + c + " menos " + a + " es: "+ resultado);
		resultado = c * b;
		System.out.println(" El resultado es de " + c + " por " + b + " es: "+ resultado);
		resultado = a / b;
		System.out.println(" El resultado es de " + b + " entre " + a + " es: "+ resultado);

		float x, y;
		double z, res;
		x = (float) 2.5;
		y = (float) 10.0;
		z = 4.5;
		res = x + y;
		System.out.println("\n El resultado es de " + x + " mas " + y + " es: "+ res);
		res = z - x;
		System.out.println(" El resultado es de " + z + " menos " + x + " es: "+ res);
		res = z * y;
		System.out.println(" El resultado es de " + z + " por " + y + " es: "+ res);
		res = y / x;
		System.out.println(" El resultado es de " + y + " entre " + x + " es: "+ res);


	}

}
