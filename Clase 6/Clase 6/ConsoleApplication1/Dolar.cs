using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    public class Dolar
    {
        private float _cantidad;

        private Dolar(float cantidad) {
            this._cantidad = cantidad;
        }

        public static Dolar operator +(Dolar dolar, Peso peso){
            return (Dolar)(dolar._cantidad + ((Dolar)peso)._cantidad);
        }

        public static implicit operator Dolar(int numero) {
            return new Dolar(numero);
        }

        public static implicit operator Peso(Dolar numero) {
            return (Peso)(numero._cantidad / 15);
        }



    }
}
