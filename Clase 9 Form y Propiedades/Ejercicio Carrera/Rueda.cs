using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ejercicio_Carrera
{
    public class Rueda
    {
        public string Marca;
        public float Tamaño;

        // el constructor no tiene retorno, no devuelve nada, ni siquiera void
        // tiene que tener el mismo nombre que la clase
        // es el valor que le pone por defecto
        // se ejecuta una unica vez y es cuando se crea el objeto

        /// <summary>
        /// Este es el constructor por defecto. Inicializa el tamaño en 0 y la marca en 'Sin marca'.
        /// </summary>
        public Rueda()
        {
            this.Marca = "Sin marca";
        }

        /// <summary>
        /// Inicializa el tamaño en 0 y la marca en el valor pasado como parámetro.
        /// </summary>
        /// <param name="marca">Marca con la que será inicializada la rueda.</param>
        public Rueda(string marca)
        {
            this.Marca = marca;
        }

        /// <summary>
        /// Inicializa la marca en 'Sin marca' y el tamaño en el valor pasado como parámetro.
        /// </summary>
        /// <param name="tamaño">Tamaño con el que será inicializada la rueda.</param>
        public Rueda(float tamaño) : this() // puedo llamar a otros constructores
        {
            this.Tamaño = tamaño;
        }

        /// <summary>
        /// Inicializa la marca y el tamaño en los valores pasados como parámetro.
        /// </summary>
        /// <param name="marca">Marca con la que será inicializada la rueda.</param>
        /// <param name="tamaño">Tamaño con el que será inicializada la rueda.</param>
        public Rueda(string marca, float tamaño) : this(tamaño)
        {
            this.Marca = marca;
        }

        /// <summary>
        /// 
        /// </summary>
        /// <param name="tamaño"></param>
        /// <param name="marca"></param>
        public Rueda(float tamaño, string marca) : this(marca, tamaño)
        {

        }

        public void MostrarRueda()
        {
            Console.WriteLine("El tamaño es {0:#,###.00}", this.Tamaño);
        }
    }
}
