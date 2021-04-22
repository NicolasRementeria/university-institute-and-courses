#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define HIPOTENUSA(a, b) (sqrt((a*a) + (b*b))) /* Definición de macros */
int main()
{
    /*
        Determinar la hipotenusa de un triángulo rectángulo conocidas las longitudes de sus dos catetos. Desarrollar los correspondientes algoritmos.
    */

    float cateto1, cateto2;
    printf("\nEscriba el cateto 1 de un triangulo rectangulo: ");
    scanf("%f", &cateto1);
    printf("\nEscriba el cateto 2 de un triangulo rectangulo: ");
    scanf("%f", &cateto2);


    printf("\nSu hipotenuza es: %.2f\n", HIPOTENUSA(cateto1, cateto2));
    system("pause");
    return 0;
}