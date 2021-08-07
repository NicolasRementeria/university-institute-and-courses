using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Herencia
{
    public class Documentos
    {
        public int numero;
        //protected string _fecha;
        public string _fecha;
        //private int _numeroDeControl;
        public int _numeroDeControl;

        public void Mostrar() {
            Console.Write(this.numero);
        }

        public Documentos(int numero) {  //CONSTRUCTOR
            
        }

        public Documentos(int numero, string fecha, int numDeControl) : this(numero){ 
            
        }

    }
}
