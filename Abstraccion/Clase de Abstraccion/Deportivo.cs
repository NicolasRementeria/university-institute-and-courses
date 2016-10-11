using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Clase_de_Abstraccion
{
    public class Deportivo : Auto, IAfip
    {

        public Deportivo(string patente) : base(patente) { 
        }
        public override float CalcularCosto() // Esta llamando de vehiculo
        {
            //throw new NotImplementedException();
            return base.costo;
        }


        public float RetornarImpuesto()
        {
            return 1;
        }

        //******

        private float _impuesto = 1;
        public float Impuesto {
            get {
                return _impuesto;
            }
            set {
                _impuesto = value;
            }
        }

    }
}
