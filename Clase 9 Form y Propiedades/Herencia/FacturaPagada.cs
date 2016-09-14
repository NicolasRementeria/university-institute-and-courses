using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Herencia
{
    public class FacturaPagada : FacturaA
    {
        public FacturaPagada(string fechaDePago, FacturaA unaFactura) : base(unaFactura.iva, unaFactura) { }

    }
}
