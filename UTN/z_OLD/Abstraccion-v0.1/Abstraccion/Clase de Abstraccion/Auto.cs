using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Clase_de_Abstraccion
{
    public abstract class Auto : Vehiculo
    {
        public Auto(string patente) : base(patente){}
        //***
        public Auto(float costo) : base(costo) { }
        //***

        public int cantidadDePuertas;

        /* Quito el constructor porque Auto es abstracto
         * public Auto(string patente) : base(patente) { 
            
        }*/

        public override string MostrarDatos()
        {
            //return base.MostrarPatente() + base.cantidadDePuertas.ToString();
            StringBuilder sb = new StringBuilder();
            sb.AppendLine(base.MostrarDatos());
            sb.AppendLine("Auto");
            sb.AppendLine(this.cantidadDePuertas.ToString());
            return sb.ToString();
        }

        

    }
}
