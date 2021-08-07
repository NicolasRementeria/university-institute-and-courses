using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ejercicio_1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Title = "Ejercicio N° 1";
            /*01. Ingresar 5 números por consola, guardándolos en una variable escalar. 
             *    Luego calcular y  mostrar: el valor máximo, el valor mínimo y el promedio. */

            int[] Vector = new int[5];
            int Promedio = 0;
            Console.Write("Ingrese 5 valores numericos \n");
            for (int i = 0; i < Vector.Length; i++)
            {
                Vector[i] = Convert.ToInt32(Console.ReadLine());
            }
            int Maximo = Vector[0];
            int Minimo = Vector[0];


            Console.WriteLine("Los valores ingresados son: {0}, {1}, {2}, {3}, {4}", Vector[0], Vector[1], Vector[2], Vector[3], Vector[4]);
            Console.ReadKey();

            for (int i = 0; i < Vector.Length; i++)
            {
                if (Vector[i] < Minimo)
                {
                    Minimo = Vector[i];
                }
                if (Vector[i] > Maximo)
                {
                    Maximo = Vector[i];
                }
                Promedio = Promedio + Vector[i];
            }
            Promedio = Promedio / 5;
            Console.WriteLine("Minimo: {0} \n Maximo: {1} \n Promedio: {2}", Minimo, Maximo, Promedio);
            Console.ReadKey();

        }
    }
}
