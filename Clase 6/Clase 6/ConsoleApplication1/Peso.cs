using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    public class Peso
    {
        private float _cantidad;

        private Peso(float cantidad) {
            this._cantidad = cantidad;
        }

        public static Peso operator +(Peso peso, Dolar dolar){
            return (Peso)(peso._cantidad + ((Peso)dolar)._cantidad);
        }

        public static implicit operator Peso(int numero){
            return new Peso(numero);
        }
        public static implicit operator Dolar(Peso numero){
            return (Dolar)(numero._cantidad * 15);
        }



    }
}
