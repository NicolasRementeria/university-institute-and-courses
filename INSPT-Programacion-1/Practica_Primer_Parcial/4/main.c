#include <stdio.h>
#include <stdlib.h>

/*
    4. Se desea procesar las compras realizadas por los clientes de una empresa mayorista. La empresa tiene un grupo de N clientes. 
    El valor de N se ingresa por teclado. Para cada uno, se ingresa el código de cliente, la zona de compra 
    (puede ser ‘a’, ‘b’, ‘c’, ‘d’, ‘e’ o ‘f’) y una serie de importes correspondientes a las compras que realizaron. 
    El número de compras por cada cliente es variable y se ingresa un -1 para terminar el ingreso de las compras.
    La empresa tiene un sistema especial de premios para los clientes de algunas zonas. Si el cliente reside en 
    zona ‘a’ o ‘b’ se le bonifica el 20% de la compra. Si reside en ‘c’ la bonificación es del 10%. Si la zona 
    es ‘d’ o ‘e’ participan en un sorteo de un automóvil. Se desea realizar un programa en C que:
    
        a. Para cada cliente emitir el importe total de compras sin la bonificación, con la bonificación y si ha participado o no del sorteo.
        b. Emitir el total de ventas de la zona ‘f’.
        c. Emitir un mensaje indicando cuantos clientes corresponden a la zona ‘a’ o ‘c’.
*/

void Es_Cliente_A_o_C(char zona, int *cantidad_clientes_a, int *cantidad_clientes_c);

float Procesar_Compras(char zona, int *total_ventas_f);

int Es_Bonificado(char zona);

int Participa_En_Sorteo(char zona);

float Calcular_Bonificacion(char zona, float importe);

int main()
{

    int numero_de_clientes, i, codigo_de_cliente, total_ventas_f = 0, cantidad_clientes_a = 0, cantidad_clientes_c = 0;
    char zona_de_compra;
    float importe_total_cliente, importe_con_bonificacion;

    printf("Ingrese numero de clientes: ");
    scanf("%d", &numero_de_clientes);

    for (i = 0; i < numero_de_clientes; i++)
    {
        //Ingreso de Compras por cliente
        printf("Ingrese codigo de cliente: ");
        scanf("%d", &codigo_de_cliente);
        printf("Ingrese zona de compra (a, b, c, d, e, f): ");
        fflush(stdin);
        scanf("%c", &zona_de_compra);
        

        Es_Cliente_A_o_C(zona_de_compra, &cantidad_clientes_a, &cantidad_clientes_c);

        importe_total_cliente = Procesar_Compras(zona_de_compra, &total_ventas_f);

        if (Es_Bonificado(zona_de_compra))
        {
            importe_con_bonificacion = Calcular_Bonificacion(zona_de_compra, importe_total_cliente);
        }
        else
        {
            importe_con_bonificacion = importe_total_cliente;
        }

        if (Participa_En_Sorteo(zona_de_compra))
        {
            printf("El cliente numero %d participa en sorteo por Automovil!\n", codigo_de_cliente);
        }

        printf("Cod. Cliente: %d | Zona Compra: %c | Importe Total: %f | Importe Bonificado: %f | Participa en Sorteo (1 = Si, 0 = No): %d  \n", codigo_de_cliente, zona_de_compra, importe_total_cliente, importe_con_bonificacion, Participa_En_Sorteo(zona_de_compra));
    }
    printf("Total de ventas Zona F: %d\n", total_ventas_f-1);
    printf("Total de clientes A: %d\n", cantidad_clientes_a);
    printf("Total de clientes C: %d\n", cantidad_clientes_c);

    printf("\n");
    system("pause");

    return 0;
}

void Es_Cliente_A_o_C(char zona, int *cantidad_clientes_a, int *cantidad_clientes_c){
    if(zona == 'a' || zona == 'A'){
        (*cantidad_clientes_a)++;
    }
    if(zona == 'c' || zona == 'C'){
        (*cantidad_clientes_c)++;
    }
}

float Procesar_Compras(char zona, int *total_ventas_f)
{
    float importe, importe_total = 0;

    do
    {
        printf("Ingresar valor de compra (-1 para salir): ");
        scanf("%f", &importe);
        importe_total += importe;
        if (zona == 'f' || zona == 'F')
        {
            (*total_ventas_f)++;
        }
    } while (importe != -1);

    return importe_total+1;
}

int Es_Bonificado(char zona)
{
    if (zona == 'a' || zona == 'A' || zona == 'b' || zona == 'B' || zona == 'c' || zona == 'C')
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

float Calcular_Bonificacion(char zona, float importe)
{
    if (zona == 'a' || zona == 'A' || zona == 'b' || zona == 'B')
    {
        return importe * 0.8;
    }
    else if (zona == 'c' || zona == 'C')
    {
        return importe * 0.9;
    }
    return importe;
}

int Participa_En_Sorteo(char zona)
{
    if (zona == 'd' || zona == 'D' || zona == 'e' || zona == 'E')
    {
        return 1;
    }
    else
    {
        return 0;
    }
}