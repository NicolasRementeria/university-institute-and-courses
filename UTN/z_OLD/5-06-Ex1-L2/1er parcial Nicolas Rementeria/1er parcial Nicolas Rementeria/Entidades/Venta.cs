using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Entidades
{
    public class Venta
    {
        #region Atributos
        private Articulo _articuloVendido;
        private int _cantidad;
        #endregion

        #region Constructor
        public Venta(Articulo articuloVendido, int Cantidad) {
            this._articuloVendido = articuloVendido;
            this._cantidad = Cantidad;
        }
#endregion

        public float RetornarGanancia() {

            return this._articuloVendido.PrecioVenta * this._cantidad;
        }


    }
}
