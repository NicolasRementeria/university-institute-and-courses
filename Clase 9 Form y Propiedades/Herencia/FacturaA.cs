using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Herencia
{
    public class FacturaA : Factura
    {
        public int iva;
        
        public FacturaA(int iva, Factura unaFactura) : base(unaFactura.numero, unaFactura._fecha, unaFactura._numeroDeControl){
            this.iva = iva; // ??
        }
    }
}
