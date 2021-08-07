using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ejercicio_4
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Title = "Ejercicio N° 4";
            /*04. Un número perfecto es un entero positivo, que es igual a la suma de todos 
             * los enteros positivos (excluido el mismo) que son divisores del número.  El primer número perfecto es 6, 
             * ya que los divisores de 6 son 1, 2 y 3; y 1 + 2 + 3 = 6.  Escribir una aplicación que encuentre los 4 
             * primeros números perfectos.   Nota: Utilizar estructuras repetitivas, selectivas y la función módulo (%). */
            int cantidad = 0;
            for (int i = 1; cantidad < 4; i++)
            {
                if (esNumeroPerfecto(i))
                {
                    cantidad++;
                    Console.WriteLine("Numero Perfecto {0}: {1}", cantidad, i);
                }
            }
            Console.ReadKey();
        }



        static bool esNumeroPerfecto(int numero)
        {
            if (sumaDeLosDivisores(numero) == numero)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        static int sumaDeLosDivisores(int numero)
        {
            int suma = 0;
            for (int i = 1; i < numero; i++)
            {
                if (numero % i == 0)
                {
                    suma = suma + i;
                }
            }
            return suma;

        }
    }
}
