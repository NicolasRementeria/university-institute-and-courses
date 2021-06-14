// raices de una ecuacion de segundo grado
// x2 -x +6
// x1 y x2
// -b +- (raiz(b2-4ac) / 2*a)
// discriminante = b2 -4ac
// si discriminante < 0 no tiene solucion en los reales
// si discrimiante > 0, x1 y x2 son soluciones distintas
// si discriminante == 0, x1 y x2 son iguales

Algoritmo raices
	Definir a, b, c Como Real;
	Definir x1, x2 como Real;
	Definir discriminante como Real;
	
	Repetir
		Escribir "Ingrese el coeficiente A";
		leer a;
	Mientras Que a = 0;
	
	Escribir "Ingrese el coeficiente B";
	leer b;	
	Escribir "Ingrese el coeficiente C";
	leer c;	
	
	discriminante <- b^2 - 4 * a * c;
	
	si discriminante < 0 Entonces
		Escribir "La ecuacion no tiene solucion en los reales";
	SiNo
		x1 <- (-b + rc(discriminante)) / (2*a);
		x2 <- (-b - rc(discriminante)) / (2*a);
		si discriminante > 0 Entonces
			Escribir  "La raiz x1: ", x1;
			Escribir  "La raiz x2: ", x2;
		SiNo
			Escribir "La raiz x1 y x2 son iguales en : ", x1;
		FinSi
	FinSi
	
FinAlgoritmo
