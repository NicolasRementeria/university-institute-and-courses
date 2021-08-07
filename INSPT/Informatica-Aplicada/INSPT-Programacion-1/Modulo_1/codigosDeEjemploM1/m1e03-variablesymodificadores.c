#include <stdio.h>
#include <stdlib.h>

int variableExterna=10;

int main()
{
    unsigned char charSinSigno=400;
    signed char charSignado=400;
    const miConstante=6;
    static char variableResidente='A';
    extern int variableExterna;

    printf("los enteros son %d y %d\n",charSinSigno, charSignado);
    //miConstante=5; // la constante es de solo lecture

    printf("Variable externa=%d\n",variableExterna);
    return 0;
}
