#include <stdio.h>
#include <stdlib.h>

void Mostrar_Rango_Stock(int stock, int codigo_articulo);

void Procesar_Stock_Minimo(int stock, int codigo_articulo, int *codigo_menor_stock, int *comparacion_stock_min);

void Procesar_Stock_Maximo(int stock, int codigo_articulo, int *codigo_mayor_stock, int *comparacion_stock_max);

void Procesar_Precio_Maximo(int precio, int codigo_articulo, int *codigo_maximo_precio, int *comparacion_precio_max);

int main()
{

    /*
        Se procesan los datos correspondientes a los artículos de venta de una empresa de electrodomésticos. De cada artículo 
        se ingresa el código del artículo, precio del artículo y stock del artículo. No se conoce la cantidad de artículos que 
        se procesan y el ingreso de datos finaliza con código de artículo -1. Se pide calcular:

            a. La cantidad de artículos ingresados
            b. Mostrar el mensaje “El articulo X está en el rango 120-360” si su stock está entre 120 y 360
            c. El artículo que tiene el mínimo de stock, el que tiene el máximo stock y el articulo de máximo de precio de venta
            d. El porcentaje de artículos que tengan precio de venta inferior a $3600
    */
    int codigo_articulo = 0;
    int n_articulos_totales = 0;
    int precio = 0;
    int stock = 0;
    int codigo_menor_stock = 0;
    int codigo_mayor_stock = 0;
    int codigo_maximo_precio = 0;
    int comparacion_precio_max = 0;
    int comparacion_stock_min = 0;
    int comparacion_stock_max = 0;
    int contador_venta_3600 = 0;

    printf("Ingrese el codigo del articulo (-1 para salir): ");
    scanf("%d", &codigo_articulo);

    while (codigo_articulo != -1)
    {

        n_articulos_totales += 1;
        printf("Ingrese precio del articulo: ");
        scanf("%d", &precio);
        printf("Ingrese stock del articulo: ");
        scanf("%d", &stock);
        if (precio < 3600)
            contador_venta_3600 += 1;
        if (n_articulos_totales == 1)
        {
            codigo_menor_stock = codigo_articulo;
            codigo_mayor_stock = codigo_articulo;
            codigo_maximo_precio = codigo_articulo;
            comparacion_precio_max = precio;
            comparacion_stock_min = stock;
            comparacion_stock_max = stock;
        }
        Mostrar_Rango_Stock(stock, codigo_articulo);
        Procesar_Stock_Minimo(stock, codigo_articulo, &codigo_menor_stock, &comparacion_stock_min);
        Procesar_Stock_Maximo(stock, codigo_articulo, &codigo_mayor_stock, &comparacion_stock_max);
        Procesar_Precio_Maximo(precio, codigo_articulo, &codigo_maximo_precio, &comparacion_precio_max);
        printf("Ingrese el codigo del articulo (-1 para salir): ");
        scanf("%d", &codigo_articulo);
    }

    printf("Cantidad de articulos: %d\n", n_articulos_totales);
    printf("El articulo %d tiene el minimo stock (%d)\n", codigo_menor_stock, comparacion_stock_min);
    printf("El articulo %d tiene el mayor stock (%d)\n", codigo_mayor_stock, comparacion_stock_max);
    printf("El articulo %d tiene el mayor precio (%d)\n", codigo_maximo_precio, comparacion_precio_max);
    printf("El porcentaje de articulos que tienen menor precio a 3600 es: %f", ((float)contador_venta_3600 / n_articulos_totales) * 100);

    printf("\n");
    system("pause");

    return 0;
}

void Mostrar_Rango_Stock(int stock, int codigo_articulo)
{
    if (stock >= 120 && stock <= 360)
    {
        printf("El articulo codigo %d esta en el rango 120-360\n", codigo_articulo);
    }
}

void Procesar_Stock_Minimo(int stock, int codigo_articulo, int *codigo_menor_stock, int *comparacion_stock_min)
{
    if (stock < *comparacion_stock_min)
    {
        *codigo_menor_stock = codigo_articulo;
        *comparacion_stock_min = stock;
    }
}

void Procesar_Stock_Maximo(int stock, int codigo_articulo, int *codigo_mayor_stock, int *comparacion_stock_max)
{
    if (stock > *comparacion_stock_max)
    {
        *codigo_mayor_stock = codigo_articulo;
        *comparacion_stock_max = stock;
    }
}

void Procesar_Precio_Maximo(int precio, int codigo_articulo, int *codigo_maximo_precio, int *comparacion_precio_max)
{
    if (precio > *comparacion_precio_max)
    {
        *codigo_maximo_precio = codigo_articulo;
        *comparacion_precio_max = precio;
    }
}