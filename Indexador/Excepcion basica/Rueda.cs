using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Excepcion_basica
{
    public class Rueda
    {
        public string marca;

        public Rueda(string Marca) {
            this.marca = Marca;
        }

        public void Pinchar() { 
            //Lanza excepcion "pichadura exception"
            throw new PinchaduraException("Fallo por pinchadura", DateTime.Today, this.marca);
        }

        static Rueda() {
            //inicializar el numero random
            //Random numeroRandom = new Random();
        }

        static Random numeroRandom = new Random();
        public void Rodar() {
            //Random de 1 a 10, si es = 5 pincha, de lo contrario muestra el numero random por consola
            //Revisar, porque asi escrito solo genera un random aparentemente; quizas crearlo en un static
            //Random numeroRandom = new Random();
            int aux = numeroRandom.Next(1, 10);
            if (aux == 5)
                this.Pinchar();
            else
                Console.WriteLine("Numero " + aux);

        }



    }
}
