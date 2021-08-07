#include <stdio.h>
#include <stdlib.h>

int main(){
    /*
    Desarrolla un algoritmo que permita, dados ciertos centímetros como entrada de tipo flotante, 
    emitir por pantalla su equivalencia en pies (enteros) y en pulgadas (flotante, 1 decimal).
    */

    float centimetros;
    float pulgadas;
    int pies;

    printf("Ingrese un valor numerico decimal (centimetros) para calcular su equivalente en pulgadas (decimal) y pies (entero):\n");
    scanf("%f", &centimetros);
    pulgadas = centimetros / 2.54;
    pies = centimetros / 30.48;
    printf("Centimetros: %f | Pulgadas: %.1f | Pies: %d", centimetros, pulgadas, pies);

    // Ej:
    // 1000
    // Centimetros: 1000.000000 | Pulgadas: 393.7 | Pies: 32

    return 0;
}