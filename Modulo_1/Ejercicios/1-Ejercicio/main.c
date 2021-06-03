#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a = 3, b = 2, c = 1, d, e;
    float m = 2.5, n = 5.4, r, s;

    printf("a = %d, b = %d, c = %d, d = %d, e = %d \n", a, b, c, d, e);
    printf("m = %f,  n = %f, r = %f, s = %f \n", m, n, r, s);

    /* 
        "d" es un int, "m" es un float (2.5). Al asignarle "m" a "d", guarda realmente solo la parte entera (2), no la decimal.
        Si se muestra "d" en pantalla con la mascara dint, muestra el 2; si se muestra con mascara float, no lo entiende y 
        muestra la parte decimal del int, que es siempre 0) 
    */
    //d = m;
    //printf("%d o %f", d, d);
    // resultado:
    // 2 o -0.000000


    /*
            Mismo caso que arriba, "d" es un int, "n" es un float (5.4), al asignarle "n" a "d", "d" vale 5
            Si se muestra como dint muestra 5, si se muestra como float muestra la parte decimal del int, siendo -0.000...
    */
    //d = n;
    //printf("%d o %f", d, d);
    // resultado:
    // 5 o -0.000000jaja is


    /*
        "e" es un int, al asignarle un valor float valdra solo la parte entera.
        Al mostrarse como dint muestra 3, al mostrarse como float muestra -0.000...
    */
    //e=3.7;
    //printf("%d o %f", e, e);
    // resultado:
    // 3 o -0.000000


    /*
        "d" y "a" (3) son ints, asique "d" va a valer lo que valia "a"
    */
    //d=a;
    //printf("%d o %f", d, d);
    // resultado:
    // 3 o -0.000000


    /*
        "a" = 3, "b" = 2, "d" = 3+2
    */
    //d=a+b;
    //printf("%d", d);
    // resultado:
    // 5
    

    /*
        "a" = 3, "b" = 2, "d" = 3/2
        Las 3 variables son dint, como el resultado es float (3/2 = 1.5), y  "d" es int, solo guarda el valor entero
        Al mostrarse en pantalla como dint, muestra 1, si se muestra como float muestra -0.000...
    */
    //d=a/b;
    //printf("%d o %f", d, d);
    // resultado: 
    // 1 o -0.000000


    /*
        "a" = 3, "b" = 2, "d" = 3%2 guardará el valor del resto, siendo 1.
    */
    //d=a%b;
    //printf("%d", d);
    // resultado: 
    // 1


    /*
        "a" = 3, "d" = 3%2 guardará el valor del resto, siendo 1.
    */
    //d=a%2;
    //printf("%d", d);
    // resultado: 
    // 1


    /*
        "e" es un int no inicializado, por lo cual puede valer cualquier int
        "b" = 2, "c" = 1
        "e" = 2/1 = 2
    */
    //e=b/c;
    //printf("%d", e);
    // resultado: 
    // 2


    /*
        "e" es un int no inicializado, por lo cual puede valer cualquier int
        "c" es un int que vale 1
        "b" es un int que vale 2
        3/2 = 0.5, pero como "e" es un int valdrá 0, tanto si se muestra como dint como float
    */
    //e=c/b;
    //printf("%d o %f", e, e);
    // resultado: 
    // 0 o -0.000000


    /*
        "r" es un float no inicializado
        "a" es un int que vale 3
        "b" es un int que vale 2
        3+2 = 5, "r" como float valdrá 5.000...; como dint por alguna razon da 0
    */
    //r=a+b;
    //printf("%f, %d", r, r);
    // resultado: 
    // 5.000000, 0


    /*
        "r" es un float no inicializado
        "a" es un int que vale 3
        "b" es un int que vale 2
        3/2 = 1.5, pero como son enteros el resultado que guardarán en r como float es el 1.0000
        Si se muestra en pantalla r, como float mostrará 1.0000 y si se muestra como dint será 0
    */
    //r=a/b;
    //printf("%f, %d", r, r);
    // resultado: 
    // 1.000000, 0


    /*
        "r" es un float no inicializado
        "a" es un int que vale 3
        3/2 = 1.5, pero como son enteros el resultado que guardarán en r como float es el 1.0000
        Si se muestra en pantalla r, como float mostrará 1.0000 y si se muestra como dint será 0
    */
    //r=a/2;
    //printf("%f, %d", r, r);
    // resultado: 
    // 1.000000, 0


    /*
        "r" es un float no inicializado
        "a" es un int que vale 3
        3/2.0 = 1.5000..., mostrado como float valdrá 1.500... y como dint, 0 
    */
    //r=a/2.0;
    //printf("%f, %d", r, r);
    // resultado: 
    // 1.500000, 0


    /*
        "s" es un float no inicializado
        "m" es un float que vale 2.5
        "n" es un float que vale 5.4
        2.5 + 5.4 = 7.9, como "s" es un float puede almacenar el resultado
    */
    //s=m+n;
    //printf("%f", s);
    // resultado: 
    // 7.900000


    /*
        Al "s" ser un float, no puede almacenar valores dint
        3+4-1 = 6, pero "s" al no poder almacenarlo se convertirá en 0.000...
        Si se muestra como dint, será un 0, si se muestra como float será 0.000...
    */
    //s=3+4-1;
    //printf("%d, %f", s, s);
    // resultado: 
    //


    /*
        Al al menos un valor de la operacion es un float, el resultado puede almacenarse en "s"
        3.0 + 4.0 - 1 = 6.0000
        Mostrado como float será 6.000..., mostrado como dint será 0.
    */
    //s=3.0+4.0-1;
    //printf("%f, %d", s, s);
    // resultado: 
    // 6.000000, 0


    /*
        "a" es un int
        "m" es un float que vale 2.5
        "a" solo podrá almacenar la parte entera, por lo cual "a" valdrá 2
        Si se muestra "a" como int, muestra 2, si se muestra como float mostrará -0.000...
    */
    //a=m;
    //printf("%d, %f", a, a);
    // resultado: 
    // 2, -0.000000


    /*
        "a" es un int
        "m" es un float que vale 2.5
        2.5 / 2 = 1.25
        Como "a" es un int, solo podrá almacenar la parte entera, por lo cual "a" valdrá 1
    */
    //a=m/2;
    //printf("%d, %f", a, a);
    // resultado: 
    // 1, -0.000000


    /*
        "a" es un int
        "m" es un float que vale 2.5
        2.5 / 2.0 = 1.25
        "a" sigue siendo un int, por lo cual solo puede almacenar el valor entero 1.
    */
    //a=m/2.0;
    //printf("%d, %f", a, a);
    // resultado: 
    // 1, -0.000000


    /*
        "a" es un int
        3.0 + 4.0 - 1 = 6.0
        Como "a" es un int, solo puede almacenar el valor entero, 6
    */
    //a=3.0+4.0-1;
    //printf("%d, %f", a, a);
    // resultado: 
    // 6, -0.000000


    /*
        "r" es un float
        "a" es un int que vale 3
        3 + 1 = 4, pero como "r" es un float almacenará 4.000...
        Mostrado por pantalla como float mostrará 4.000..., como dint mostrará 0.
    */
    //r=a+1;
    //printf("%f, %d", r, r);
    // resultado: 
    // 4.000000, 0


    /*
        Igual que arriba
    */
    //r=a+1.0;
    //printf("%f, %d", r, r);
    // resultado: 
    // 4.000000, 0


    /*
        Incrementa el valor de "a" por 1 y lo almacena en "a"
    */
    //a++;
    //printf("%d", a);
    // resultado: 
    // 4


    /*
        "r" no está inicializado
        Deberia igual sumarle 1 al valor de "r", pero por alguna razon no lo hizo
        De todas maneras, aplicar incremental o decremental (++, --) a un float es una mala practica y esta desaconsejado
    */
    //r++;
    //printf("%d, %f", r, r);
    // resultado: 
    // 0, 0.000000


    /*
        "b" es un int y vale 2
        b-- hace que "b" valga 1
    */
    //b--;
    //printf("%d", b);
    // resultado: 
    // 1


    /*
        "a" es un int y vale 3
        a += 5 le sumará 5 a "a" y el resultado lo almacenará en "a" 
    */
    //a+=5;
    //printf("%d", a);
    // resultado: 
    // 5


    /*
        "s" es un float y no está inicializado por lo tanto puede valer cualquier float
        s *= 5 multiplicará "s" por 5 y el valor lo almacenará en "s"
    */
    //s*=5;
    //printf("%f, %d", s, s);
    // resultado: 
    // 4371728303494513300000000000000000.000000, 0


    return 0;
}