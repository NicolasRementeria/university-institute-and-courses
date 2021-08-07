using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ejercicio_5
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Title = "Ejercicio N° 5";
            /*05. Un centro numérico es un número que separa una lista de números enteros 
             * (comenzando en 1) en dos grupos de números, cuyas sumas son iguales.  El primer 
             * centro numérico es el 6, el cual separa la lista (1 a 8) en los grupos: (1; 2; 3; 4; 5) 
             * y (7; 8) cuyas sumas son ambas iguales a 15. El segundo centro numérico es el 35, el 
             * cual separa la lista (1 a 49) en los grupos: (1 a 34) y (36 a 49) cuyas sumas son ambas 
             * iguales a 595.  Se pide elaborar una aplicación que calcule los centros numéricos entre 
             * 1 y el número que el usuario ingrese por consola.  
             * Nota: Utilizar estructuras repetitivas, selectivas y la función módulo (%). */

            int numero;
            Console.WriteLine("Ingrese número mayor a 0");
            numero = Int32.Parse(Console.ReadLine());
            for (int i = 1; i <= numero; i++)
            {
                Console.WriteLine("Centro numérico: {0}", centroNumérico(i));
            }
            Console.ReadKey();
        }
        public static int centroNumérico(int numero)
        {
            int sumaPosteriores = 0;
            for (int i = numero + 1; i <= sumaAnteriores(numero); i++)
            {
                if (sumaPosteriores == sumaAnteriores(numero) || sumaPosteriores > sumaAnteriores(numero))
                {
                    break;
                }
                sumaPosteriores = sumaPosteriores + i;
            }
            if (sumaAnteriores(numero) == sumaPosteriores)
            {
                return numero;
            }
            return 1;

        }

        public static int sumaAnteriores(int numero)
        {
            int suma = 0;
            for (int i = 1; i < numero; i++)
            {
                suma = suma + i;
            }
            return suma;
        }
    }
}

// FUNCIONA BIEN PERO HAY QUE ARREGLAR AGREGANDO UNA FUNCION "ES CENTRO NUMERICO" PARA QUE VALIDE Y NO SPAMEE LOS 1 DE RETURN


/*            // Variables
            double aumento = 1,
                numero,
                i,
                j,
                sumaAtras,
                sumaAdelante;
 
            // Ingreso de datos
            Console.Write("Ingrese un numero (ejemplo: 10000): ");
            numero = double.Parse(Console.ReadLine());
 
            // Comienzo del programa
            while (aumento < numero){
 
                aumento++;
                sumaAtras = 0;
                sumaAdelante = 0;
 
                // Calculo para atras
                for (i = 1; i < aumento; i++){
                    sumaAtras = sumaAtras + i;
                }
                //calculo para adelante
                for (j = aumento + 1; j <= sumaAtras; j++){
                    if ((sumaAdelante == sumaAtras)||(sumaAdelante > sumaAtras))
                        break;
                    sumaAdelante = sumaAdelante + j;
                }
 
                // Mostrando en pantalla
                if (sumaAtras == sumaAdelante)
                Console.WriteLine("Es centro numerico: {0}", aumento);
            }
            Console.ReadLine();*/
