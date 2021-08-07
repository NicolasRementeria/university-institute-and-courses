Algoritmo ejercicio02
	// realizar un ingreso de una cantidad de notas
	// solicitadas por el usr, debiendo calcular el promedio
	// de las mismas
	//ambiente de datos
	definir nota Como Entero;
	definir acumNotas Como Entero;
	definir cantNotas Como Entero;
	definir i Como Entero;
	definir promedio Como Real;
	acumNotas <- 0;
	escribir "Ingrese cantidad de notas a procesar";
	leer cantNotas;
	Para i<-0 Hasta cantNotas-1 Con Paso 1 Hacer
		Escribir "Ingrese nota", i+1, ":";
		leer nota;
		acumNotas <- acumNotas + nota;
	FinPara
	promedio <- acumNotas / cantNotas;
	Limpiar Pantalla;
	escribir "El promedio fue: ", promedio;
FinAlgoritmo
