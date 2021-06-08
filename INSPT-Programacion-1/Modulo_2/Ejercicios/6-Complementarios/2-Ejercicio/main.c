#include <stdio.h>
#include <stdlib.h>

int main()
{

    /*
        Recomendado: Repita la lectura de un número entero hasta que sea positivo, entonces, 
        determine cuantas cifras tiene. El método que debe usar es contar cuantas veces es divisible para 10.
    */

    int numero, divisible = 0;

    do
    {
        printf("Ingrese numero positivo: ");
        scanf("%d", &numero);
    } while (numero < 0);

    while (numero >= 10){
        numero /= 10;
        divisible++;
    }

    printf("La cantidad de divisiones por 10 del numero es %d\n", divisible);
    printf("Por lo tanto tiene %d cifras.", divisible+1);

    printf("\n");
    system("pause");

    return 0;
}