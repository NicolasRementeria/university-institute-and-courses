using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Clase_de_Abstraccion
{
    public abstract class Vehiculo
    {
        public string patente;
        public float costo;

        //clases abstractas no deberian tener constructor?
        public Vehiculo(string patente1) {
            this.patente = patente1;
        }
        //CREADO POR MI, NO DADO POR CLASE
        public Vehiculo(float costo1) {
            this.costo = costo1;
        }

        //usar metodo virtual de object, tostring
        //si se quiere se sobreescribe, sino no, no es obligatorio

        public override string ToString(){
            //return base.ToString();
            return this.patente;
        }

        public virtual string MostrarDatos(){
            //muestra la patente, revisar
            return this.patente;
        }

        //definir propiedades abstractas

        /*public abstract float CalcularCosto()
        {
            return 1;
        }*/
        public abstract float CalcularCosto();

       //Quizas convertir el string de patente a float de costo?
        /*public float Costo {
            get {
                return ;
            }
        }*/

        //falta en algun lado las propiedades get y set



    }
}
