using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Excepcion_basica
{
    public class Carrera
    {
        public List<Auto> listaDeAutos;
        public string autodromo;

        public Carrera(string autodromoDado) {
            this.autodromo = autodromoDado;
            this.listaDeAutos = new List<Auto>();
        }

        public void CorrerCarrera() { 
            //se fija si el listado de autos es > 0, sino lanza excepcion de tipo MiExcepcion
            if(this.listaDeAutos.Count == 0 )
                throw new MiExcepcion("Lista vacia", DateTime.Now);
            else
                foreach (Auto item in this.listaDeAutos)
                {
                    item.Andar();
                }
        }



        //Ejercicio 2 de practica, Constructor

       /* public Carrera()
        {
            this.listaDeAutos = new List<Auto>();
            this.autodromo = "Autodromo por Defecto";

            throw new MiExcepcion("Fallo Prueba 2", DateTime.Now);

        }

        EL METODO DEBE ESTAR EN OTRA CLASE
        
        public void PruebaEjercicio2() {
            if(this.listaDeAutos.Count == 1)
                throw new MiExcepcion("Hay solo un auto", DateTime.Now);
            try
            {
                foreach (var item in collection)
                {
                    
                }
            }
            catch (Exception ex)
            {
                
                throw new Exception(ex.Message);
            }
        }*/



    }
}
