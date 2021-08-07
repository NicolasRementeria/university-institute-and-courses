using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication2
{
    public class Auto
    {
        //LA CLASE AUTO ESTÀ COMPUESTA POR LA CLASE RUEDA

        private eFabricante Fabricante; // Era publico, le puse privado
        private static Random marcaCualquiera = new Random();
        public Rueda DI;
        public Rueda DD;
        public Rueda TI;
        public Rueda TD;
        public static int contadorDeObjetos;
        private Kilometro kilometrosRecorridos; // No es necesario inicializar en el constructor porque se sabe q inicia de 0
        private Tiempo tiempoDemorado;


        public Auto()
        { // << Constructor
            this.Fabricante = (eFabricante)(marcaCualquiera.Next(0, 3)); // < INICIALIZACION ALEATORIAS

            this.DI = new Rueda();
            this.DD = new Rueda();
            this.TI = new Rueda();
            this.TD = new Rueda();

            Auto.contadorDeObjetos++;

        }
        /* Generar un constructor que reciba un fabricante, pero heredarlo de auto(), para no pasar por otro lugar
           en el contador de objetos */

        public void volverACero()
        {
            this.kilometrosRecorridos = 0;
            this.tiempoDemorado = 0;
        }

        //Deprecated por sobrecarga de metodos
        /*public void agregarKilometros(int kilometros)
        {
            this.kilometrosRecorridos += kilometros;
        }
        public void agregarTiempo(int tiempo)
        {
            this.tiempoDemorado += tiempo;
        }
        // NO se puede escribir this. en un metodo estatico, es solo para instancias*/


        public static bool compararAuto(Auto auto1, Auto auto2)
        {
            if (auto1.Fabricante == auto2.Fabricante)
                return true;
            return false;
        }


        /*public static Auto() { 
            // UN CONSTRUCTOR ESTATICO NO TIENE ACCESO A MODIFICADORES
           // ADENTRO DE CONSTRUCTOR ESTATICO PODEMOS HACER LO QUE QUERAMOS CON ATRIBUTOS ESTATICOS
        }*/

        static Auto()
        {
            Auto.contadorDeObjetos = 0;
        }

        public void mostrarAuto()
        {
            Console.WriteLine("Fabricante es: {0}", this.Fabricante);
        }

        // CLASE 5

        public Tiempo Agregar(Tiempo tiempo) {
            return this.tiempoDemorado = this.tiempoDemorado + tiempo;
        }

        public Kilometro Agregar(Kilometro kilometro){
            return this.kilometrosRecorridos = this.kilometrosRecorridos + kilometro;
        }



    }
}
