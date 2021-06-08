#include <stdio.h>
#include <stdlib.h>
#define AREA(x) (3.14 * x * x) /* Definición de macros */
int main()
{
    /*
        Desarrollar un algoritmo que le permita leer un valor para el radio (R) y calcule el área (A) de un círculo y emitir su valor.
    */

    float a;
    printf("\nEscriba el radio de un circulo: ");
    scanf("%f", &a);
    printf("\nSu area es: %.2f\n", AREA(a));
    system("pause");
    return 0;
}