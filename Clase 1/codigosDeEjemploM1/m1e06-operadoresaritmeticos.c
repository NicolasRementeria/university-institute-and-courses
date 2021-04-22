#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a,b=10,c=0,d=0;
    float precio;

    a=5;        // asignacion de dato
    a=a-1;      // resta de valores y guardado del resultado en una variable
    b=a+b+4;    // suma de variables
    a+b;        // esto vale, pero el resultado de la suma se pierde

    printf("En este punto, la variable a vale %d y la b vale %b\n",a,b);
    printf("Operaciones directamente en el printf: %d\n",a*b);

    // division entera
    precio=10/3;
    printf("Division entera, precio=%2.2f\n",precio);
    // division decimal
    precio=10/3.0;
    printf("Division decimal, precio=%2.2f\n",precio);
    // operador resto
    a=10%3;
    printf("Resto de division entera, a=%d\n\n",a);

    // operadores de (pre/post)incremento
    a=b;
    a++;
    printf("Despues del a++, b vale %d y a vale %d\n",b,a--); // el decremento se ejecuta al final de la instruccion
    printf("Luego del post-decremento: %d\n",a);
    printf("Luego del pre-decremento: %d\n",++a);

    // asociatividad
    a=1; b=2; c=3; d=4;
    printf("operacion 1: %d\n",a+b+c); // 1+2+3=6
    printf("operacion 2: %d\n",a+b-c); // 1+2-3=0
    printf("operacion 3: %d\n",a+b*c); // 1+2*3=7
    printf("operacion 4: %d\n",a+(b*c));  // 1+(2*3)=7
    printf("operacion 5a: %d\n",(a+b)*c); // (1+2)*3=9
    printf("operacion 5b: %d\n",a+b*c); // 1+2*3=7
    printf("operacion 5c: %d\n",a+(b*c)); // 1+(2*3)=7 parentesis redundante
    printf("operacion 6: %d\n\n",a*b+c*d); // 1*2+3*4=14

    /*
    OPERADORES ARITMETICOS CON ASIGNACION
    */
    a=b;
    a+=2;
    printf("Ahora b vale %d y a vale %d\n",b,a);
    a/=2;
    printf("Ahora a vale %d\n",a);

    return 0;
}
