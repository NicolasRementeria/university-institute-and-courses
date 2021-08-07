using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication2
{
    class Program
    {
        static void Main(string[] args)
        {
            eFabricante fabricante;
            fabricante = eFabricante.Honda;

            Rueda otraRueda = new Rueda("Firestone"); // < Sobrecarga de un segundo constructor con parametro
            Rueda otraRueda2 = new Rueda(25); // < Sobrecarga de constructor que pide un int que va a ser tamaño
            Rueda otraRueda3 = new Rueda("Skylake", 19); // Sobrecarga de constructor que pide marca y tamaño
            Rueda otraRueda4 = new Rueda(99, "Rueda de camion"); // Sobrecarga de constructor que pide tamaño y marca
            Rueda otraRueda5 = new Rueda(50);

            Carrera race = new Carrera();

            Console.WriteLine(fabricante); // VA A MOSTRAR "HONDA"

            fabricante = (eFabricante)1; // castear para forzar el dato, va a mostrar Chevrolet que es el dato 1
            Console.WriteLine(fabricante); // VA A MOSTRAR "CHEVROLET"




            /*Rueda nuevaRueda;
            nuevaRueda = new Rueda();*/

            Rueda nuevaRueda = new Rueda();
            Auto nuevoAuto1 = new Auto();
            Auto nuevoAuto2 = new Auto();
            Auto nuevoAuto3 = new Auto();
            Auto nuevoAuto4 = new Auto();

            // Console.WriteLine("{0}", );

            race.mostrarCarrera();
            Console.ReadKey();


            Tiempo t1 = new Tiempo(5);
            Tiempo result = Tiempo.sumar(t1, 10);


            t1 = t1 + 10; // Sobrecarga de operador + para sumar un tiempo

        }
    }
}
