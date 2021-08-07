#include <stdio.h>
#include <stdlib.h>

int main()
{

    /*
        Recomendado: Escribir un programa para evaluar la función y = 4 * x^2 - 16 * x + 15, 
        en donde x toma los valores de 1 a 2 en pasos de 0,1. Para cada x la salida 
        debe dar el valor de y junto con el mensaje POSITIVO o NO POSITIVO en formato de tabla.
    */

    float x, y;

    for (x = 1.0; x <= 2.1; x = x + 0.1)
    {
            printf("----------\n");
            y = 4 * x * x - 16 * x + 15;

            if (y >= 0)
                printf("y = 4 * %.1f^2 -16 * %.1f +15 \t | %.1f \t | POSITIVO\n", x, x, y);
            else
                printf("y = 4 * %.1f^2 -16 * %.1f +15 \t | %.1f \t | NEGATIVO\n", x, x, y);

    }
    printf("----------\n");

    printf("\n");
    system("pause");

    return 0;
}

