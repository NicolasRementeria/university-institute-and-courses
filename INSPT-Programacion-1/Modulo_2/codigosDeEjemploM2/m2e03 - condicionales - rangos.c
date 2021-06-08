#include <stdio.h>
#include <stdlib.h>

int main()
{
    // declaracion de una variable
    int a=20;

    // condicional evaluando rangos...
    printf("Evaluando el valor de a segun rangos...\n");
    if (a>0 && a<100){
        printf("valor entre 0 y 100\n");
    }
    if (a>100 && a<200){
        printf("valor entre 100 y 200\n");
    }
    if (a>200 && a<300){
        printf("valor entre 200 y 300\n");
    }

    return 0;
}
