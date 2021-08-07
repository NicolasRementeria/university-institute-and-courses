using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Entidades
{
    public class Estante
    {
        protected sbyte _capacidad;
        protected List<Producto> _productos; //agregue static

        private Estante() {
            this._productos = new List<Producto>();
        }

        public Estante(sbyte capacidad) : this() {
            this._capacidad = capacidad;
        }

        public List<Producto> GetProductos() {
            return this._productos;
        }

        public static string MostrarEstante(Estante est) {
            Galletita auxGalletita;
            Gaseosa auxGaseosa;
            Jugo auxJugo;

            StringBuilder sb = new StringBuilder();
            sb.AppendLine("Contenido estante: ");
            sb.AppendLine("Capacidad " + est._capacidad);
            sb.AppendLine("Listado de productos: ");

            foreach (Producto prod in est.GetProductos()){
                //usar stringbuilder para guardar la info de cada producto
                if (prod is Galletita) {
                    auxGalletita = (Galletita)prod;
                    sb.AppendLine(Galletita.MostrarGalletita(auxGalletita));
                }
                if (prod is Gaseosa)
                {
                    auxGaseosa = (Gaseosa)prod;
                    sb.AppendLine(auxGaseosa.MostrarGaseosa());
                }
                if (prod is Jugo)
                {
                    auxJugo = (Jugo)prod;
                    sb.AppendLine(auxJugo.MostrarJugo());
                }
            }
            return sb.ToString();
        }

        public static bool operator ==(Estante est, Producto prod){
            foreach (Producto item in est.GetProductos()){
                if (item == prod) {
                    return true;
                }
            }
            return false;
        }

        public static bool operator !=(Estante est, Producto prod) {
            return !(est == prod);
        }

        public static bool operator +(Estante est, Producto prod) {
            if ((est.GetProductos().Count < est._capacidad) && est != prod) {
                est.GetProductos().Add(prod);
                return true;
            }
            return false;
        }


        public static Estante operator -(Estante est, Producto prod) {
            
            if (est == prod) {
                /*for (int i = 0; i < est.GetProductos().Count() || est.GetProductos()[i] == prod; i++){
                    return est.GetProductos().Remove(est.GetProductos()[i]);
                }*/
                /*for (int i = 0; i < est.GetProductos().Count(); i++){
                    est.GetProductos().RemoveAt(i);
                }*/
                est.GetProductos().Remove(prod);

            }
            return est;
        }

        public static Estante operator -(Estante est, ETipoProducto tipo) {
            /*for (int i = 0; i < est.GetProductos().Count(); i++){
               //Si el tipo del ìndice es igual al tipo recibido por parametro, sacarlo de la lista
                if (est._productos.GetType()[i] == tipo) { 
                
                }
            }*/

            for (int i = 0; i < est.GetProductos().Count; i++){
                if ((tipo == ETipoProducto.Galletita) && (est.GetProductos()[i] is Galletita)){
                    est.GetProductos().RemoveAt(i);
                }
                if ((tipo == ETipoProducto.Gaseosa) && (est.GetProductos()[i] is Gaseosa))
                {
                    est.GetProductos().RemoveAt(i);
                }
                if ((tipo == ETipoProducto.Jugo) && (est.GetProductos()[i] is Jugo))
                {
                    est.GetProductos().RemoveAt(i);
                }
                /*if ((tipo == ETipoProducto.Todos) && (est.GetProductos()[i] is Todos))
                {
                    est.GetProductos().RemoveAt(i);
                }*/
            }
            return est;
        }

        //NO ESTOY SEGURO DE CUAL GETVALORESTANTE ES EL CORRECTO
        /*public static float GetValorEstante() { 
            //Devuelve la suma de los precios del tipo dado

            float aux = 0;
            foreach (Producto item in _productos)
            {
                if (tipo == ETipoProducto.Galletita && item is Galletita)
                {
                    aux = aux + item.Precio;
                }
                if (tipo == ETipoProducto.Gaseosa && item is Gaseosa)
                {
                    aux = aux + item.Precio;
                }
                if (tipo == ETipoProducto.Jugo && item is Jugo)
                {
                    aux = aux + item.Precio;
                }
            }
            return aux = 0;
        }*/

        private float GetValorEstante()
        {
            return this.GetValorEstante(ETipoProducto.Todos);
        }

        /*public float GetValorEstante(ETipoProducto tipo) {
            float aux = 0;
            foreach (Producto item in _productos){
                if (tipo == ETipoProducto.Galletita && item is Galletita) {
                    aux = aux + item.Precio;
                }
                if (tipo == ETipoProducto.Gaseosa && item is Gaseosa)
                {
                    aux = aux + item.Precio;
                }
                if (tipo == ETipoProducto.Jugo && item is Jugo)
                {
                    aux = aux + item.Precio;
                }
            }
            return aux;
        }*/
        public float GetValorEstante(ETipoProducto tipo)
        {
            float valor = 0;
            foreach (Producto item in this.GetProductos())
            {
                switch (tipo)
                {
                    case ETipoProducto.Galletita:
                        if (item is Galletita)
                            valor += item.Precio;
                        break;
                    case ETipoProducto.Gaseosa:
                        if (item is Gaseosa)
                            valor += item.Precio;
                        break;
                    case ETipoProducto.Jugo:
                        if (item is Jugo)
                            valor += item.Precio;
                        break;
                    case ETipoProducto.Todos:
                        valor += item.Precio;
                        break;
                    default:
                        break;
                }
            }
            return valor;
        }



        /*public float ValorEstanteTotal {
            get {
                return (GetValorEstante(ETipoProducto.Galletita) + GetValorEstante(ETipoProducto.Gaseosa) + GetValorEstante(ETipoProducto.Jugo));
            }
        }*/
        public float ValorEstanteTotal
        {
            get
            {
                return this.GetValorEstante();
            }
        }

    }
}


//VER SI HACE FALTA MODIFICAR el using System.Collections.Generic POR using System.Collections;
//HACER EJERCICIO 10 CON EL MAIN DADO APARTE
