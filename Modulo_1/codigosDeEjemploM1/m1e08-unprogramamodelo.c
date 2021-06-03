#include <stdio.h>
#include <stdlib.h>

int main()
{
	// ingreso de datos
    int miVariable = 0;
    int unResultado = 0;
    printf("Ingrese un valor entero: ");
    scanf("%d", &miVariable);

	// procesamiento de datos
    miVariable++;
    printf("Incremento en uno: %d\n",miVariable);
    miVariable--;
    unResultado= miVariable*miVariable;

	// emision de resultados
	printf("el cuadrado de %d es %d\n", miVariable,unResultado);
    return 0;
}
