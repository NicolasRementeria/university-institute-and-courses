#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define CALCULAR_SEMIPERIMETRO(lado1, lado2, lado3) ((lado1 + lado2 + lado3) / 2)
#define AREA_TRIANGULO(lado1, lado2, lado3, sp) ( sqrt(sp * (sp - lado1) * (sp - lado2) * (sp - lado3)) )

int main(){

    /*
        Desarrollar un algoritmo que permita calcular el área de un triángulo en función de las longitudes de sus lados previamente leídos desde el teclado.
    */

    /*
        Inspirado por la formula de Heron/Hero: :
            - https://www.programmingsimplified.com/c/source-code/c-program-find-area-of-triangle
            - https://keisan.casio.com/exec/system/1223267646
    */

    float lado1, lado2, lado3, semiperimetro;
    double area;

    printf("Ingrese lado 1 de triangulo: ");
    scanf("%f", &lado1);
    printf("Ingrese lado 2 de triangulo: ");
    scanf("%f", &lado2);
    printf("Ingrese lado 3 de triangulo: ");
    scanf("%f", &lado3);

    semiperimetro = CALCULAR_SEMIPERIMETRO(lado1, lado2, lado3);
    area = AREA_TRIANGULO(lado1, lado2, lado3, semiperimetro);

    printf("L1: %.2f\n", lado1);
    printf("L2: %.2f\n", lado2);
    printf("L3: %.2f\n", lado3);
    printf("Semiperimetro: %.2f\n", semiperimetro);
    printf("Area: %.2f\n", area);

    return 0;
}