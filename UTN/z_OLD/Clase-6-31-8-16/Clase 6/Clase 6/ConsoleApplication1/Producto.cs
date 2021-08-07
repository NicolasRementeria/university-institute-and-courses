using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    public class Producto
    {
        private int _cantidad;

        private Producto(int cantidad) {
            this._cantidad = cantidad;
        }

        /*public static Producto operator +(Producto productoAux, int valor){
            productoAux._cantidad = productoAux._cantidad + valor;
            return productoAux;
        }*/

        public static Producto operator +(Producto prod1, Producto prod2) { 
            return (prod1._cantidad + prod2._cantidad);
        }

        public static implicit operator Producto(int numero){
            return new Producto(numero);
        }

        public static implicit operator int(Producto producto)
        {
            return producto._cantidad;
        }
    }
}
