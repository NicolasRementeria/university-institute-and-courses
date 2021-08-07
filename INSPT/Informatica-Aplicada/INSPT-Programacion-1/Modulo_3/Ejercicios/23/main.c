#include <stdio.h>
#include <stdlib.h>

int leeOpcion();
int menu();
float cuadrado(int lado);
float circulo(int radio);
float rectangulo(int base, int altura);
float trapecio(int base1, int base2, int altura);
float triangulo(int base, int altura);

int main()
{

    /*
        23) RECOMENDADO: Escribe un programa teniendo en cuenta las siguientes funciones:
        • leeOpcion lee la opción deseada y comprueba su validez
        • menú muestra el menú en la pantalla
        • cuadrado, circulo, rectángulo, trapecio, triángulo calculan la superficie correspondiente.
        
        El menú por mostrar sería algo como lo que sigue:
        ************************************
        ****** CÁLCULO DE SUPERFICIES ******
        1. Cuadrado (lado*lado)
        2. Círculo (pi*radio*radio)
        3. Rectángulo (base*altura)
        4. Trapecio (base1+base2)*altura/2)
        5. Triángulo (base*altura)/2)
        0. Salir del programa
        ************************************
    */

    int opcion;
    int lado, radio, base, altura, base1, base2;
    float resultado;

    do
    {
        menu();
        opcion = leeOpcion();
        switch (opcion)
        {
        case 1:
            printf("CUADRADO\n");
            printf("Lado:");
            scanf("%d", &lado);
            resultado = cuadrado(lado);
            printf("Superficie = %f\n", resultado);
            break;
        case 2:
            printf("CIRCULO\n");
            printf("Radio:");
            scanf("%d", &radio);
            resultado = circulo(radio);
            printf("Superficie = %f\n", resultado);
            break;
        case 3:
            printf("RECTANGULO\n");
            printf("Lado:");
            scanf("%d", &base);
            printf("Lado:");
            scanf("%d", &altura);
            resultado = rectangulo(base, altura);
            printf("Superficie = %f\n", resultado);
            break;
        case 4:
            printf("TRAPECIO\n");
            printf("Base 1:");
            scanf("%d", &base1);
            printf("Base 2:");
            scanf("%d", &base2);
            printf("Altura:");
            scanf("%d", &altura);
            resultado = trapecio(base1, base2, altura);
            printf("Superficie = %f\n", resultado);
            break;
        case 5:
            printf("TRIANGULO\n");
            printf("Base:");
            scanf("%d", &base);
            printf("Altura:");
            scanf("%d", &altura);
            resultado = triangulo(base, altura);
            printf("Superficie = %f\n", resultado);
            break;
        }

    } while (opcion != 0);

    printf("\n");
    system("pause");

    return 0;
}

int leeOpcion(){
    int opcion;
    do{
        printf("Ingrese opcion: ");
        scanf("%d", &opcion);
        if(opcion > 5){
            printf("DATO NO VALIDO.\n");
            //menu();
        }
    }while(opcion > 5);
    return opcion;
}

int menu(){
    printf("************************************\n");
    printf("****** CALCULO DE SUPERFICIES ******\n");
    printf("1. Cuadrado (lado*lado)\n");
    printf("2. Circulo (pi*radio*radio)\n");
    printf("3. Rectangulo (base*altura)\n");
    printf("4. Trapecio (base1+base2)*altura/2)\n");
    printf("5. Triangulo (base*altura)/2)\n");
    printf("0. Salir del programa\n");
    printf("************************************\n");
}

float cuadrado(int lado){
    return lado*(float)lado;
}

float circulo(int radio){
    return 3.14*radio*radio;
}

float rectangulo(int base, int altura){
    return base * (float)altura;
}

float trapecio(int base1, int base2, int altura){
    return (base1+base2)*(float)altura/2;
}
float triangulo(int base, int altura){
    return base*(float)altura/2;
}