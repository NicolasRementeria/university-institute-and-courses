/*
En este codigo fuente se muestra cómo se trabaja con vectores
*/

#include <stdio.h>
#define DIM 20

void cargar(int* vec, int lim){
    int i=0;
    for (i=0; i<lim; i++){
        printf("Ingrese dato para la posicion #%d:",i+1);
        fflush(stdin);
        scanf("%c",&vec[i]);
    }
}

int cantidadHastaMarca(int* vec, int tam){
    int marca,i=0;

    printf("valor a buscar?\n");
    scanf("%d",&marca);

    while (vec[i]!=marca && i<tam){
        i++;
    }
    if (i==tam)
        return -1;
    else
        return i;
}

int main(){
    int vector[DIM]={11,22,33,44,55,66,77,88,99},limite,i;

    printf("cuantos elementos queres ingresar (max %d)?\n",DIM);
    scanf("%d",&limite);
    cargar(vector,limite);

    for (i=0; i<DIM; i++){
        printf("%c|",vector[i]);
    }
    printf("\n");

    i=cantidadHastaMarca(vector, DIM);
    printf("Cantidad hasta la marca: %d\n",i);

    return 0;
    }
