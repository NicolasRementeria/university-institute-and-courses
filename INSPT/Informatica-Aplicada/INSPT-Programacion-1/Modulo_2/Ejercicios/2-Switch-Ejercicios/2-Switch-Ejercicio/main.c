#include <stdio.h>
#include <stdlib.h>

int main()
{

    /*
        Recomendado: Construir un programa que ingrese un carácter y determine si es una vocal.
    */

    char letra;

    printf("Ingrese caracter: ");
    scanf("%c", &letra);
    switch (letra)
    {
    case 'a':
    case 'A':
    case 'e':
    case 'E':
    case 'i':
    case 'I':
    case 'o':
    case 'O':
    case 'u':
    case 'U':
        printf("%c es vocal", letra);
        break;
    default:
        printf("%c es NO vocal", letra);
        break;
    }
    
    printf("\n");
    system("pause");
    
    return 0;
}