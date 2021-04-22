#include <stdio.h>
#include <stdlib.h>

int main()
{
    int miVariable=65;
    float precio=10.50;
    char letra;
    printf("Formatos de salida para las varaibles\n");

    printf("Variables enteras\n");
    printf("Como %%d: %d\n",miVariable); // como decimal
    printf("Como %%c: %c\n",miVariable); // como caracter segun codigo ASCII
    printf("Como %%f: %f\n",miVariable); // como flotante
    printf("Como %%x: %x\n",miVariable); // como hexadecimal

    printf("Ingrese un valor numerico: ");
    scanf("%d",&miVariable);
    printf("El valor ingresado es: %d\n",miVariable);
    system("PAUSE");

    printf("\nVariables flotantes\n");
    printf("Como %%d: %d\n",precio); // como decimal
    printf("Como %%c: %c\n",precio); // como caracter segun codigo ASCII
    printf("Como %%f: %f\n",precio); // como flotante
    printf("Como %%2.2f: %2.2f\n",precio); // como flotante
    printf("Como %%x: %x\n",precio); // como hexadecimal

    printf("Ingrese un valor decimal: ");
    scanf("%f",&precio); // es CRUCIAL colocar el formato de lectura correcto!!!!!
    printf("El valor ingresado es: %2.2f\n",precio);

    printf("Ingrese un valor caracter: ");
    fflush(stdin); // esta funcion ES NECESARIA por cómo el formato de texto trabaja
    scanf("%c",&letra); // es CRUCIAL colocar el formato de lectura correcto!!!!!
    printf("El valor ingresado es: %c\n",letra);

    system("PAUSE");

    return 0;
}
