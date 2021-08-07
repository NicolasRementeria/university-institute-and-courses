#include <stdio.h>
#include <stdlib.h>

int main(){
    int a=5, e=5>1;
    float b=13.546;
    char c='A';
    char d='a';

    printf ("1)  a vale %d\n", a);    // 5
    printf ("2)  a vale %O\n", a);    // 0 (null))
    printf ("3)  a vale %X\n", a);    // 5 (hexa)
    printf ("4)  a vale %f\n", a);    // 0.00000
    printf ("5)  a vale %c\n", a);    // ♣
    printf ("6)  b vale %d\n", b);    // 1073741824 (???)
    printf ("7)  b vale %5.2d\n", b); // 1073741824 (???)
    printf ("8)  b vale %f\n", b);    // 13.546000
    printf ("9)  b vale %.1f\n", b);  // 13.5
    printf ("10) b vale %.2f\n", b);  // 13.55 (redondeo el centecimo de 6 al decimo pasando de 4 a 5)
    printf ("11) b vale %6.4f\n", b); // 13.5460
    printf ("12) b vale %6.1f\n", b); // 6 espacios partiendo del numero menos significado, "  13.5"
    printf ("13) b vale %c\n", b);    // retorno de carro?
    printf ("14) b vale %O\n", b);    // 0 (null)
    printf ("15) b vale %X\n", b);    // 40000000 (hexa?)
    printf ("16) c vale %d\n", c);    // 65
    printf ("17) c vale %f\n", c);    // 13.545998 (???)
    printf ("18) c vale %c\n", c);    // A
    printf ("19) c vale %O\n", c);    // 0 (null)
    printf ("20) c vale %X\n", c);    // 41 (hexa)
    printf ("21) d vale %d\n", d);    // 97
    printf ("22) d vale %f\n", d);    // 13.545998 (???)
    printf ("23) d vale %c\n", d);    // a
    printf ("24) d vale %O\n", d);    // 0 (null)
    printf ("25) d vale %X\n", d);    // 61 (hexa)
    printf ("26) e vale %d\n", e);    // 1
    printf ("27) e vale %f\n", e);    // 13.545998 (???)
    printf ("28) e vale %c\n", e);    // ☺
    printf ("29) e vale %O\n", e);    // 0 (null)
    printf ("30) e vale %X\n", e);    // 1 (hexa)

    return 0;
}