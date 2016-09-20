using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CentralitaHerencia
{
    public class Provincial : Llamada
    {
        #region Atributos
        protected Franja _franjaHoraria;
        #endregion

        #region Propiedades
        public float CostoLlamada {
            get {
                return this.CalcularCosto();
            }
        }
        #endregion

        #region Constructores
        /*public Provincial(Franja miFranja, Llamada unaLlamada){
            this._franjaHoraria = miFranja;
            this._
        }*/

        public Provincial(string origen, Franja miFranja, float duracion, string destino) : base (origen, destino, duracion){
            //Utiliza los parametros de Llamada
            this._franjaHoraria = miFranja;
        }

        public Provincial(Franja miFranja, Llamada unaLlamada) : this(unaLlamada.NroOrigen, miFranja, unaLlamada.Duracion, unaLlamada.NroDestino){
            //Le paso los parametros de la Llamada

        }
        #endregion

        #region Funciones
        private float CalcularCosto() {
            return 0; //
        }

        public void Mostrar() {
            //
        }
        #endregion
    }
}
