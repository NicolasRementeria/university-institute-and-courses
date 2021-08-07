using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ejercicio_2
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Title = "Ejercicio N° 2";
            /*02. Ingresar un número y mostrar: el cuadrado y el cubo del mismo. 
             *    Se debe validar que el número sea mayor que cero, caso contrario, mostrar el mensaje: "ERROR. Reingresar número!!!". 
                  Nota: Utilizar el método ‘Pow’ de la clase Math para realizar la operación.*/

            int numero;
            Console.WriteLine("Ingresar número mayor a cero");
            numero = Convert.ToInt32(Console.ReadLine()); ;
            while (numero <= 0)
            {
                Console.WriteLine("ERROR. Reingresar número!!!");
                numero = Convert.ToInt32(Console.ReadLine()); ;
            }
            Console.WriteLine("Cuadrado: {0}\nCubo: {1}", (long)Math.Pow(numero, 2), (long)Math.Pow(numero, 3));
            Console.ReadKey();
        }
    }
}
