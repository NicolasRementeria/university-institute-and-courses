using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Excepcion_basica
{
    public class Auto
    {
        public string marca;
        public int numero;
        public List<Rueda> listadoDeRuedas;

        public Auto(string Marca, int Numero) {
            this.marca = Marca;
            this.numero = Numero;
            this.listadoDeRuedas = new List<Rueda>();


        }

        public void Andar() { 
            //Si la cantidad de ruedas es <4, lanza excepcion
            if (this.listadoDeRuedas.Count < 4)
            {
                throw new MiExcepcion("Fallo por ruedas < 4", DateTime.Now);
            }
            else {
                try
                {
                    foreach (Rueda item in this.listadoDeRuedas)
                    {
                        item.Rodar();
                    }
                }
                catch (PinchaduraException miPinchadura)
                {

                    //throw new AutoException("Excepcion de Auto", miPinchadura.horaDeLaExepcion, this);
                    throw new AutoException(miPinchadura.Message, miPinchadura.horaDeLaExepcion, this);

                    //Tambien puede ser:
                    //AutoException miExcepcion = new AutoException("Excepcion de Auto", miPinchadura.horaDeLaExepcion, this);
                    // Accionar sobre miExcepcion
                    //throw miExcepcion;

                }
                
            }
            
        }



    }
}
