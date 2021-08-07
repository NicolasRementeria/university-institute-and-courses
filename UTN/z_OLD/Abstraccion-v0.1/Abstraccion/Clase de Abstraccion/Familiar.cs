using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Clase_de_Abstraccion
{
    public class Familiar : Auto
    {
        public Familiar(string patente) : base(patente){ }
        public override float CalcularCosto()
        {
            //throw new NotImplementedException();
            return base.costo;
        }
    }
}
