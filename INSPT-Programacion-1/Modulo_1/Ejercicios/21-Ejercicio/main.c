#include <stdio.h>
#include <stdlib.h>

int main()
{
    /*
       Construye un programa que permita ingresar las medidas de los lados de un rectángulo; el mismo debe emitir por pantalla su superficie y su perímetro.
    */

    float lado1, lado2, perimetro, superficie;

    printf("Ingrese las medidas del lado 1: ");
    scanf("%f", &lado1);
    printf("Ingrese las medidas del lado 2: ");
    scanf("%f", &lado2);

    perimetro = 2 * lado1 + 2 * lado2;
    superficie = lado1 * lado2;

    printf("Un rectangulo de lados %.1f y %.1f forman un perimetro de %.1f y una superficie de %.1f", lado1, lado2, perimetro, superficie);

    return 0;
}