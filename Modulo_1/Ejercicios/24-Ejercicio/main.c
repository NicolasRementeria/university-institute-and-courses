#include <stdio.h>
#include <stdlib.h>

int main(){

    /*
        Construye un programa que permita ingresar 2 tiempos, expresados en horas, minutos y segundos, 
        el mismo debe emitir por pantalla la suma de ambos (también en horas, minutos y segundos).
    */

   int hora1, minuto1, segundo1, segundos_totales1;
   int hora2, minuto2, segundo2, segundos_totales2;
   int resultado_en_segundos, hora_resultado, minuto_resultado, segundos_resultado;


    printf("Ingresar primer horario expresado en horas, minutos y segundos, de la siguiente forma: hh:mm:ss > ");
    scanf("%02d:%02d:%02d", &hora1, &minuto1, &segundo1);
    printf("Ha ingresado: %02d:%02d:%02d", hora1, minuto1, segundo1);

    segundos_totales1 = hora1 * 60 * 60 + minuto1 * 60 + segundo1;

    printf("\nIngresar segundo horario expresado en horas, minutos y segundos, de la siguiente forma: hh:mm:ss > ");
    scanf("%02d:%02d:%02d", &hora2, &minuto2, &segundo2);
    printf("Ha ingresado: %02d:%02d:%02d", hora2, minuto2, segundo2);

    segundos_totales2 = hora2 * 60 * 60 + minuto2 * 60 + segundo2;

    resultado_en_segundos = segundos_totales1 + segundos_totales2;
    segundos_resultado = resultado_en_segundos % 60;
    minuto_resultado = (resultado_en_segundos / 60) % 60;
    hora_resultado = (resultado_en_segundos / 60) / 60;

    printf("\n%02d:%02d:%02d + %02d:%02d:%02d = %02d:%02d:%02d", hora1, minuto1, segundo1, hora2, minuto2, segundo2, hora_resultado, minuto_resultado, segundos_resultado);

    return 0;
}