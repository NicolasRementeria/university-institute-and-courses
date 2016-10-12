using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab_2_Indexador
{
    public class PC
    {
        public string marca;
        public string SO;
        public static int contadorPC; // Va a ser estatico
        public int numero;

        private PC(string marcaDada) { //<< era publico, lo hice privado
            this.marca = marcaDada;
            this.SO = "Windows";
            this.numero = contadorPC;
            contadorPC = contadorPC + 1;
        }

        static PC() { // Es estatico este constructor?
            contadorPC = 1;
        }

        /*public PC(string marcaDada, string SODado)
            : this(marcaDada)
        {
            this.SO = SODado;
        }*/

        public static implicit operator PC(string marca){
            return new PC(marca);
        }

        /*private PC(string marcaDada){
            this.marca = marcaDada;
            this.SO = "Windows";
        }*/





    }
}
