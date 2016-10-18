using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Excepcion_basica
{
    public class MiExcepcion : Exception // Clase que hereda de Exception
    {
        public DateTime horaDeLaExepcion;
        public string textoHoraDeLaExcepcion;

        public MiExcepcion(string Mensaje, DateTime fecha) : base(Mensaje)
        {
            this.horaDeLaExepcion = fecha;
            //this.textoHoraDeLaExcepcion = Mensaje;
            this.textoHoraDeLaExcepcion = horaDeLaExepcion.ToString();

        }
        
        public MiExcepcion(string Mensaje, DateTime fecha, Exception excepAnterior) : this(Mensaje, fecha) {
            //Fijarse como usar innerException con excepAnterior
            
        }




    }
}
