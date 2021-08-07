using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Excepcion_basica
{
    public class AutoException : MiExcepcion
    {
        public AutoException(string Mensaje, DateTime fecha, Auto auto) : base(Mensaje, fecha) {
            Auto autoaux = auto;
        }

    }
}
