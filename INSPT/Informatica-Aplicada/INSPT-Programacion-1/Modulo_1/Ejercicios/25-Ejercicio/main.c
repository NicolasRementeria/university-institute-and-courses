#include <stdio.h>
#include <stdlib.h>
#define CUAD(x) (x * x) /* Definición de macros */
int main()
{
    float a;
    printf("\nEscriba un numero: ");
    scanf("%f", &a);
    printf("\nSu cuadrado es: %.2f\n", CUAD(a));
    system("pause");
    return 0;
}