#include <stdio.h>
#include <stdlib.h>

int main()
{
    int valor=5,i=0;

    // DO-WHILE - EJEMPLO ESTANDAR
    printf("Ciclo do-while estandar:\n");
    do {
        printf("%d|",i);
        i++;
    } while (i<valor);


    // DO-WHILE - EJEMPLO DE CONDICION FALSE
    printf("\n\nCiclo con la condicion falsa desde el principio\n");
    i=5;
    valor=4;
    do {
        printf("%d|",i);
    } while (i<valor); // el bloque ejecuta al menos una vez!

    // si la condicion es verdadera siempre, tambien es un ciclo infinito

    system("PAUSE");
    return 0;
}
