#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i=0,j=0;
    int dni,nota,cantNotas=0,acumNotas=0;

    printf("Corte de control, muy importante saberlo\n");
    // ingresamos un dato clave, como el DNI
    printf("Ingrese un DNI:");
    scanf("%d",&dni);
    while (dni>0){
        // mientras el DNI sea valido, procesaremos sus notas
        // primero limpiamos los acumuladores
        acumNotas=0;
        cantNotas=0;
        // ingresamos una nota
        printf("Inicio de procesamiento de DNI %d\n",dni);
        printf("Ingrese nota:");
        scanf("%d",&nota);
        while(nota>0){
            // acumulamos notas
            acumNotas+=nota;
            cantNotas++;
            printf("Ingrese otra nota:");
            scanf("%d",&nota);
        }
        // cuando terminamos de acumular notas, mostramos el resultado del DNI
        printf("El promedio del DNI %d es %2.2f\n",dni,(acumNotas*1.0)/cantNotas);
        // pedimos un DNI nuevo para seguir
        printf("Ingrese otro DNI:");
        scanf("%d",&dni);
    }

    /*
    Para pensar: cómo puedo modificar este codigo para que ademas de
    calcular promedios, al final del programa me muestre el DNI que
    obtuvo el mejor promedio?
    */
    return 0;
}
