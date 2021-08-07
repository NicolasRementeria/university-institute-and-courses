using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Excepcion_basica
{
    public class PinchaduraException : MiExcepcion
    {

        public PinchaduraException(string Mensaje, DateTime fecha, string Marca) : base(Mensaje, fecha){
            string marca = Marca; //se crea dentro del constructor

        }

    }
}
