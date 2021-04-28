#include <stdio.h>
#include <stdlib.h>

int main()
{
    int opcion;

    printf("Segunda chance, ingresa otra opcion:");
    scanf("%d",&opcion);
    switch (opcion){
        case 0:
        case 1: // si la misma accion va para varios casos
        case 2: // no hagas copy/paste de codigo, simplificalo asi!
        case 3:
        case 4:
        case 5:
            printf("Elegiste la opcion %d, perdiste!\n",opcion);
            break;
        case 6:
            printf("Bueno, ahora si ganaste\n");
            break;
        default: // si ningun caso es valido, se ejecuta la el caso por DEFECTO, que puede o no estar
            printf("opcion invalida, no tengo tanas opciones disponibles!");
            break;
    }
    return 0;
}
