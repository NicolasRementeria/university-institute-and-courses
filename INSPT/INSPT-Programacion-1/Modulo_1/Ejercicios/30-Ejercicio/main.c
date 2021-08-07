#include <stdio.h>
#include <stdlib.h>
#define CELCIUS_A_FAHRENHEIT(celcius) ((celcius * 9/5) + 32)

int main(){

    /*
        Desarrollar un algoritmo que permita leer un valor que represente una temperatura expresada 
        en grados Celsius y convierta dicho valor en un valor expresado en grados Fahrenheit.
    */

   float celcius, fahrenheit;

   printf("Ingresar temperatura en Celcius: ");
   scanf("%f", &celcius);

    fahrenheit = CELCIUS_A_FAHRENHEIT(celcius);

    printf("%.2f Celcius == %.2f grados Fahrenheit", celcius, fahrenheit);
    
    return 0;
}