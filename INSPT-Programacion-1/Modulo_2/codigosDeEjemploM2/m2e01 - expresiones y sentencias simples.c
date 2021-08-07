#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a;
    // esto es una expresion, da un resultado pero no se guarda en ningun lado
    // (no significa que no se ejecute, porque sí se ejecuta)
    (8+15/3);
    // una instruccion, una expresion cuyo resultado se asigna a una variable
    a=(8+15/3);
    printf("a=%d\n",a);
    printf("Ingrese un numero entero: ");
    scanf("%d",&a);
    a=a*4;
    printf("ahora a vale %d\n",a);
    return 0;
}
