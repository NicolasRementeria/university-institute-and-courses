using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    public class Aula
    {
        public int numero;
        public Alumno[] listaDeAlumno; //Array de alumnos, necesitan instancia para funcionar

        public Aula() { //Constructor
            this.listaDeAlumno = new Alumno[10]; //Instancia
            /*for (int i = 0; i < this.listaDeAlumno.Length; i++)
            {
                this.listaDeAlumno[i] = new Alumno();

            }*/
            /*foreach (Alumno objAlum in this.listaDeAlumno) //ASI NO SE USA, MEJOR USAR EL NULL
            {
                objAlum.nombre = "Sin Asignar";
            }*/
        }

        public static void MostrarAlumno(Aula AulaRecorrida) {
            foreach (Alumno objAlum in AulaRecorrida.listaDeAlumno)
            {
                if((object)objAlum != null){ // << castear objAlum con object?
                    Console.WriteLine("Nombre: {0}", objAlum.nombre);
                }

            }
        }
        /// <summary>
        /// Devuelve el indice del 1er elemento null, de lo contrario retorna -1
        /// </summary>
        /// <returns></returns>
        public int obtenerIndice() {
            int i;
            for (i = 0; i < this.listaDeAlumno.Length; i++){
                if ((object)this.listaDeAlumno[i] == null){ //casteando un objeto y comparando a null
                    return i;
                }
            }
            return -1;
        }
        /// <summary>
        /// Retorna el indice del objeto, de lo contrario retorna -1
        /// </summary>
        /// <param name="objAlumno"></param>
        /// <returns></returns>
        public int obtenerIndice(Alumno objAlumno) { //sobrecarga
            int i;
            for (i = 0; i < this.listaDeAlumno.Length; i++){
                if ((object)this.listaDeAlumno[i] != null){
                    if(this.listaDeAlumno[i].legajo == objAlumno.legajo){
                        return i;
                    }
                }
            }
            return -1;            
        }

        public void AgregarAlumno(Alumno alumno){
            int indice = obtenerIndice();
            if ((this.obtenerIndice(alumno) == -1) &&  indice != -1) // Funciona incluso si quiero agregar una posicion 11 en un array de 10, es decir no lo agrega en vez de dar error
                this.listaDeAlumno[indice] = alumno;

        }
        public void BorrarAlumno(Alumno objAlum) {
            for (int i = 0; i < this.listaDeAlumno.Length; i++){
                if((object)this.listaDeAlumno[i] != null){
                    if (this.listaDeAlumno[i].legajo == objAlum.legajo)
                    {
                        this.listaDeAlumno[i] = null;
                        break;
                    }
                }
            }
        }

        public bool existeAlumno(Alumno alumno)
        {
            for (int i = 0; i < this.listaDeAlumno.Length; i++)
            {
                if ((object)this.listaDeAlumno[i] != null)
                {
                    if (this.listaDeAlumno[i].legajo == alumno.legajo)
                    {
                        Console.WriteLine("El alumno existe");
                        return true;
                    }
                }
            }
            Console.WriteLine("El alumno no existe");
            return false;
        }



    }
}
