Algoritmo vector02
	// cargar numeros al azar entre 50 y 250, CI=50 CS=250
	// (cs-ci+1)+ci;
	// en un vector llamado vec de 30 posiciones
	Definir vec Como Entero;
	Definir i Como Entero;
	Dimension vec[30];
	Para i <- 0 Hasta 29 con Paso 1 Hacer
		vec[i] = azar(250-50+1)+50;
	FinPara
	Escribir "Valores Cargados: ";
	Para i <- 0 Hasta 29 Con Paso 1 Hacer
		Escribir "Dato de la Pos<",i,">:", vec[i];		
	FinPara
FinAlgoritmo
