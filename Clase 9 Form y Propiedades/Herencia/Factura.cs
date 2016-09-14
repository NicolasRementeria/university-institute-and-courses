using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Herencia
{
    public class Factura : Documentos
    {
        public float importe;

        public Factura(int numero) : base(numero) { 
        
        }

        public Factura(int numero, string fecha, int numDeControl) : base(numero, fecha, numDeControl){

        }
    }
}
