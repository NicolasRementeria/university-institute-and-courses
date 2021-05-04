#include <stdio.h>
#include <stdlib.h>

int main()
{

    /*
        Recomendado: Se ingresa un número de hasta 5 cifras y se indica si es o no capicúa.
    */

    int numero, unidad, decena, centena, unidad_de_mil, decena_de_mil;

    printf("Ingrese un numero de hasta 5 cifras: ");
    scanf("%d", &numero);

    if (numero >= 10000 && numero <= 99999){
        //El numero tiene 5 digitos
        decena_de_mil = (int)(numero / 10000);
        unidad_de_mil = (int)(numero / 1000) - decena_de_mil * 10;
        centena       = (int)(numero / 100) - decena_de_mil * 100 - unidad_de_mil * 10;
        decena        = (int)(numero / 10) - decena_de_mil * 1000 - unidad_de_mil * 100 - centena * 10;
        unidad        = numero  - decena_de_mil * 10000 - unidad_de_mil * 1000 - centena * 100 - decena * 10;
        printf("El numero %d esta dividido en: dM = %d M = %d c = %d d = %d u = %d\n", numero, decena_de_mil, unidad_de_mil, centena, decena, unidad);
        if (decena_de_mil == unidad && unidad_de_mil == decena)
            printf("El numero es capicua!");
        else
            printf("El numero NO es capicua!");
    }
    else if (numero >= 1000 && numero <= 9999) {
        //El numero tiene 4 digitos
        unidad_de_mil = (int)(numero / 1000);
        centena       = (int)(numero / 100) - unidad_de_mil * 10;
        decena        = (int)(numero / 10) - unidad_de_mil * 100 - centena * 10;
        unidad        = numero - unidad_de_mil * 1000 - centena * 100 - decena * 10;
        printf("El numero %d esta dividido en: M = %d c = %d d = %d u = %d\n", numero, unidad_de_mil, centena, decena, unidad);
        if (unidad_de_mil == unidad && centena == decena)
            printf("El numero es capicua!");
        else
            printf("El numero NO es capicua!");
    }
    else if (numero >= 100 &&  numero <= 999){
        //El numero tiene 3 digitos
        centena       = (int)(numero / 100);
        decena        = (int)(numero / 10) - centena * 10;
        unidad        = numero - centena * 100 - decena * 10;
        printf("El numero %d esta dividido en: c = %d d = %d u = %d\n", numero, centena, decena, unidad);
        if (centena == unidad)
            printf("El numero es capicua!");
        else
            printf("El numero NO es capicua!");
    }
    else if(numero >= 10 && numero <= 99){
        //El numero tiene 2 digitos
        decena        = (int)(numero / 10);
        unidad        = numero - decena * 10;
        printf("El numero %d esta dividido en: d = %d u = %d\n", numero, decena, unidad);
        if (decena == unidad)
            printf("El numero es capicua!");
        else
            printf("El numero NO es capicua!");
    }
    else{
        //El numero tiene 1 digito
        printf("El numero %d no puede ser capicua!", numero);
    }

    return 0;
}