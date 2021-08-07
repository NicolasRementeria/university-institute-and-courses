using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            Aula miPrimerAula = new Aula();

            Alumno alum1 = new Alumno("Chico 1", 1);
            Alumno alum2 = new Alumno("Chico 2", 2);
            Alumno alum3 = new Alumno("Chico 3", 3);
            Alumno alum4 = new Alumno("Chico 4", 4);

            miPrimerAula.AgregarAlumno(alum1);
            miPrimerAula.AgregarAlumno(alum2);
            miPrimerAula.AgregarAlumno(alum3);

            miPrimerAula.BorrarAlumno(alum2);
            miPrimerAula.AgregarAlumno(alum4); //Hay un tema de posiciones de memorias


            miPrimerAula.AgregarAlumno(alum1);
            miPrimerAula.AgregarAlumno(alum2);
            miPrimerAula.AgregarAlumno(alum3);

            Aula.MostrarAlumno(miPrimerAula);

            miPrimerAula.existeAlumno(alum4);

            

            miPrimerAula.listaDeAlumno[0].nombre = "lalalala"; 
            //Console.WriteLine(alum1.nombre);

            Aula.MostrarAlumno(miPrimerAula);
            Console.ReadKey();

            /*En un array de 10, agrego el alumno 1, 2 y 3, quito el 2, en su lugar pongo el 4, intento agregar nuevamente el
             * 1, 2 y 3 pero 1 y 3 ya existen, en la posicion 4 agrego el alumno 2 que falta
             * y cambio el 1 por lalala*/

            /*Falta sobrecargar los operadores para lograr hacer: 
             Alumno == Alumno
             Aula == Alumno
             Aula = Aula + Alumno
             Aula = Aula - Alumno*/

        }
    }
}
