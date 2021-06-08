Algoritmo ejercicio03
	// dado un ingreso de nota
	// se pide al ingresar valide su rango entre 1 y 10
	// incluyendo sus extremos
	// si la nota esta entre ese rango, poner el mensaje NOTA CORRECTA
	// Si no lo es, poner el mensaje VUELVA A INGRESAR NOTA ENTRE 1 Y 10 
	// Una vez superada la validacion, mostrar la nota
	definir nota Como Entero;
	Hacer
		Escribir  "Ingrese nota entre 1 y 10";
		Leer  nota;
		si nota < 1 o nota > 10
			Escribir "VUELVA A INGRESAR NOTA ENTRE 1 Y 10";
		FinSi
	Mientras Que nota > 10 o nota < 1; 
	Escribir "NOTA CORRECTA";
	
FinAlgoritmo
