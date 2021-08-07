#include <stdio.h>
#include <stdlib.h>

/*
    Se ingresan los siguientes datos del personal de una fábrica: legajo (valores validos entre 1200 y 4000), 
    edad y genero (F/M/O). Se ingresa por cada empleado un número de sueldos correspondiente a tres sectores 
    donde realizan tareas distintas. Alguno de ellos puede ser cero, lo que significa que no realizan tareas 
    en ese sector. El número de empleados no se conoce. El ingreso de datos finaliza con legajo -1. A partir 
    de estos datos, se pide informar por pantalla:
        a. Cantidad de empleados
        b. Porcentaje de personal ‘F’ y ‘M’
        c. Promedio de edad de los empleados
        d. El número de legajo del empleado de sexo masculino de mayor edad.
*/

int Es_Valido_Legajo(int legajo);
int Ingresar_Legajo();
int Es_Valido_Edad(int edad);
int Ingresar_Edad(int *sumatoria_edad);
int Es_Valido_Genero(char genero);
char Ingresar_Genero(int *numero_hombres, int *numero_mujeres);

int main()
{

    int legajo, edad;
    int cantidad_de_empleados = 0, sumatoria_edad = 0, numero_hombres = 0, numero_mujeres = 0, max_legajo_hombre_mayor = 0, edad_hombre_mayor = 0;
    float promedio_edad = 0, porcentaje_femenino = 0, porcentaje_masculino = 0;
    char genero;

    legajo = Ingresar_Legajo();

    while (legajo != -1)
    {
        cantidad_de_empleados++;
        edad = Ingresar_Edad(&sumatoria_edad);
        genero = Ingresar_Genero(&numero_hombres, &numero_mujeres);

        // ****************
        // Falta ingreso de sueldos a 3 sectores, que no se usa para calcular
        // ****************

        if((genero == 'm' || genero == 'M') && (edad > edad_hombre_mayor)){
            edad_hombre_mayor = edad;
            max_legajo_hombre_mayor = legajo;
        }

        legajo = Ingresar_Legajo();
    }
    if(cantidad_de_empleados > 0){
        promedio_edad = sumatoria_edad / (float)cantidad_de_empleados;
        porcentaje_femenino = (numero_mujeres / (float)cantidad_de_empleados) * 100;
        porcentaje_masculino = (numero_hombres / (float)cantidad_de_empleados) * 100;
    }


    printf("Cantidad Empleados = %d | Porcentaje Femenino: %f | Porcentaje Masculino: %f | Promedio edad: %f | Legajo del hombre de mayor edad: %d \n", cantidad_de_empleados, porcentaje_femenino, porcentaje_masculino, promedio_edad, max_legajo_hombre_mayor);

    printf("\n");
    system("pause");

    return 0;
}

int Es_Valido_Legajo(int legajo)
{
    if ((legajo >= 1200 && legajo <= 4000) || legajo == -1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int Ingresar_Legajo()
{
    int legajo = 0;
    while (Es_Valido_Legajo(legajo) != 1)
    {
        printf("Ingrese Legajo (Entre 1200 y 4000, -1 para salir de sesion): ");
        scanf("%d", &legajo);
    }
    return legajo;
}

int Es_Valido_Edad(int edad)
{
    if (edad >= 1 && edad <= 130)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int Ingresar_Edad(int *sumatoria_edad)
{
    int edad = 0;
    while (Es_Valido_Edad(edad) != 1)
    {
        printf("Ingrese Edad (Entre 1 y 130): ");
        scanf("%d", &edad);
    }
    (*sumatoria_edad) += edad;
    return edad;
}

int Es_Valido_Genero(char genero)
{
    if (genero == 'm' || genero == 'M' || genero == 'f' || genero == 'F' || genero == 'o' || genero == 'O')
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

char Ingresar_Genero(int *numero_hombres, int *numero_mujeres)
{
    char genero = 0;
    while (Es_Valido_Genero(genero) != 1)
    {
        printf("Ingrese genero (F/M/O): ");
        fflush(stdin);
        scanf("%c", &genero);
    }
    if (genero == 'm' || genero == 'M')
        (*numero_hombres)++;
    if (genero == 'f' || genero == 'F')
        (*numero_mujeres)++;
    return genero;
}