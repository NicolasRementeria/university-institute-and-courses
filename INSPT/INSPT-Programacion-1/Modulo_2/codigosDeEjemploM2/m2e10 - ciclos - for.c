#include <stdio.h>
#include <stdlib.h>

int main()
{
    int valor=5,i=4;

    // ********* CICLO FOR *********
    printf("Ciclo FOR estandar:\n");
    for( i=0 ; i<5 ; i++ ) {
        printf("%d|",i);
    }
    printf("\n");
    system("PAUSE");


    printf("\nSi hay una instruccion, se pueden omitir las llaves\n");
    for( i=0 ; i<5 ; i++ )
        printf("%d|",i);
    printf("\n");
    // no importa como quedo el contador i anteriormente,
    // el for lo inicia en 0 antes de empezar :)
    system("PAUSE");


    printf("\nPuedo hacer un uso avanzado del for, que no es recomendable\n");
    // esto es posible porque los parametros del  ciclo son instrucciones en si mismas
    i=0 ;
    for( ; i<valor ; ){
        printf("%d|",i);
        i++;
    }
    printf("\n");
    // por favor NO UTILIZAR el ciclo FOR de esta forma!!!
    system("PAUSE");

    printf("Un ciclo for sin parametros! O sea, ciclo infinito\n");
    i=0;
    for( ; ; ){
        printf("%d|",i++);
    }
    printf("\n");

    return 0;
}
