using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Entidades
{
    public class Producto
    {

        protected int _codigoBarra;

        protected EMarcaProducto _marca;
        public EMarcaProducto Marca
        {
            get
            {
                return _marca;
            }
        }

        protected float _precio;
        public float Precio {
            get {
                return _precio;
            }
        }


        public Producto(int codigo, EMarcaProducto marca, float precio) {
            this._codigoBarra = codigo;
            this._marca = marca;
            this._precio = precio;
        }

        protected static string MostrarProducto(Producto prod){ //o public string
            return("Marca: " + prod.Marca + "Precio: " + prod.Precio + "Codigo de barra: " + (int)prod);
        }

        // EJERCICIO 2
        public static bool operator ==(Producto prodUno, Producto prodDos) {
            if(prodUno._marca == prodDos._marca && prodUno._codigoBarra == prodDos._codigoBarra){
                return true;
            }
            return false;
        }

        public static bool operator !=(Producto prodUno, Producto prodDos) { 
            return !(prodUno == prodDos);
        }

        public static bool operator ==(Producto prodUno, EMarcaProducto marca){
            if (prodUno._marca == marca) {
                return true;
            }
            return false;
        }

        public static bool operator !=(Producto prodUno, EMarcaProducto marca) {
            return !(prodUno == marca);
        }

        public static explicit operator int(Producto prod){
            return prod._codigoBarra;
        }



    }
}
