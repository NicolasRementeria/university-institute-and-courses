#include <stdio.h>
#include <stdlib.h>

int main()
{
    // declaracion de una variable
    int a=20;

    // condicional de una sola instruccion por cada caso
    if (a%10==0)
        printf("Es divisible por 10\n");
    else
        printf("*** No divisible por 10 ***\n");
    /*
    los condicionales evaluan expresiones, y dependiendo del resultado,
    la seccion que ejecutan
    */
    a=1;
    if (a) // resulta que el valor cero decimal se considera FALSO, todo lo demas es VERDADERO
        printf("a vale TRUE\n");
    else
        printf("a vale FALSE\n");


    // condicional con varias instrucciones por cada caso
    printf("Ingrese un valor entero:");
    scanf("%d",&a);
    if (a%10==0){
        // las llaves delimitan el bloque de codigo a ejecutar por verdadero
        printf("Sigue siendo divisible por 10\n");
        a++;
        printf("ahora la variable seguro no es divisible por 10 (vale %d)\n",a);
    }
    else {
        // los comentarios no son parte del bloque de codigo, pero tampoco esta mal si hay una sola linea como aqui
        printf("*** No divisible por 10 ***\n");
    }

    return 0;
}
