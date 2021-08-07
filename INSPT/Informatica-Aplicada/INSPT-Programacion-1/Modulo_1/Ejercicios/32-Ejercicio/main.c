#include <stdio.h>
#include <stdlib.h>
#define AREA_CILINTRO(radio, altura) (2 * 3.14 * radio * altura + 2 * 3.14 * radio * radio)
#define VOLUMEN_CILINDRO(radio, altura) (3.14 * radio * radio * altura)

int main()
{

    /*
        Desarrollar un algoritmo que permita determinar el área y volumen de un cilindro cuyo radio (r) y altura (h) se leen desde teclado.
    */

    float radio, altura, area, volumen;

    printf("Ingrese radio de cilindro: ");
    scanf("%f", &radio);
    printf("Ingrese altura de cilindro: ");
    scanf("%f", &altura);

    area = AREA_CILINTRO(radio, altura);
    volumen = VOLUMEN_CILINDRO(radio, altura);

    printf("Cilindro | Radio: %.2f, Altura: %.2f, Area: %.2f, Volumen: %.2f", radio, altura, area, volumen);

    return 0;
}