using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ejercicio_3
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Title = "Ejercicio N° 3";
            /*03. Mostrar por pantalla todos los números primos que haya hasta el número que ingrese el usuario por consola.  
                  Nota: Utilizar estructuras repetitivas, selectivas y la función módulo (%).*/
            int numero;
            Console.WriteLine("Ingrese número.");
            numero = Int32.Parse(Console.ReadLine());
            Console.WriteLine("Los números primos son:");
            for (int i = 1; i <= numero; i++)
            {
                if (esNumeroPrimo(i))
                {
                    Console.WriteLine("{0}", i);
                }
            }
            Console.ReadKey();

        }
        public static bool esNumeroPrimo(int numero)
        {
            int a = 0, i;
            for (i = 1; i < (numero + 1); i++)
            {
                if (numero % i == 0)
                {
                    a++;
                }
            }
            if (a != 2)
            {
                return (false);
            }
            else
            {
                return (true);
            }
        }
    }
}