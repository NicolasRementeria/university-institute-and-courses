#include <stdio.h>
#include <stdlib.h>

int main()
{

    /*
        Recomendado: Desarrolla un algoritmo que le permita leer un valor cualquiera N y escribir
        en la pantalla si dicho número es Positivo, Negativo o 0 (cero).
    */

    int numero;

    printf("Ingrese numero: ");
    scanf("%d", &numero);

    if (numero > 0)
    {
        printf("El numero es positivo");
    }
    else if (numero < 0)
    {
        printf("El numero es negativo");
    }
    else
        printf("El numero es 0");

    return 0;
}