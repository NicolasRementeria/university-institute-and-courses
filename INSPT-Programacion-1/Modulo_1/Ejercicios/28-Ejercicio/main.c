#include <stdio.h>
#include <stdlib.h>
#define OBTENER_SEGUNDOS(seg_totales) ( seg_totales % 60 )
#define OBTENER_MINUTOS(seg_totales) ( ( seg_totales / 60) % 60 )
#define OBTENER_HORAS(seg_totales) ( ( seg_totales / 60) / 60 )

int main(){

    /*
        Dada una cantidad entera de segundos (menor a 86400) y conviértela en horas, minutos y segundo utilizando los operadores de cociente y resto enteros.
    */
    
    int segundos_totales, hora, min, seg;
    printf("Ingrese los segundos totales (no mayor a 86400 segundos) para convertirlo a formato hh:mm:ss: ");
    scanf("%d", &segundos_totales);

    hora = OBTENER_HORAS(segundos_totales);
    min = OBTENER_MINUTOS(segundos_totales);
    seg = OBTENER_SEGUNDOS(segundos_totales);

    printf("Segundos totales: %d | Horario convertido: %02d:%02d:%02d", segundos_totales, hora, min, seg);

    

    return 0;
}