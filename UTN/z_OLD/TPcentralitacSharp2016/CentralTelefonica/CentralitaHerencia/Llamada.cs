using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CentralitaHerencia
{
    public class Llamada
    {
        #region Atributos y Propiedades
        protected float _duracion;
        public float Duracion {
            get {
                return this._duracion;
            }
        }

        protected string _nroDestino;
        public string NroDestino {
            get {
                return this._nroDestino;
            }
        }

        protected string _nroOrigen;
        public string NroOrigen {
            get {
                return this._nroOrigen;
            }
        }
        #endregion

        #region Constructor
        public Llamada(string origen, string destino, float duracion) {
            this._duracion = duracion;
            this._nroDestino = destino;
            this._nroOrigen = origen;
        }
        #endregion

        #region Funciones
        public int OrdenarPorDuracion(Llamada uno, Llamada dos) {
            return 0; //
        }

        public void Mostrar() {
            //
        }

        #endregion
    }
}
