#include <stdio.h>
#include <stdlib.h>

int main(){

    /*
        Recomendado: Desarrolla un algoritmo que le permita leer tres valores enteros e indique
        cuál es el mayor.
    */

    int valor1, valor2, valor3;

    printf("Ingrese valor 1: ");
    scanf("%d", &valor1);
    printf("Ingrese valor 2: ");
    scanf("%d", &valor2);
    printf("Ingrese valor 3: ");
    scanf("%d", &valor3);

    if(valor1 > valor2 && valor1 > valor3)
        printf("%d es el numero mayor (valor1 = %d, valor2 = %d, valor3 = %d)", valor1, valor1, valor2, valor3);    
    else if(valor2 > valor3)
        printf("%d es el numero mayor (valor1 = %d, valor2 = %d, valor3 = %d)", valor2, valor1, valor2, valor3);  
    else
        printf("%d es el numero mayor (valor1 = %d, valor2 = %d, valor3 = %d)", valor3, valor1, valor2, valor3);  

    return 0;
}