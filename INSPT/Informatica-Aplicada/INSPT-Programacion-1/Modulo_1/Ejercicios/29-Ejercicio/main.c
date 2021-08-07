#include <stdio.h>
#include <stdlib.h>
#define OBTENER_DIA(fecha) ( ((int)(fecha / 1000000)))
#define OBTENER_MES(fecha) ( (int)((fecha - OBTENER_DIA(fecha) * 1000000) / 10000) )
#define OBTENER_ANIO(fecha) ( fecha - OBTENER_DIA(fecha) * 1000000 - OBTENER_MES(fecha) * 10000)

int main(){

    /*
        Dada una fecha en el formato DDMMAAAA y separarlo en Dia, Mes y Año utilizando operaciones aritméticas.
    */

    int fecha, dia, mes, anio;

    printf("Ingrese una fecha en formato DDMMAAAA (ej: 22042021): ");
    scanf("%d", &fecha);

    dia = OBTENER_DIA(fecha);
    mes = OBTENER_MES(fecha);
    anio = OBTENER_ANIO(fecha);

    printf("El dia %d queda formateado como: %02d:%02d:%02d", fecha, dia, mes, anio);

    return 0;
}