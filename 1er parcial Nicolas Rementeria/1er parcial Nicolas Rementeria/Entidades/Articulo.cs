using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Entidades
{
    public class Articulo
    {
        private int _codigo;
        private string _nombre;
        private float _precioCosto;
        private float _precioVenta;
        private int _stock;

        public string NombreYCodigo {
            get { 
                return (this._nombre + this._codigo);
            }
        }

        public float PrecioCosto {
            set {
                float precioCosto = this._precioCosto;
                float precioVenta = (30 * precioCosto)/100 + precioCosto;
                

            }
        }

        public float PrecioVenta {
            get {
                return this._precioVenta;
            }
        }

        public int Stock {
            set {
                int stock = this._stock;
            }
        }

        public Articulo(int codigo, string nombre, float precioCosto, int cantidad) {
            this._codigo = codigo;
            this._nombre = nombre;
            this._precioCosto = precioCosto;
            this._precioVenta = PrecioVenta;
        }

        public bool HayStock(int cantidad) { 
            if(Stock >= cantidad){
                return true;
            }
            return false;
        }

        public static bool operator ==(Articulo articuloUno, Articulo articuloDos){
            if(articuloUno.NombreYCodigo == articuloDos.NombreYCodigo){
                return true;
            }
            return false;
        }

        public static bool operator !=(Articulo articuloUno, Articulo articuloDos){
            return !(articuloUno == articuloDos);
        }

        public static int operator +(Articulo articuloUno, Articulo articuloDos){
            return articuloUno.Stock + articuloDos.Stock;
        }

        public static int operator -(Articulo articuloUno, int cantidad){
            return articuloUno.Stock - cantidad;
        }



    }
}
