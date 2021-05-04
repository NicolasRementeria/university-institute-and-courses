#include <stdio.h>
#include <stdlib.h>

int main()
{

    /*
        Recomendado: Construye un programa que ingrese los valores de los lados de un 
        triángulo: a) Valide si las medidas pueden formar un triángulo y b) detecte y 
        muestre un mensaje correspondiente a su tipo (EQUILÁTERO, ISÓSCELES, O ESCALENO);
    */

    int lado1 = 0, lado2 = 0, lado3 = 0;

    printf("Ingrese lado 1 de Triangulo: ");
    scanf("%d", & lado1);
    printf("Ingrese lado 2 de Triangulo: ");
    scanf("%d", & lado2);
    printf("Ingrese lado 3 de Triangulo: ");
    scanf("%d", & lado3);
    

    if ((lado1 != lado2) && (lado1 != lado3) && (lado2 != lado3))
    {
        printf("El triangulo de lados %d, %d, %d, es ESCALENO", lado1, lado2, lado3);
    }
    else if ((lado1 == lado2) && (lado1 == lado3) && (lado2 == lado3))
    {
        printf("El triangulo de lados %d, %d, %d, es EQUILATERO", lado1, lado2, lado3);
    }
    else
    {
        printf("El triangulo de lados %d, %d, %d, es ISOSCELES", lado1, lado2, lado3);
    }
    printf("\n");
    system("pause");
    return 0;
}