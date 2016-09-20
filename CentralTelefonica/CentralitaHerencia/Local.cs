using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CentralitaHerencia
{
    public class Local : Llamada
    {
        #region Atributos
        protected float _costo;
        #endregion

        #region Propiedades
        public float CostoLlamada {
            get {
                //return this._costo;
                return CalcularCosto();
            }
        }
        #endregion

        #region Funciones
        private float CalcularCosto() {
            return this._costo * this._duracion; 
        }

        public void Mostrar() {
            //
        }
        #endregion

        public Local(string origen, float duracion, string destino, float costo) : base(origen, destino, costo){
            this._costo = costo;
        }

        public Local(Llamada unaLlamada, float costo) : this(unaLlamada.NroOrigen, unaLlamada.Duracion, unaLlamada.NroDestino, costo) {

        }
    }
}
