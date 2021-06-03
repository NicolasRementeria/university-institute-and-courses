#include <stdio.h>
#include <stdlib.h>

int main()
{
    /*
        Recomendado: Construye un programa que solicite la primera letra de los días de la semana y 
        emita por pantalla el nombre completo de ese día. En el caso de los martes y miércoles, 
        pedir la segunda letra para emitir.
    */

    char letra1, letra2;

    printf("Ingrese caracter de la primera letra:\n\t L  = Lunes\n\t M = Martes\n\t M = Miercoles\n\t J  = Jueves\n\t V  = Viernes\n\t S  = Sabado\n\t D  = Domingo\n");
    scanf("%c", &letra1);
    getchar();

    switch (letra1)
    {
    case 'L':
        printf("Lunes");
        break;
    case 'M':
        printf("Ingrese caracter de la segunda letra:\n\t a = Martes\n\t i = Miercoles\n");
        scanf("%c", &letra2);
        printf("\n");
        if (letra2 == 'a')
            printf("Martes");
        else if (letra2 == 'i')
            printf("Miercoles");
        break;
    case 'J':
        printf("Jueves");
        break;
    case 'V':
        printf("Viernes");
        break;
    case 'S':
        printf("Sabado");
        break;
    case 'D':
        printf("Domingo");
        break;

    default:
        break;
    }

    printf("\n");
    system("pause");
    return 0;
}

int main_2()
{

    /*
        Recomendado: Construye un programa que solicite la primera letra de los días de la semana y 
        emita por pantalla el nombre completo de ese día. En el caso de los martes y miércoles, 
        pedir la segunda letra para emitir.
    */
    //char primera_letra, segundaLetra;

    char primera_letra, segunda_letra;

    printf("Ingrese caracter de primera_letra:\n\t L  = Lunes\n\t M = Martes\n\t M = Miercoles\n\t J  = Jueves\n\t V  = Viernes\n\t S  = Sabado\n\t D  = Domingo\n");

    scanf("%d", &primera_letra);
    //getchar();
    printf("\n");

    if (primera_letra == 'L' || primera_letra == 'l')
    {
        printf("L es Lunes");
    }
    if (primera_letra == 'm' || primera_letra == 'M')
    {
        printf("Ingrese caracter de segunda_letra:\n\t a = Martes\n\t i = Miercoles");
        scanf("%c", &segunda_letra);
        if (segunda_letra == 'a' || segunda_letra == 'A')
        {
            printf("Ma es Martes");
        }
        else
        {
            printf("Mi es Miercoles");
        }
    }
    if (primera_letra == 'J' || primera_letra == 'j')
    {
        printf("J es Jueves");
    }
    if (primera_letra == 'V' || primera_letra == "v")
    {
        printf("V es Viernes");
    }
    if (primera_letra == 'S' || primera_letra == 's')
    {
        printf("S es Sabado");
    }
    if (primera_letra == 'D' || primera_letra == 'D')
    {
        printf("D es Domingo");
    }

    printf("\n");
    system("pause");

    return 0;
}