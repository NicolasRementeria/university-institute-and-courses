using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ejercicio_Carrera
{
    public class Auto
    {
        // composicion: tiene otras clases dentro, como Rueda.
        public EFabricante Fabricante;
        public Rueda DI;
        public Rueda DD;
        public Rueda TI;
        public Rueda TD;
        private Kilometro KilometrosRecorridos;
        private Tiempo TiempoDemorado;
        public static int contadorDeObjetos;
        private static Random randomMarcas; // es unico para esta clase.

        //public string nombreDelPiloto;

        private string _nombreDelPiloto;

        public string NombrePiloto
        { //PROPIEDAD QUE USA EL PRIVATE
            set
            { //el set asigna; sirve para validar asignaciones, de ser necesario
                this._nombreDelPiloto = value; //Escritura
            }
            get
            {
                return this._nombreDelPiloto; //Lectura
            }
        }

        public string DatosEnString
        { //PROPIEDAD QUE NO USA VARIABLE, ES DE SOLO LECTURA
            get
            {
                return this.retornarStringParaListado();
            }
        }

        //public Dictionary<string, Rueda> ruedasIngresadas;

        public Auto()
        {
            this.Fabricante = (EFabricante)(Auto.randomMarcas.Next(0, 3));
            this.DI = new Rueda();
            this.DD = new Rueda();
            this.TI = new Rueda();
            this.TD = new Rueda();
            this.KilometrosRecorridos = 0;
            this.TiempoDemorado = 0;

            Auto.contadorDeObjetos++;
        }

        public Auto(string nombrePiloto, EFabricante fabricante) : this()
        {
            this._nombreDelPiloto = nombrePiloto;
            this.Fabricante = fabricante;
        }

        // un constructor estatico no puede ser public. Se ejecuta en la primer llamada a la clase que haga
        // tiene que tener atributos estaticos
        // puedo hacerlo para inicializar variables estaticas, como contador de objetos creados
        // no se lo puede sobrecargar
        static Auto()
        {
            Auto.contadorDeObjetos = 0;
            Auto.randomMarcas = new Random();
        }

        public static bool CompararAuto(Auto auto1, Auto auto2)
        {
            if (auto1.Fabricante == auto2.Fabricante)
                return true;
            return false;
        }

        public string MostrarAuto()
        {
            //Console.WriteLine("El fabricante es {0}", this.Fabricante);
            StringBuilder sb = new StringBuilder();
            sb.AppendLine("Fabricante: " + this.Fabricante);
            sb.AppendLine("Kilometros recorridos: " + this.KilometrosRecorridos);
            sb.AppendLine("Tiempo demorado: " + this.TiempoDemorado);
            return sb.ToString();

        }

        public void VolverACero()
        {
            this.KilometrosRecorridos = 0;
            this.TiempoDemorado = 0;
        }

        #region version antigua
        /*
         * DEPRECATED: POR SOBRECARGA DE METODOS
        public void AgregarKilometro(int kilometros)
        {
            this.KilometrosRecorridos += kilometros;
        }

        public void AgregarTiempo(int tiempo)
        {
            this.TiempoDemorado += tiempo;
        }
        */
        #endregion

        public Kilometro ObtenerKilometros()
        {
            return this.KilometrosRecorridos;
        }

        public Tiempo ObtenerTiempo()
        {
            return this.TiempoDemorado;
        }

        public void Agregar(Tiempo tiempo)
        {
            this.TiempoDemorado = this.TiempoDemorado + tiempo;
        }

        public void Agregar(Kilometro kilometro)
        {
            this.KilometrosRecorridos = this.KilometrosRecorridos + kilometro;
        }

        private string retornarStringParaListado()
        { //Deberia ser publico, pero es private por el GET mas arriba
            StringBuilder sb = new StringBuilder();
            sb.AppendLine("Fabricante: " + this.Fabricante + " - ");
            sb.AppendLine("Piloto: " + this._nombreDelPiloto);
            return sb.ToString();
        }

        public static int OrdenarPorMarcaAsc(Auto auto1, Auto auto2){
            /*if (auto1.Fabricante.CompareTo){}*/
            //return string.Compare(auto1.Fabricante.ToString(), auto2.Fabricante.ToString()); //Ordena de forma creciente, de menor letra a mayor
            
            return string.Compare(auto1.Fabricante.ToString(), auto2.Fabricante.ToString()); //Ordena de forma decreciente, de mayor letra a menor
        }
        public static int OrdenarPorMarcaDesc(Auto auto1, Auto auto2)
        {
            return string.Compare(auto2.Fabricante.ToString(), auto1.Fabricante.ToString()); //Ordena de forma decreciente, de mayor letra a menor
        }

        public static int OrdenarPorPilotoAsc(Auto auto1, Auto auto2)
        {
            return string.Compare(auto1.NombrePiloto.ToString(), auto2.NombrePiloto.ToString());
        }

        public static int OrdenarPorPilotoDesc(Auto auto1, Auto auto2)
        {
            return string.Compare(auto2.NombrePiloto.ToString(), auto1.NombrePiloto.ToString());
        }

         

    }
}
