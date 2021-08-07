#include <stdio.h>
#include <stdlib.h>

int main()
{

    /*
        Se pide hacer un programa para el profesor Jerman que pueda procesar información de sus alumnos. El programa debe:

        - Mostrar un menú de opciones. Las opciones son:
            - Calcular el promedio de notas para el legajo deseado
            - Dadas las notas de un legajo, saber si esta aprobado. La condición de aprobación es que todas las notas sean mayor a 4.
            - Salir del programa
        - El programa se ejecuta hasta que se elija la opción de Salir
    */
    int opcion = 1, cantidad_de_notas = 0;
    float promedio = 0, nota = 0, sumatoria_nota = 0;

    do
    {
        printf("Ingrese opcion: \n\t0- Salir \n\t1-Calcular promedio \n\t2-Esta aprobado? \n\t");
        scanf("%d", &opcion);

        switch (opcion)
        {
            case 0:
                break;
            case 1:
                printf("Estoy calculando el promedio\n");
                printf("Cuantas notas quieres ingresar? ");
                scanf("%d", &cantidad_de_notas);
                for(int i = 0; i < cantidad_de_notas; i++){
                    printf("Ingrese nota: ");
                    scanf("%f", &nota);
                    printf("La nota es: %f\n", nota);
                    sumatoria_nota += nota;
                }
                promedio = sumatoria_nota / cantidad_de_notas;
                printf("El promedio es %.2f\n", promedio);
                break;
            case 2:
                printf("Estoy calculando si aprobo\n");
                if(promedio > 4){
                    printf("Aprobaste!\n");
                } else {
                    printf("Fallaste!\n");
                }
                break;

            default:
                printf("Valor ingresado no valido. Por favor ingrese opcion valida.\n");
        }
    } while (opcion != 0);

    printf("\n");
    system("pause");

    return 0;
}