// calcular el factorial de un numero cualquiera

Algoritmo factorial
	// no existe para numeros negativos y numeros que no sean 
	// enteros
	// el factorial de 0 == 1
	// el factorial de 1 == 1
	// el factorial de 4 == 4*3*2*1
	Definir num Como Entero;
	Definir resultado Como Entero;
	Definir i Como Entero;
	resultado <- 1;
	
	Repetir
		escribir "Ingrese un numero no negativo: ";
		leer num;
	Mientras Que (num < 0);
	
	Para i<-1 Hasta num Con Paso 1 Hacer
		resultado = resultado * i;
	FinPara
	
	//Escribir "El factorial de ", num, " es: ", resultado;
	escribir "el factorial de num:",num," es :",resultado; 

FinAlgoritmo
