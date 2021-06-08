#include <stdio.h>
#include <stdlib.h>

int main()
{

    /*
        Recomendado: Desarrolla un algoritmo que le permita leer un valor entero 
        cualquiera N y escribir si dicho número es par o impar.
    */

    int numero;
    printf("Ingrese un numero: ");
    scanf("%d", &numero);

    if (numero % 2 == 0)
    {
        printf("El numero es par.");
    }
    else
    {
        printf("El numero es impar.");
    }

    return 0;
}