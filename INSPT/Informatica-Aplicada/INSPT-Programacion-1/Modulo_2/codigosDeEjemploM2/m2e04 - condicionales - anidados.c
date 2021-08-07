#include <stdio.h>
#include <stdlib.h>

int main()
{
    // declaracion de una variable
    int a=20;

    // condicional anidado
    if (a>0){
        if (a>100){
            if (a>200){
                printf("a es mayor a 200\n");
            }
            else {
                printf("a esta entre 100 y 200\n");
            }
        }
        else {
            printf("a esta entre 0 y 100\n");
        }
    }
    else {
        printf("a es menor a 0\n");
    }
    return 0;
}
