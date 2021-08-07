// En una empresa de tienda de ropa se carga a fin de dia, una cantidad 
// determinada de facturas de 2 vendedores, 
// determinar cual fue la venta de cada uno, y la comision del 
// 10% sobre cada una de las ventas de ellos

Algoritmo comisiones
	// saber cuantas facturas son
	// tener dos acumuladores para cada vendedor
	// definir de que vendedor es la venta
	// definir el monto de la factura
	Definir facturas Como Entero;
	Definir venta1 Como Entero;
	Definir venta2 Como Entero;
	Definir i Como Entero;
	Definir vendedor Como Entero; //vendedor 1 o vendedor 2
	Definir monto Como Entero;
	
	Escribir "Ingrese cantidad de facturas: ";
	leer facturas;
	venta1 <- 0;
	venta2 <- 0;
	i <- 0;
	
	Mientras i < facturas Hacer
		Repetir
			Escribir "Ingrese el numero de vendedor 1 o 2: ";
			leer vendedor;
		Mientras Que vendedor < 1 o vendedor > 2;
		Escribir "Ingrese monto de la factura: ";
		leer monto;
		si vendedor = 1 Entonces
			venta1 = venta1 + monto;
		SiNo
			venta2 = venta2 + monto;
		FinSi
		i <- i+1;
	FinMientras
	
	Escribir "Total Vendedor 1: ", venta1;
	Escribir "Total Vendedor 2: ", venta2;
	Escribir "Comision Vendedor 1: ", venta1*0.1;
	Escribir "Comision Vendedor 2: ", venta2*0.1;

	
FinAlgoritmo
