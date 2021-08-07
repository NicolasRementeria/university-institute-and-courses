#include <stdio.h>
#include <stdlib.h>

/*
    6. Una escuela necesita para una prueba de competencias una aplicación que procese notas de alumnos, 
    para obtener información estadística de cada curso/anio. Para ello, la secretaria se reúne con usted y 
    definen lo siguiente: construir un programa que permita procesar 5 anios (1ero. A 5to.). Por cada anio 
    se ingresan una cantidad desconocida de números de legajos de alumnos que finaliza con legajo 0 (cero). 
    Por cada legajo se ingresa:
        a. División a la cual pertenece el alumno (A, B o C), no están ordenados por división
        b. Nota (1 a 10)
    Esta función debe emitir, por cada anio, el promedio de notas por cada división.
    Al finalizar, emitir el total de notas procesadas, el mayor promedio de todos con su anio y división.
*/

int Es_Division_Valida(int division);
char Procesar_Division(int anio, int legajo);
int Es_Nota_Valida(int nota);
void Procesar_Nota(int anio, int legajo, char *division, int *sumatoria_notas_A, int *sumatoria_notas_B, int *sumatoria_notas_C, int *n_notas_A, int *n_notas_B, int *n_notas_C);
void Procesar_Promedio(int anio, int *n_notas_A, int *n_notas_B, int *n_notas_C, int *sumatoria_notas_A, int *sumatoria_notas_B, int *sumatoria_notas_C, float *promedio_nota_A, float *promedio_nota_B, float *promedio_nota_C);
void Procesar_Alumno(int *n_notas_total, int anio, int legajo, int *sumatoria_notas_A, int *sumatoria_notas_B, int *sumatoria_notas_C, int *n_notas_A, int *n_notas_B, int *n_notas_C, char *division);
void Calcular_Mayor_Promedio(int anio, int *anio_mayor_promedio, char division, char *division_mayor_promedio, float promedio_nota_A, float promedio_nota_B, float promedio_nota_C, float *mayor_promedio);
void Reinicializar_Variables(int *n_notas_A, int *n_notas_B, int *n_notas_C, int *sumatoria_notas_A, int *sumatoria_notas_B, int *sumatoria_notas_C, float *promedio_nota_A, float *promedio_nota_B, float *promedio_nota_C);

int main()
{
    int anio = 1, legajo, n_notas_total = 0, n_notas_A = 0, n_notas_B = 0, n_notas_C = 0, sumatoria_notas_A = 0, sumatoria_notas_B = 0, sumatoria_notas_C = 0;
    char division;
    float promedio_nota_A = 0, promedio_nota_B = 0, promedio_nota_C = 0;
    float mayor_promedio = 0;
    int anio_mayor_promedio = 0;
    char division_mayor_promedio = 0;

    for (anio = 1; anio <= 5; anio++)
    {
        printf("anio %d | Ingrese legajo (0 para finalizar): ", anio);
        scanf("%d", &legajo);
        while (legajo != 0)
        {
            Procesar_Alumno(&n_notas_total, anio, legajo, &sumatoria_notas_A, &sumatoria_notas_B, &sumatoria_notas_C, &n_notas_A, &n_notas_B, &n_notas_C, &division);
            printf("anio %d | Ingrese legajo (0 para finalizar): ", anio);
            scanf("%d", &legajo);
        }

        Procesar_Promedio(anio, &n_notas_A, &n_notas_B, &n_notas_C, &sumatoria_notas_A, &sumatoria_notas_B, &sumatoria_notas_C, &promedio_nota_A, &promedio_nota_B, &promedio_nota_C);

        printf("Promedio Division A Anio %d: %f\n", anio, promedio_nota_A);
        printf("Promedio Division B Anio %d: %f\n", anio, promedio_nota_B);
        printf("Promedio Division C Anio %d: %f\n", anio, promedio_nota_C);

        Calcular_Mayor_Promedio(anio, &anio_mayor_promedio, division, &division_mayor_promedio, promedio_nota_A, promedio_nota_B, promedio_nota_C, &mayor_promedio);

        Reinicializar_Variables(&n_notas_A, &n_notas_B, &n_notas_C, &sumatoria_notas_A, &sumatoria_notas_B, &sumatoria_notas_C, &promedio_nota_A, &promedio_nota_B, &promedio_nota_C);
    }
    
    printf("Total de notas procesadas: %d\n", n_notas_total);
    printf("Promedio mayor: Anio %d | Division: %c | Promedio: %f\n", anio_mayor_promedio, division_mayor_promedio, mayor_promedio);

    printf("\n");
    system("pause");

    return 0;
}

int Es_Division_Valida(int division)
{
    if (division == 'a' || division == 'A' || division == 'b' || division == 'B' || division == 'c' || division == 'C')
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

char Procesar_Division(int anio, int legajo)
{
    char division = 0;
    while (!Es_Division_Valida(division))
    {
        printf("anio %d | Legajo %d | Ingrese Division (A/B/C) (0 para finalizar): ", anio, legajo);
        fflush(stdin);
        scanf("%c", &division);
    }
    return division;
}

int Es_Nota_Valida(int nota)
{
    if (nota >= 1 && nota <= 10)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

void Procesar_Nota(int anio, int legajo, char *division, int *sumatoria_notas_A, int *sumatoria_notas_B, int *sumatoria_notas_C, int *n_notas_A, int *n_notas_B, int *n_notas_C)
{
    int nota = 0;
    while (!Es_Nota_Valida(nota))
    {
        printf("anio %d | Legajo %d | Division %c | Ingrese Nota (entre 1 y 10): ", anio, legajo, *division);
        scanf("%d", &nota);
    }
    if (*division == 'a' || *division == 'A')
    {
        (*n_notas_A)++;
        *sumatoria_notas_A += nota;
    }
    if (*division == 'b' || *division == 'B')
    {
        (*n_notas_B)++;
        *sumatoria_notas_B += nota;
    }
    if (*division == 'c' || *division == 'C')
    {
        (*n_notas_C)++;
        *sumatoria_notas_C += nota;
    }
}

void Procesar_Promedio(int anio, int *n_notas_A, int *n_notas_B, int *n_notas_C, int *sumatoria_notas_A, int *sumatoria_notas_B, int *sumatoria_notas_C, float *promedio_nota_A, float *promedio_nota_B, float *promedio_nota_C)
{
    if (*n_notas_A != 0)
    {
        *promedio_nota_A = *sumatoria_notas_A / (float)*n_notas_A;
    }

    if (*n_notas_B != 0)
    {
        *promedio_nota_B = *sumatoria_notas_B / (float)*n_notas_B;
    }
    if (*n_notas_C != 0)
    {
        *promedio_nota_C = *sumatoria_notas_C / (float)*n_notas_C;
    }
}

void Procesar_Alumno(int *n_notas_total, int anio, int legajo, int *sumatoria_notas_A, int *sumatoria_notas_B, int *sumatoria_notas_C, int *n_notas_A, int *n_notas_B, int *n_notas_C, char *division)
{
    (*n_notas_total)++;
    *division = Procesar_Division(anio, legajo);
    Procesar_Nota(anio, legajo, division, sumatoria_notas_A, sumatoria_notas_B, sumatoria_notas_C, n_notas_A, n_notas_B, n_notas_C);
}

void Calcular_Mayor_Promedio(int anio, int *anio_mayor_promedio, char division, char *division_mayor_promedio, float promedio_nota_A, float promedio_nota_B, float promedio_nota_C, float *mayor_promedio)
{
    if (promedio_nota_A > *mayor_promedio)
    {
        *anio_mayor_promedio = anio;
        *division_mayor_promedio = division;
        *mayor_promedio = promedio_nota_A;
    }
    if (promedio_nota_B > *mayor_promedio)
    {
        *anio_mayor_promedio = anio;
        *division_mayor_promedio = division;
        *mayor_promedio = promedio_nota_B;
    }
    if (promedio_nota_C > *mayor_promedio)
    {
        *anio_mayor_promedio = anio;
        *division_mayor_promedio = division;
        *mayor_promedio = promedio_nota_C;
    }
}

void Reinicializar_Variables(int *n_notas_A, int *n_notas_B, int *n_notas_C, int *sumatoria_notas_A, int *sumatoria_notas_B, int *sumatoria_notas_C, float *promedio_nota_A, float *promedio_nota_B, float *promedio_nota_C){
        *n_notas_A = 0;
        *n_notas_B = 0;
        *n_notas_C = 0;
        *sumatoria_notas_A = 0;
        *sumatoria_notas_B = 0;
        *sumatoria_notas_C = 0;
        *promedio_nota_A = 0;
        *promedio_nota_B = 0;
        *promedio_nota_C = 0;
}