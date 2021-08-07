using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            /*Lograr que funcione:
             
             * Producto prod1 = (Producto) 33;
             * int resultado;
             * resultado = prod1 + prod1;
             */

            Producto prod1 = (Producto)33;
              int resultado;
             resultado = prod1 + prod1;


             Console.WriteLine("La suma del producto es {0}", resultado);
             Console.ReadKey();

            /*Dolar und;
              Pesos unp;
              und = 1;
              unp = (Pesos)1;
              und = und + unp;
              unp = unp + und;*/
             Dolar und;
             Peso unp;
             und = 1;
             unp = (Peso)1;
             und = und + unp;
             unp = unp + und;
             Console.WriteLine("La suma dolar mas peso es {0}", und); // quiza falte sobrecargarlo
             Console.WriteLine("La suma peso mas dolar es {0}", unp);
             Console.ReadKey();

        }
    }
}
