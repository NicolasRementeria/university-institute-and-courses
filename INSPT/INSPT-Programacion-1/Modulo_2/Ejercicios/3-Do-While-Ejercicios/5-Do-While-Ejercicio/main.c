#include <stdio.h>
#include <stdlib.h>

int main()
{

    /*
        Escriba un programa que le permita al usuario intentar hasta cuatro veces la respuesta 
        a una cierta pregunta. Si el usuario no acierta a los cuatro intentos, se le deberá indicar 
        la respuesta correcta.
    */

    int anio, contador = 1;

    do
    {
        printf("Intento %d: Cual es mi anio de nacimiento? ", contador);
        scanf("%d", &anio);
        
        if (anio == 1989)
        {
            printf("Exacto! Naci en el 1989. Intentos = %d", contador);
            break;
        }
        if(contador == 4){
            printf("No! Naci en el 1989.");
        }
        contador++;
    } while (contador < 5);

        printf("\n");
    system("pause");

    return 0;
}