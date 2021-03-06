using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Clase_de_Abstraccion
{
    class Program
    {
        static void Main(string[] args)
        {
            /*Vehiculo vehiculo = new Vehiculo("patente de prueba");

            Console.WriteLine(vehiculo);
            Console.ReadKey();*/

            Carreta Carreta1 = new Carreta("5"); // deberian recibir todos patente
            Avion Avion1 = new Avion("1500");
            Familiar AutoFamiliar = new Familiar("100");
            Deportivo Deportivo1 = new Deportivo(150); // << Al estar sobrecargado en float costo, 150 es el valor del deportivo
            List<Vehiculo> listaVehiculos = new List<Vehiculo>();
            listaVehiculos.Add(Avion1);
            listaVehiculos.Add(AutoFamiliar);
            listaVehiculos.Add(Carreta1);
            listaVehiculos.Add(Deportivo1);

            foreach (Vehiculo item in listaVehiculos)
            {
                Console.WriteLine(item.CalcularCosto()); // << Al no estar la sobrecarga del costo en cada elemento ingresado, muestra 0 en todos los casos excepto en Deportivo, 150
            }

            Console.WriteLine(Deportivo1.CalcularCosto());

            List<IAfip> listaIAfip = new List<IAfip>();
            listaIAfip.Add(Deportivo1);
            listaIAfip.Add(Avion1);
            foreach (IAfip item in listaIAfip)
            {
                item.RetornarImpuesto();
                Console.WriteLine("objeto" + item.GetType().ToString() + "\nimpuesto " + item.Impuesto.ToString());
                //ver mejor manera de mostrar el tipo del objeto
            }

            Console.ReadKey();
        }
    }
}
