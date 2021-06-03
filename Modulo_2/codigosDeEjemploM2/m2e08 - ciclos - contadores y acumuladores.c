#include <stdio.h>
#include <stdlib.h>

int main()
{
    // CONTADORES y ACUMULADORES
    int contador=0, acumulador=0, valor=1;

    while (valor!=0){
        printf("Ingrese un valor (ingrese 0 para terminar):");
        scanf("%d",&valor);
        //acumulador=acumulador+valor;
        acumulador+=valor;
        contador++;
    }
    printf("Se ingresaron %d valores\n",contador);
    printf("El promedio es %f", acumulador/(float)contador);

    // que pasa si ingreso un 0 como primer valor??? anda bien???
    return 0;
}
