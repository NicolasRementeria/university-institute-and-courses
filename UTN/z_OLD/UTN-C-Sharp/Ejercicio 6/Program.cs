using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ejercicio_6
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Title = "Ejercicio N° 6";
            /*06. Escribir un programa que determine si un año es bisiesto.  Un año es 
             * bisiesto si es múltiplo de 4. Los años múltiplos de 100 no son bisiestos, salvo 
             * si ellos también son múltiplos de 400. Por ejemplo: el año 2000 es bisiesto pero 1900 no.   
             * Nota: Utilizar estructuras repetitivas, selectivas y la función módulo (%).  */
            int añoIngresado = 0;
            Console.WriteLine("Ingrese año");
            añoIngresado = Int32.Parse(Console.ReadLine());
            if (esMultiploDe(añoIngresado, 4) && (esMultiploDe(añoIngresado, 400) || !esMultiploDe(añoIngresado, 100)))
            {
                Console.WriteLine("Es año bisiesto");
            }
            else
            {
                Console.WriteLine("No es año bisiesto");
            }
            Console.ReadKey();
        }
        static bool esMultiploDe(int numero1, int numero2)
        {
            return numero1 % numero2 == 0;
        }
    }
}
