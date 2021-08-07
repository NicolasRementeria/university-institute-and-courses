#include <stdio.h>
#include <stdlib.h>

int main(){

    int a;
    float b;
    char c;
    printf("1) ");
    scanf("%d", &a);  // 10 > 10
    printf("%d\n", a);

    printf("2) ");
    scanf("%f", &a);  // 10 > 0.000000
    printf("%f\n", a);

    printf("3) ");
    scanf("%c", &a); // salto de linea??
    printf("%c\n", a);

    printf("4) ");
    scanf("%d", &b); // 10 > 0
    printf("%d\n", b);

    printf("5) ");
    scanf("%f", &b); // 10 > 10.000000
    printf("%f\n", b);

    printf("6) ");
    scanf("%c", &b);  // salto de linea??
    printf("%c\n", b);

    printf("7) ");
    scanf("%d", &c);  // 10 > 10
    printf("%d\n", c);

    printf("8) ");
    scanf("%f", &c);  // 10 > 10.000008
    printf("%f\n", c);

    printf("9) ");
    scanf("%f", &c);  // 10 > 10.000008
    printf("%f\n", c);

    return 0;
}