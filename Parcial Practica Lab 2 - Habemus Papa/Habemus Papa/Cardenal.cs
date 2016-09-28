using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Habemus_Papa
{
    public class Cardenal
    {
        private int _cantVotosRecibidos;
        /*public int CantVotosRecibidos {
            get {
                return this._cantVotosRecibidos;
            }
        }*/

        private ENacionalidades _nacionalidad;
        private string _nombre;
        private string _nombrePapal;

        #region Constructores
        private Cardenal() { // << Lo hice inicialmente publico
            this._cantVotosRecibidos = 0; // Inicializacion de los votos a 0
        }
        public Cardenal(string nombre, string nombrePapal) : this(){
            this._nombre = nombre;
            this._nombrePapal = nombrePapal;
        }

        public Cardenal(string nombre, string nombrePapal, ENacionalidades nacionalidad) : this(nombre, nombrePapal) {
            this._nacionalidad = nacionalidad;
        }
        #endregion

        public int getCantidadVotosRecibidos() {
            return _cantVotosRecibidos;
        }

        private string Mostrar() { 
            return ObtenerNombreYNombrePapal(); //Mostrar  toda la info del cardenal, usar metodo ObtenerNombreYNombrePapal
        }

        public static string Mostrar(Cardenal c) { 
            //Usar funcion anterior, no repetir codigo
            return (c.Mostrar() + "Nacionalidad: " + (ENacionalidades)c._nacionalidad + "/nCantidad de votos recibidos: " + c._cantVotosRecibidos );
            //Ver de usar StringBuilder
        }

        public string ObtenerNombreYNombrePapal() {
            return ("El cardenal " + this._nombre + "se llamará " + this._nombrePapal + ".");
        }

        public static bool operator ==(Cardenal c1, Cardenal c2) {
            if (c1._nombre == c2._nombre && c1._nombrePapal == c2._nombrePapal && c1._nacionalidad == c2._nacionalidad) {
                return true;
            }
            return false;
        }

        public static bool operator !=(Cardenal c1, Cardenal c2) { 
            return !(c1 == c2);
        }

        public static Cardenal operator ++(Cardenal c){
            Cardenal cAux = c;
            cAux._cantVotosRecibidos = cAux._cantVotosRecibidos + 1;
            return cAux;
        }

    }
}
