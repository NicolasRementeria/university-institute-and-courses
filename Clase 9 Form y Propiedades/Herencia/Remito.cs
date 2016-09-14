using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Herencia
{
    public class Remito : Documentos
    {
        public string fecha;

        public Remito(int numero) : base(numero) { 
            
        }

        public Remito(int numero, string fecha, int numDeControl) : base(numero, fecha, numDeControl){

        }
    }
}
