Algoritmo vector01
	Definir datos Como Entero;
	Definir i Como Entero;
	Dimension datos[4];
	Para i <- 0 Hasta 3 con Paso 1 Hacer
		Escribir "Ingrese dato: <", i+1, ">:";
		leer datos[i];
	FinPara
	Escribir "Valores Cargados: ";
	Para i <- 0 Hasta 3 Con Paso 1 Hacer
		Escribir "Dato en la Pos<", i, ">:", datos[i];
	FinPara
FinAlgoritmo
