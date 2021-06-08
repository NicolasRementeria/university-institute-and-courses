#include <stdio.h>
#include <stdlib.h>

int main(){

    /*
        Recomendado: Dadas las 4 notas obtenidas por un alumno, calcule e informe por pantalla 
        su promedio e informe con una leyenda si está aprobado o no. La condición de aprobación es 
        obtener un promedio mayor o igual que 4.
    */

    float nota1, nota2, nota3, nota4, promedio;

    printf("Ingrese la nota 1: ");
    scanf("%f", &nota1);
    printf("Ingrese la nota 2: ");
    scanf("%f", &nota2);
    printf("Ingrese la nota 3: ");
    scanf("%f", &nota3);
    printf("Ingrese la nota 4: ");
    scanf("%f", &nota4);
    promedio = (nota1 + nota2 + nota3 + nota4) / 4;
    printf("Nota 1: %.2f | Nota 2: %.2f | Nota 3: %.2f | Nota 4: %.2f | Promedio: %.2f \n", nota1, nota2, nota3, nota4, promedio);

    if (promedio >= (float)4)
        printf("APROBADO");
    else
        printf("REPROBADO");

    printf("\n");
    system("pause");

    return 0;
}