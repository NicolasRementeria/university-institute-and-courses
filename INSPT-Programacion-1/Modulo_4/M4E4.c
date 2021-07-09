#include <stdio.h>
#define DIM 10

void imprimirBarra(int c){
    int i;

    for(i=0;i<c;i++){
        printf("*");
    }
    printf("\n");
}

void imprimirHistograma(int temp[], int tam){
    int i;
    for (i=0;i<tam;i++){
        printf("Temp #%d: ",i+1);
        imprimirBarra(temp[i]);
    }
}

/*
Desarrollar una funcion que reciba 3 vectores, de los cuales:
- los primeros 2 tienen datos
- el tercero tiene la concatenacion de los dos anteriores

*/
void concatenarVectores(char vec1[], int tam1, char vec2[], int tam2, char resultado[], int tam3){
    int i;

    if(tam1+tam2>tam3){
        printf("*** ERROR: tamanio insuficiente ***\n");
    } else {
        for (i=0;i<tam1;i++){
            resultado[i]=vec1[i];
        }
        for (i;i<(tam2+tam1);i++){
            resultado[i]=vec2[i-tam1];
        }
    }
}

/*
Hacer una funcion que reciba vec1 y vec2 asi:
VEC1: A C F
VEC2: A B H Z

y cargue en vec3 sus datos tal que asi:
VEC3: A A B C F H Z

NO SABEN ORDENAR, ARREGLENSELAS CON LO QUE SABEN HASTA AHORA
*/

int main (void){
    int temperaturas[10]={22,24,25,33,35,32,29,25,10,11},i;
    char vec1[3]={'u','t','n'};
    char vec2[4]={'C','A','S','A'};
    char vec3[8]={'-','-','-','-','-','-','-','-'};

    concatenarVectores(vec1,3,vec2,4,vec3,8);

    for(i=0;i<8;i++)
        printf("%c",vec3[i]);
    printf("\n");
    //imprimirHistograma(temperaturas, DIM);
    return 0;
}
