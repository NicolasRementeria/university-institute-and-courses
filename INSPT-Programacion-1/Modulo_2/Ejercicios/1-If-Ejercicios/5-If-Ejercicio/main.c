#include <stdio.h>
#include <stdlib.h>

int main(){

    /*
        Recomendado: Desarrolla un algoritmo que le permita leer dos valores A y B e indicar si la
        suma de los dos números es par.
    */

    int valor1=0, valor2=0, resultado=0;

    printf("Ingrese valor 1: ");
    scanf("%d", &valor1);
    printf("Ingrese valor 2: ");
    scanf("%d", &valor2);

    resultado = valor1 + valor2;
    
    if(resultado%2 == 0 )
        printf("El resultado %d es par", resultado);
    else
        printf("El resultado %d es impar", resultado);
    return 0;
}