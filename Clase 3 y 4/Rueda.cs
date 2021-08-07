using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication2
{
    public class Rueda
    {
        public string Marca;
        public float Tamanio;
        //constructor por defecto, debe llevar el nombre de la clase
        //constructor solo se puede ejecutar UNA vez por objeto, que es cuando ejecuta el objeto
        //metodos se pueden ejecutar mas de una vez en una misma instancia

        /// <summary>
        /// Este es el constructor por defecto, va a inicializar tamaño en 0 y marca en "sin marca"
        /// </summary>
        public Rueda()
        {

            this.Marca = "Sin Marca";
        }
        /// <summary>
        /// Este es el constructor que inicializa Marca con el parametro que me pasan por string
        /// </summary>
        /// <param name="marca"></param>
        public Rueda(string marca)
        { // Sobrecarga de constructor

            this.Marca = marca;
        }

        /// <summary>
        /// Este es el constructor que inicializa tamaño en tamanio dado por un int
        /// </summary>
        /// <param name="tamaño"></param>
        public Rueda(int tamaño) : this()
        { // Està llamando al constructor por defecto para asignar marca a Sin Marca
          /*this.Marca = "Sin marca";  Està mal forzada la inicializacion de este caso */

            this.Tamanio = tamaño;
        }

        /// <summary>
        /// Este es el contructor que inicializa tamaño por tamaño dado, y marca por marca dada
        /// </summary>
        /// <param name="marca"></param>
        /// <param name="tamaño"></param>
        public Rueda(string marca, int tamaño) : this(tamaño)
        { // 
            this.Marca = marca;
        }

        /// <summary>
        /// Este es el contructor que inicializa tamaño por tamaño dado, y marca por marca dada
        /// Se ingresan de forma inversa al constructor anterior, para lograr el funcionamiento total
        /// </summary>
        /// <param name="tamaño"></param>
        /// <param name="marca"></param>
        public Rueda(int tamaño, string marca) : this(marca, tamaño)
        { // EL ULTIMO CONSTRUCTOR DEBE QUEDAR VACIO
        }


        public void mostrarAuto()
        {
            Console.WriteLine("Tamaño de la Rueda: {0:#,###.00}", this.Tamanio);
        }

    }
}

