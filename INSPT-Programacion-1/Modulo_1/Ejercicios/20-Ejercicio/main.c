#include <stdio.h>
#include <stdlib.h>

int main(){

    /*
    	Construye un programa que permita ingresar las medidas de los lados de un rectángulo; el mismo debe emitir por pantalla su superficie y su perímetro.
    */

    float angulo1, angulo2, angulo3;
    
    printf("Ingrese primer angulo interior: ");
    scanf("%f", &angulo1);

    printf("Ingrese segundo angulo interior: ");
    scanf("%f", &angulo2);

    angulo3 = 180 - angulo1 - angulo2;

    printf("Los angulos del triangulo son: %.1f, %.1f, %.1f", angulo1, angulo2, angulo3);

    return 0;
}
