#include <stdio.h>
#include <stdlib.h>

int main()
{
    int valor,i=0;

    printf("Ingrese un valor:");
    scanf("%d",&valor);
    fflush(stdin);
    printf("\nEjecutando el while\n");

    // CICLO WHILE - EJEMPLO ESTANDAR
    while (i<valor){
        printf("%d|",i);
        i++;
        getchar(); // pausa de cada interacion
    }
    printf("\n");
    system("PAUSE");

    // CICLO WHILE - EJEMPLO SIN LLAVES
    printf("\nAhora los mismo pero mas simplificado!\n");
    i=0; // volvemos la variable i, que es nuestro contador, a cero
    while (i<valor)
        printf("%d|",i++); // de esta forma, el ++ se ejecuta despues de ejecutar el printf (es post incremento)
    printf("\n");
    system("PAUSE");

    // CICLO WHILE - EJEMPLO CON UN IF
    printf("\nCiclo con un if!\n");
    i=0;
    while (i<valor){
        printf("%d\t",i);
        if (i%2==0) {
            printf("es par!\n");
        } else {
            printf("es IMpar!\n");
        }
        i++;
        //getchar(); // descomentar esta linea para ejecutar ciclo por ciclo
    }
    printf("\n");
    system("PAUSE");

    // CICLO WHILE - EJEMPLO DE CODIGO INALCANZABLE
    printf("\nAhora un ciclo con codigo inalcanzable!\n");
    i=5;
    while(i<4){
        printf("Codigo inalcanzable!\n");
        i++;
    }
    printf("Acabamos de saltear un ciclo while completo\n");
    system("PAUSE");


    // CICLO WHILE - EJEMPLO DE CICLO INFINITO
    printf("\nFinalmente ciclo infinito!\n");
    i=5;
    while (i>4){
        printf("Ciclo infinito!!!");
        i++;
        // ups, le pifie a la condicion
        // estos son los PEORES errores, porque no se ven a simple vista en el codigo
    }
    return 0;
}
