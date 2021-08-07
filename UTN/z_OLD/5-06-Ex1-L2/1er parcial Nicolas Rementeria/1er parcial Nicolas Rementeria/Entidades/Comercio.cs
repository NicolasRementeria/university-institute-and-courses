using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Entidades
{
    public class Comercio
    {
        #region atributos
        private string _dueño;
        private List<Articulo> _misArticulos;
        private List<Venta> _misVentas;
        #endregion

        #region Constructor
        public Comercio(string dueño){
            this._dueño = dueño;
            this._misArticulos = new List<Articulo>();
            this._misVentas = new List<Venta>();
        }
        #endregion

        public static void MostrarArticulos(Comercio ComercioAMostrar){
            foreach (Articulo item in ComercioAMostrar._misArticulos)
            {
                Console.WriteLine(item.NombreYCodigo);
            }
        }

        public static void MostrarGanancia(Comercio ComercioParaResumen){
            double ganancia = 0;
            foreach (Venta item in ComercioParaResumen._misVentas)
            {
                ganancia += item.RetornarGanancia();
            }
            Console.WriteLine(ganancia);
        }

        public void ComprarArticulo(Articulo articuloComprado){
            //Si el articulo ya existe, sumas el stock, de lo contrario se agrega a la lista de articulos
            foreach (Articulo item in this._misArticulos)
            {
                if (item == articuloComprado)
                {
                    item.Stock = item + articuloComprado;
                }
            }
            this._misArticulos.Add(articuloComprado);
        }

        public void VenderArticulo(Articulo articuloSolicitado, int cantidad){
            foreach (Articulo item in this._misArticulos)
            {
                if (item == articuloSolicitado && item.HayStock(cantidad))
                {
                    item.Stock = item - cantidad;
                    this._misVentas.Add(new Venta(articuloSolicitado, cantidad));
                }
            }
        }
    }
}
