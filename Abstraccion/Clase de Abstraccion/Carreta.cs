using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Clase_de_Abstraccion
{
    public class Carreta : Vehiculo
    {
        public Carreta(string patente) : base(patente) { 
        
        }

        /*public abstract float CalcularCosto()
        {


            return 1;
        }*/

        /*public Carreta() : base(patente){ 
         
        }*/
        //Hacer constructores 

        public override float CalcularCosto()
        {
            //throw new NotImplementedException();
            return base.costo;
        }

    }
}
