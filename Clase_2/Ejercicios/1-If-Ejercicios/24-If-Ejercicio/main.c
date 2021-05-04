#include <stdio.h>
#include <stdlib.h>

int main(){

    /*
        Recomendado: Desarrolla un algoritmo que le permita leer tres valores A, B y C 
        e indicar si la suma de dos de ellos cualquiera es igual al tercero.
    */

    int A, B, C, resultado;

    printf("Ingrese valor A: ");
    scanf("%d", &A);
    printf("Ingrese valor B: ");
    scanf("%d", &B);
    printf("Ingrese valor C: ");
    scanf("%d", &C);

    if ((A + B) == C){
        printf("A=%d | B=%d | C=%d | A+B=C", A, B, C);
    }
    else if((A + C) == B){
        printf("A=%d | B=%d | C=%d | A+C=B", A, B, C);
    }
    else if((B + C) == A){
        printf("A=%d | B=%d | C=%d | B+C=A", A, B, C);
    }
    else{
        printf("A=%d | B=%d | C=%d | Ninguna eleccion de dos valores sumados da el tercer valor como resultado", A, B, C);
    }

    printf("\n");
    system("pause");

    return 0;
}