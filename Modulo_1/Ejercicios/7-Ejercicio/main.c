#include <stdio.h>
#include <stdlib.h>

int main()
{
    // Obtener el n° de bytes por tipo de objeto
    char c;
    short s;
    int i;
    long l;
    float f;
    double d;
    long double ld;
    printf("\nA continuación…\n");
    printf("El sizeof de un char es %d\n", sizeof(c));
    printf("El sizeof de un short es %d\n", sizeof(s));
    printf("El sizeof de un int es %d\n", sizeof(i));
    printf("El sizeof de un long es %d\n", sizeof(l));
    printf("El sizeof de un float es %d\n", sizeof(f));
    printf("El sizeof de un double es %d\n", sizeof(d));
    printf("El sizeof de un long double es %d\n", sizeof(ld));
    printf("El sizeof 1+1 es %d\n", sizeof(1+1));
    printf("El sizeof 1.+1. es %d\n", sizeof(1.+1.));
    system("Pause");
    return 0;
}