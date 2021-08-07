using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CentralitaHerencia
{
    public class Centralita
    {
        private List<Llamada> _listaDeLlamadas;
        protected string _razonSocial;

        #region Propiedades
        public float GananciaPorLocal {
            get {
                return this.CalcularGanancia(TipoLlamada.Local);
            }
        }

        public float GananciaPorProvincial{
            get{
                return this.CalcularGanancia(TipoLlamada.Local);
            }
        }

        public float GananciaTotal{
            get{
                return this.CalcularGanancia(TipoLlamada.Todas);
            }
        }

        public List<Llamada> Llamadas {
            get {
                return this._listaDeLlamadas;
            }
        }
        #endregion

        #region Constructores
        public Centralita() {
            this._listaDeLlamadas = new List<Llamada>();
            this._razonSocial = "Sin razon social";
        }
        public Centralita(string nombreEmpresa) : this(){
            //hereda del constructor sin parametros
            this._razonSocial = nombreEmpresa;
        }
        #endregion

        #region Funciones
        private float CalcularGanancia(TipoLlamada tipo)
        {
            return 0; //
        }

        public void Mostrar() {
            //
        }

        public void OrdenarLlamadas() {
            //Ordenar las llamadas por duracion
        }
        #endregion
    }
}
