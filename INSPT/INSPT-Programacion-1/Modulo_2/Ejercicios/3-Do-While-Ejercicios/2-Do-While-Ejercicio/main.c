#include <stdio.h>
#include <stdlib.h>

int main()
{

    /*
        Recomendado: ¿Qué mostrará en pantalla el siguiente fragmento?
        m=5;
        n=9;
        do
        {
        printf("%d %d \n",m,n);
        m = m + 2;
        n = n + 1;
        }while( m <= n);
        printf("%d %d \n",m,n);
    */

    int m = 5;
    int n = 9;
    do
    {
        printf("% d % d \n", m, n);
        m = m + 2;
        n = n + 1;
    } while (m <= n);
    printf("% d % d \n", m, n);

    printf("\n");
    system("pause");

    return 0;

    // RTA:
    // 5   9
    // 7   10
    // 9   11
    // 11  12
    // 13  13
    // 15  14
}