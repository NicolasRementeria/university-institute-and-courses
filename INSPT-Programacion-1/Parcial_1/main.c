#include <stdio.h>
#include <stdlib.h>

/*
    Antes de empezar: Lea el enunciado completo antes de empezar. Utilizar punteros cuando sea necesario. 
    No utilizar variables globales. Escribir con letra clara y entregar en tinta, identificando nombre, apellido y fecha en cada hoja.
    Una agencia de marketing necesita una aplicación para el proceso de sus clientes y publicidades. Para ello se reúne con usted y define:

    1- Construir una función que permita procesar una cantidad desconocida de ids de clientes que finaliza con el número 0. 
    Por cada cliente se ingresa su categoría (P-Platinum, G-Gold)   y una cantidad desconocida de publicidades. Cada publicidad tiene 
    un importe y un rating. Por lo tanto, se debe ingresar:
        a. rating: B (bueno), R (regular), M (malo) -carácter-
        b. Importe: número decimal
    Esta función debe emitir por cada cliente ingresado cuánto dinero se recaudó por cada rating, que se procesan en la función 2. Ejemplo:
    Total de publicidades del cliente 64: $10.000
    Publicidades buenas: $2.000
    Publicidades regulares: $3.000
    Publicidades malas: $4.000

    2- Construir una función que reciba al menos categoría e importe y devuelva (de alguna manera) a la función 1 todos los totales 
    de las facturas procesadas por cada cliente.

    3- En main el mensaje final que se emite debe mostrar:
        a. Total de clientes procesados
        b. Qué rating dejo más ganancias en total
        c. Qué categoría de cliente fue la más lucrativa
*/

void Reiniciar_Variable_Recaudaciones(float *recaudacion_B, float *recaudacion_R, float *recaudacion_M, float *recaudacion_total);
void Procesar_Clientes();
void Mostrar_Recaudacion_Del_Cliente(int id_cliente, float recaudacion_total, float recaudacion_B, float recaudacion_R, float recaudacion_M);
int Es_Categoria_Valida(char categoria);
char Ingresar_Categoria();
int Es_Rating_Valido(char rating);
char Ingresar_Rating();
void Procesar_Publicidades(int id_cliente, char categoria, float *recaudacion_B, float *recaudacion_M, float *recaudacion_R, float *recaudacion_total);

int main()
{
    int total_clientes = 0;
    float rating_B_total = 0, rating_M_total = 0, rating_R_total = 0; 
    float suma_categoria_G = 0, suma_categoria_P = 0;
    Procesar_Clientes(&total_clientes, &rating_B_total, &rating_M_total, &rating_R_total, &suma_categoria_G, &suma_categoria_P);

    printf("Total Clientes: %d\n", total_clientes);
    if(rating_B_total > rating_M_total && rating_B_total > rating_R_total)
        printf("El Rating B dejo mas ganancias (B: %f | M: %f | R: %f)\n", rating_B_total, rating_M_total, rating_R_total);
    if(rating_M_total > rating_B_total && rating_M_total > rating_R_total)
        printf("El Rating M dejo mas ganancias (B: %f | M: %f | R: %f)\n", rating_B_total, rating_M_total, rating_R_total);
    if(rating_R_total > rating_B_total && rating_R_total > rating_M_total)
        printf("El Rating R dejo mas ganancias (B: %f | M: %f | R: %f)\n", rating_B_total, rating_M_total, rating_R_total);
    if(suma_categoria_G > suma_categoria_P)
        printf("La categoria G fue la mas lucrativa (G: %f | P: %f)\n", suma_categoria_G, suma_categoria_P);
    else
        printf("La categoria P fue la mas lucrativa (G: %f | P: %f)\n", suma_categoria_G, suma_categoria_P);

    printf("\n");
    system("pause");

    return 0;
}

void Reiniciar_Variable_Recaudaciones(float *recaudacion_B, float *recaudacion_R, float *recaudacion_M, float *recaudacion_total)
{
    *recaudacion_B = 0;
    *recaudacion_R = 0;
    *recaudacion_M = 0;
    *recaudacion_total = 0;
}

void Procesar_Clientes(int *total_clientes, float *rating_B_total, float *rating_M_total, float *rating_R_total, float *suma_categoria_G, float *suma_categoria_P)
{
    int id_cliente;
    char categoria;
    float recaudacion_B = 0, recaudacion_R = 0, recaudacion_M = 0, recaudacion_total = 0;
    printf("Ingrese id del cliente (0 para salir): ");
    scanf("%d", &id_cliente);
    while (id_cliente != 0)
    {
        (*total_clientes)++;
        categoria = Ingresar_Categoria();
        Procesar_Publicidades(id_cliente, categoria, &recaudacion_B, &recaudacion_M, &recaudacion_R, &recaudacion_total);
        *rating_B_total += recaudacion_B;
        *rating_M_total += recaudacion_M;
        *rating_R_total += recaudacion_R;
        if(categoria == 'p' || categoria == 'P')
            *suma_categoria_P += recaudacion_total;
        else if(categoria == 'g' || categoria == 'G')
            *suma_categoria_G += recaudacion_total;
        Mostrar_Recaudacion_Del_Cliente(id_cliente, recaudacion_total, recaudacion_B, recaudacion_R, recaudacion_M);
        Reiniciar_Variable_Recaudaciones(&recaudacion_B, &recaudacion_R, &recaudacion_M, &recaudacion_total);
        printf("Ingrese id del cliente (0 para salir): ");
        scanf("%d", &id_cliente);
    }
}

void Mostrar_Recaudacion_Del_Cliente(int id_cliente, float recaudacion_total, float recaudacion_B, float recaudacion_R, float recaudacion_M){
    printf("Total de publicidades del cliente %d: $%f\n", id_cliente, recaudacion_total);
    printf("Publicidades buenas: %f\n", recaudacion_B);
    printf("Publicidades regulares: %f\n", recaudacion_R);
    printf("Publicidades malas: %f\n", recaudacion_M);
}

int Es_Categoria_Valida(char categoria)
{
    if (categoria == 'p' || categoria == 'P' || categoria == 'g' || categoria == 'G')
        return 1;
    else
        return 0;
}

char Ingresar_Categoria()
{
    char categoria = 'a';
    while (!Es_Categoria_Valida(categoria))
    {
        printf("Ingrese categoria (P o G): ");
        fflush(stdin);
        scanf("%c", &categoria);
    }
    return categoria;
}

int Es_Rating_Valido(char rating)
{
    if (rating == 'b' || rating == 'B' || rating == 'r' || rating == 'R' || rating == 'm' || rating == 'M' || rating == 'x' || rating == 'X')
        return 1;
    else
        return 0;
}

char Ingresar_Rating()
{
    char rating;
    printf("Ingrese rating (B, M o R), X PARA SALIR: ");
    fflush(stdin);
    scanf("%c", &rating);
    while (!Es_Rating_Valido(rating))
    {
        printf("Ingrese rating (B, M o R), X PARA SALIR: ");
        fflush(stdin);
        scanf("%c", &rating);
    }
    return rating;
}

void Procesar_Publicidades(int id_cliente, char categoria, float *recaudacion_B, float *recaudacion_M, float *recaudacion_R, float *recaudacion_total)
{
    float dinero_ingresado = 0;
    char rating;
    rating = Ingresar_Rating();
    while (rating != 'x' && rating != 'X')
    {
        printf("Cliente %d | Categoria %c | Rating %c | Ingresar dinero: ", id_cliente, rating, categoria);
        scanf("%f", &dinero_ingresado);
        *recaudacion_total += dinero_ingresado;
        if (rating == 'b' || rating == 'B')
            *recaudacion_B += dinero_ingresado;
        if (rating == 'm' || rating == 'M')
            *recaudacion_M += dinero_ingresado;
        if (rating == 'r' || rating == 'R')
            *recaudacion_R += dinero_ingresado;
        rating = Ingresar_Rating();
    }
}