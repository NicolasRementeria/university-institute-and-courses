Algoritmo NumerosPrimos
	// Dado un vector vec, de 20 posiciones, cargados con numeros aleatorios,
	// entre 1 y 100, determine cuantos numeros primos existen en el
	
	// Guardar en un vector los numeros primos, y luego mostrar 
	// el numero primo mas grande con su indice, 
	// si se repite varias veces mostrar todos los indices
	
	Definir vec Como Entero;
	Definir cantPrimos Como Entero;
	Definir i, divisor Como Entero;
	Definir noEsPrimo Como Entero;;
	Dimension vec[20];
	cantPrimos <- 0;
	
	Para i<-0 Hasta 19 Con Paso 1 Hacer
		//(cota superior - cota inferior + 1) + cota inferior
		//(cs-ci+1)+ci
		vec[i] <- azar(100-1+1)+1;
	FinPara
	
	Para i<-0 Hasta 19 Con Paso 1 Hacer
		noEsPrimo <- 0;
		Para divisor<-2 Hasta vec[i]-1 Con Paso 1 Hacer
			Si (vec[i] mod divisor == 0) Entonces
				noEsPrimo <- 1;
			FinSi
		FinPara
		Si noEsPrimo == 0 Entonces
			Mostrar vec[i], " es Primo";
			cantPrimos <- cantPrimos + 1;
		FinSi
	FinPara
	Mostrar "Cantidad de Primos: ", cantPrimos;
	
FinAlgoritmo