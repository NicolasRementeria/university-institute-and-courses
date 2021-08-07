Algoritmo SimulacionTiradaDeDados
	// Simular una tirada de 2 dados
	// La misma se debe reiterar 9000 veces
	// Determinar cuantas veces se repiten los numeros y graficar 
	// o mostrar
	// Un dado tiene 6 caras, valores de 1 a 6, CI=1 CS=6
	// Es decir, llevar un contador por cada resultado de combinacion 
	// y mostrar
	definir dado1,dado2,dadoFinal Como Entero;
	definir cs,ci Como Entero;
	definir i Como Entero; // la cantidad de tiradas
	definir tiradas Como Entero;
	Dimension tiradas[11];
	cs<-6;
	ci<-1;
	Para i<-0 Hasta 9000-1 Con Paso 1 Hacer
		dado1<-azar(cs-ci+1)+ci;
		dado2<-azar(cs-ci+1)+ci;
		dadoFinal<-dado1+dado2;
		tiradas[dadoFinal-2]<-tiradas[dadoFinal-2]+1;
		
	Fin Para
	Para i<-0 Hasta 10 Con Paso 1 Hacer
		escribir tiradas[i];
	Fin Para
	
FinAlgoritmo
