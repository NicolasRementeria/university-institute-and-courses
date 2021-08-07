using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication2
{
    public class Carrera
    {
        Auto auto1;
        Auto auto2;
        Auto auto3;
        Auto auto4;
        Auto auto5;
        Auto auto6;
        private static Random randomKilometros;

        public Carrera()
        {
            this.auto1 = new Auto();
            this.auto2 = new Auto();
            this.auto3 = new Auto();
            this.auto4 = new Auto();
            this.auto5 = new Auto();
            this.auto6 = new Auto();
            randomKilometros = new Random();
        }


        public void mostrarCarrera()
        {
            /* Console.WriteLine("Auto 1: {0}", this.auto1);
             Console.WriteLine("Auto 2: {0}", this.auto2);
             Console.WriteLine("Auto 3: {0}", this.auto3);
             Console.WriteLine("Auto 4: {0}", this.auto4);
             Console.WriteLine("Auto 5: {0}", this.auto5);
             Console.WriteLine("Auto 6: {0}", this.auto6);
             Console.ReadKey();*/

            this.auto1.mostrarAuto();
            this.auto2.mostrarAuto();
            this.auto3.mostrarAuto();
            this.auto4.mostrarAuto();
            this.auto5.mostrarAuto();
            this.auto6.mostrarAuto();


            return;
        }
        public void porTiempo(int minutos)
        {
            /* ingresar un tiempo en minutos, un entero, por cada minuto hace una vuelta de for o while
             * Los autos, por c/u de las vueltas, incremente una cantidad de km random entre 10 y 100
             * al terminar las vueltas, hay que ver que auto sumò mas kilòmetros */

            for (int contadorDeVueltas = 0; contadorDeVueltas < minutos; contadorDeVueltas++)
            {
                this.auto1.agregarKilometros(randomKilometros.Next(10, 100));
                this.auto2.agregarKilometros(randomKilometros.Next(10, 100));
                this.auto3.agregarKilometros(randomKilometros.Next(10, 100));
                this.auto4.agregarKilometros(randomKilometros.Next(10, 100));
                this.auto5.agregarKilometros(randomKilometros.Next(10, 100));
                this.auto6.agregarKilometros(randomKilometros.Next(10, 100));
            }
            /* Luego de recorrer las vueltas, hacer una estructura de if de comparacion entre los campos 
             * kilometrosRecorridos de cada auto y mostrar el auto que mas recorrió y cuantos km, 
             * y el que menos recorriò y cuantos km. */
        }
        public void correrCarrera()
        {
            // necesita dos sobrecargas, una tiempo y otra km

        }
        public void correrCarrera(Tiempo tiempo)
        {
            // Metodo que muestra quien ganò, recibiendo tiempo

        }
        public void correrCarrera(Kilometro kilometro)
        {
            // // Metodo que muestra quien ganò, recibiendo kilometro

        }

    }
}


/* Tipo de dato "enumerado". 
 * 
 * BUSCAR LIBRO "C# AL DESCUBIERTO"
 * 
 
 */

//EJERCICIO PARA HACER
