using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Clase_de_Abstraccion
{
    public class Avion : Vehiculo, IAfip
    {
        public Avion(string patente) : base(patente){ 
        
        }

        public override float CalcularCosto()
        {
            //throw new NotImplementedException();
            return base.costo;
        }



        public float RetornarImpuesto()
        {
            //throw new NotImplementedException();
            return Impuesto;
        }

        private float _impuesto = 2;
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
