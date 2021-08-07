#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
    /*
        Construye un programa que permita ingresar la superficie de un cuadrado (en m2), el mismo debe emitir por pantalla su perímetro.
    */

    float superficie, lado, perimetro;

    printf("Ingrese la superficie de un cuadrado en metros cuadrados: ");
    scanf("%f", &superficie);

    lado = sqrt(superficie);
    perimetro = 4*lado;

    printf("Para un cuadrado de area %.1f metros cuadrados, cada lado mide %.3f metros, y su perimetro es de %.3f metros", superficie, lado, perimetro);

    return 0;
}