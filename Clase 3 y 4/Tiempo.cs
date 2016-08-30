using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication2
{
    class Tiempo
    {
        public int Cantidad;

        public Tiempo(int cantidad)
        { // Constructor de Tiempo
            this.Cantidad = cantidad;
        }

        public static Tiempo sumar(Tiempo tiempoAux, int valor)
        { // intento sobrecargar el operador + pero no es la manera

            tiempoAux.Cantidad = tiempoAux.Cantidad + valor;

            return tiempoAux;
        }

        public static Tiempo operator +(Tiempo tiempoAux, int valor)
        { // intento sobrecargar el operador + pero no es la manera

            tiempoAux.Cantidad = tiempoAux.Cantidad + valor;

            return tiempoAux;
        }
    }

}