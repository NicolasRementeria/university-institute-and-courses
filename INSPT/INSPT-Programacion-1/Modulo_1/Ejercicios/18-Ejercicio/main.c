#include <stdio.h>
#include <stdlib.h>

int main(){

    /*
        Construye un programa que pregunte los años que tienes y emita como respuesta el número de días vividos.
    */

    int anios;
    int diasVividos;

    printf("Cuantos anios tenes?: ");
    scanf("%d", &anios);

    diasVividos = anios * 365;

    printf("Con %d anios, viviste %d dias", anios, diasVividos);

    return 0;
}