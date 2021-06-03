#include <stdio.h>
#include <stdlib.h>
#define MENOR_A_15(n1, n2) (n1 < 15 && n2 < 15)
#define DIFERENCIA_2(n1, n2) ((n1 >= 15 || n2 >= 15) && (abs(n1 - n2) < 2))

int main(){
    /*
        Recomendado: Describa un algoritmo para realizar el control de la anotación de un encuentro 
        de tenis de mesa. En este juego intervienen 2 jugadores identificados como 1 y 2. A cada uno 
        se le agrega un punto cada vez que realiza una jugada a su favor si es que tiene el servicio 
        a su favor, si no únicamente pasa el servicio a su favor. El juego termina cuando un jugador 
        llega a 15 puntos teniendo por lo menos dos puntos de diferencia con respecto al otro jugador. 
        Al inicio debe ingresar el número 1 o 2 indicando cual jugador comienza con el servicio a su favor, 
        y luego sucesivamente ingrese el resultado de cada jugada (1 o 2). Al terminar debe mostrar un 
        mensaje indicando cuál es el ganador.
    */

    int servicio = 0, punto = 0, puntos_1 = 0, puntos_2 = 0;
    printf("Que jugador saca? 1: Jugador 1 | 2: Jugador 2\n");
    scanf("%d", &servicio);

    while (MENOR_A_15(puntos_1, puntos_2) || DIFERENCIA_2(puntos_1, puntos_2) ){
        printf("La tiene el Jugador %d\n", servicio);
        printf("Quien hizo el punto? 1: Jugador 1 | 2: Jugador 2\n");
        scanf("%d", &punto);
        if (servicio == punto){
            if (servicio == 1){
                puntos_1++;
            }
            else{
                puntos_2++;
            }
        }
        else{
            servicio = punto;
        }
        printf("\nPuntos Jugador 1: %d | Puntos Jugador 2: %d\n", puntos_1, puntos_2);
    }

    printf("\n");
    system("pause");
    
    return 0;
}