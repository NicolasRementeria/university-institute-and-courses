using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Habemus_Papa
{
    public class Conclave
    {
        private int _cantMaxCardenales;
        private List<Cardenal> _cardenales;
        private static bool _habemusPapa; // << Le agreguè static porque lo usa la sobrecarga explicita
        private string _lugarEleccion;
        private Cardenal _papa;
        public static int cantidadVotaciones;
        public static DateTime fechaVotacion;

        #region Constructores
        static Conclave() { 
            //Inicializar la cantidad de votaciones a 0
            //Inicializar fecha de votacion a fecha actual
            cantidadVotaciones = 0;
            fechaVotacion = DateTime.Now;

        }

        private Conclave() { // Era public, le agregue private, ya que uno de los constructores () es privado y el static no puede serlo
            this._cantMaxCardenales = this._cantMaxCardenales + 1;
            this._lugarEleccion = "Capilla Sixtina";
            _cardenales = new List<Cardenal>(); // Agregado
            _habemusPapa = false; // Agregado

        }

        private Conclave(int cantidadCardenales) : this() {
            this._cantMaxCardenales = cantidadCardenales;
        }

        public Conclave(int cantidadCardenales, string lugarEleccion) : this (cantidadCardenales){
            this._lugarEleccion = lugarEleccion;
        }
        #endregion

        private static void ContarVotos(Conclave conclave) { 
            //Recorrer la lista de cardenales, el que recibe mas votos lo proclama PAPA, coloca true o false en habemus papa
        }

        private bool HayLugar() {
            if (_cantMaxCardenales > _cardenales.Count) {
                return true;
            }
            return false;
        }

        private string MostrarCardenales()
        {
            /*MostrarCardenales (privado): Recorre la lista de Cardenales del cónclave y muestra la información 
             * de cada cardenal (utilizar el método "Mostrar" de Cardenal)*/
            StringBuilder sb = new StringBuilder();

            foreach (Cardenal car in this._cardenales){
                sb.AppendLine(Cardenal.Mostrar(car));
            }

            return sb.ToString();
            //Usar StringBuilder para mostrar toda la lista de todos los cardenales
        }

        public string Mostrar() {
            return("Lugar de votacion: " + _lugarEleccion + 
                "/nFecha de votacion: " + fechaVotacion + 
                "/nCantidad de veces que se votó: " + cantidadVotaciones
 
                );

            /*Agrear leyenda HABEMUS PAPA mas nombre del mismo con ObtenerNombreYNombrePapal si cabe, 
            sino NO HABEMUS PAPA con la info de todos los cardenales del conclave usando MostrarCardenales*/
            //Ver de usar StringBuilder
        }

        public static explicit operator bool(Conclave con) {
            return _habemusPapa;
        }

        public static implicit operator Conclave(int cantidadCardenales) {
            return new Conclave(cantidadCardenales); // Crea un nuevo conclave
        }

        public static bool operator == (Conclave con, Cardenal c){
            /*for (int i = 0; i < con._cardenales.Count; i++){
                { 
                    
                }
            }*/

            foreach (Cardenal car in con._cardenales){
                if (car == c) {
                    return true;
                }
            }
            return false;
        }

        public static bool operator !=(Conclave con, Cardenal c){ 
            return !(con == c);
        } 

        public static Conclave operator +(Conclave con, Cardenal c){
            if((con != c) && con.HayLugar() ){
                con._cardenales.Add(c);
            }
            return con;
        }

        public static void VotarPapa(Conclave conclave) { 
            // EL RANDOM PUEDE ESTAR EN EL CONSTRUCTOR, PARA QUE NO SE USE SIEMPRE EL MISMO
            /* ind = random(entre 0 u cant de cardenales) < el random va a ser un cardenal *
             * ___ [ind] ++; < Sumarle un voto
             */
        }




    }
}
