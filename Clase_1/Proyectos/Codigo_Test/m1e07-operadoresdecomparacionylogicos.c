#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a=5,b=7,c=0,d=0,e=0;
    float precio;

    a<b;    // esto vale, pero el resultado no se guarda

    c=a<b;
    d=a>b;
    printf("Comparacion por mayor/menor:\n");
    printf("c=%d  d=%d \n",c,d);

    c=a==b;
    d=a!=b;
    printf("Comparacion por igual/distinto:\n");
    printf("c=%d  d=%d \n",c,d);

    a=1;
    b=0;
    c=a&&b;
    d=a||b;
    e=!d;
    printf("comparacion por AND/OR:\n");
    printf("c=%d  d=%d e=%d\n",c,d,e);

    return 0;
}
