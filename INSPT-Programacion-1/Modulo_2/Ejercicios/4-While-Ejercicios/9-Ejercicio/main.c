#include <stdio.h>
#include <stdlib.h>

int main()
{

    /*
        Desarrolle un algoritmo que le permita realizar la escritura de los primeros N números Primos. 
        Análisis: En este ejercicio involucra el concepto anterior de número primo y se está adicionando 
        una estructura cíclica que se encargara de contar los N números primos que se desean escribir
    */

    int dato = 1, i = 0, resto = 0, cont = 0, contPrimos = 1, cantPrimos = 0;

    printf("Ingrese un numero para buscar la cantidad de los primeros N primos: ");
    scanf("%d", &cantPrimos);

    while (contPrimos <= cantPrimos)
    {
        cont = 0;
        for (i = 1; i <= dato && cont <= 2; i++)
        {
            resto = dato % i;
            if (resto == 0)
                cont++;
        }
        if (cont == 2)
        {
            contPrimos++;
            printf("El numero %d es primo\n", dato);
            
        }
        dato++;
    }

    printf("\n");
    system("pause");

    return 0;
}