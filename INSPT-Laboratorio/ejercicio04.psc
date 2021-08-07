Algoritmo ejercicio04
	// dado un lote de 10 numeros
	// determinar cual es el mayor
	definir may Como Entero;
	definir num Como Entero;
	definir i Como Entero;
	Para i<-0 Hasta 9 Con Paso 1 Hacer
		Escribir "Ingrese numero ", i+1, ":";
		Leer num;
		Si i == 0 Entonces
			may <- num;
		FinSi
		si num > may Entonces
			may <- num;
		FinSi
	FinPara
	Escribir "El numero mayor es ", may;
FinAlgoritmo
