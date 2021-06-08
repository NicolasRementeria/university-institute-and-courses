#include <stdio.h>
#include <stdlib.h>
#define CUADRADO(n) (n * n)
#define CUBO(n)     (n * n * n)

int main()
{

    /*
        Recomendado: Escribe un programa que muestre una tabla con los cuadrados y cubos de los números de 1 a 15 y luego presente en pantalla:
        a) La suma de los cuadrados.
        b) La suma de los cubos
        c) Cuántos cubos son mayores a 500
        d) Un mensaje que diga si la suma de los cuadrados fue o no mayor a 2000.
    */
    int cuadrado, cubo, suma_cuadrado = 0, suma_cubo = 0, contador_500;

    for (int n = 1; n <= 15; n++)
    {
        cuadrado = CUADRADO(n);
        cubo = CUBO(n);
        suma_cuadrado += cuadrado;
        suma_cubo += cubo;
        if (cubo > 500)
            contador_500 += 1;
        printf("numero: %d \t| cuadrado: %d \t| cubo: %d\n", n, cuadrado, cubo);
    }

    printf("%d cubos fueron mayores a 500\n", contador_500);

    if (suma_cuadrado > 2000)
    printf("La suma de los cuadrados es mayor a 2000\n", contador_500);
    else
    printf("La suma de los cuadrados es NO mayor a 2000\n", contador_500);
    
    printf("Suma de cuadrados: %d \n", suma_cuadrado);
    printf("Suma de cubos: %d \n", suma_cubo);

    printf("\n");
    system("pause");

    return 0;
}