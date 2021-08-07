Algoritmo vectores
	//Dadas 25 edades entre 1 y 90 años cargarlas en un vector Vec, calcular y mostrar
	//Punto 1) El promedio de edad.
	//Punto 2) Cantidad de edades mayor a los 18
	//Punto 3) Todas las edades mayores al promedio de edad
	//Punto 4) Porcentaje de menores a 18 y mayores a 18
	//Punto 5) Ese porcentaje verlo de una manera o especie grafica
	
	definir edades Como Entero;
	definir promedio Como Real;
	definir cantMay18 Como Entero;
	definir edadMayorPromedio Como Entero;
	definir i, s Como Entero;
	Dimension edades[25];
	s <- 0;
	edadMayorPromedio <- 0;
	
	Para i<-0 Hasta 24 Con Paso 1 Hacer
		//(cota superior - cota inferior + 1) + cota inferior
		//(cs-ci+1)+ci
		edades[i] <- azar(90-1+1)+1;
		s <- s + edades[i];
		Si edades[i] > 18
			cantMay18 <- cantMay18 +1;
		FinSi
	FinPara
	
	promedio <- s / 25;
	
	Mostrar "Edades Cargadas en el Vector";
	Para i<-0 Hasta 24 Con Paso 1 Hacer
		Mostrar edades[i], " " Sin Saltar;
		Si ((i+1) mod 5 == 0) Entonces
			Mostrar "";
		FinSi
		
	FinPara
	
	Mostrar "";
	Mostrar "El promedio de edad es: ", promedio;
	
	Para i<-0 Hasta 24 Con Paso 1 Hacer
		Si edades[i] > promedio Entonces
			edadMayorPromedio <- edadMayorPromedio + 1;
			Mostrar edades[i];
		FinSi
	FinPara
	Mostrar "Cantidades de edades mayor al promedio:", edadMayorPromedio;
	Mostrar "Porcentaje de mayores a 18 años:", cantMay18*100/25, "%";
	Mostrar "Porcentaje de menores a 18 años:", (25-cantMay18)*100/25, "%";
	
	Para i<-0 Hasta trunc(cantMay18*100/25) Con Paso 1 Hacer
		Mostrar "|" Sin Saltar;
	FinPara
	Mostrar "";
	Para i<-0 Hasta trunc((25-cantMay18)*100/25) Con Paso 1 Hacer
		Mostrar "|" Sin Saltar;
	FinPara
	Mostrar "";
	
FinAlgoritmo
