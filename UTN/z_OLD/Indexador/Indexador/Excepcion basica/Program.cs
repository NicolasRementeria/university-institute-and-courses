using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Excepcion_basica
{
    class Program
    {
        static void Main(string[] args)
        {
            Carrera miNuevaCarrera = new Carrera("Autodromo Test");
            //miNuevaCarrera.CorrerCarrera();

            Auto miNuevoAuto = new Auto("Marca test", 5);
            //miNuevoAuto.Andar();

            Auto Auto1 = new Auto("Ford", 5);
            Auto1.listadoDeRuedas.Add(new Rueda("Rueda 1 Auto 1"));
            Auto1.listadoDeRuedas.Add(new Rueda("Rueda 2 Auto 1"));
            Auto1.listadoDeRuedas.Add(new Rueda("Rueda 3 Auto 1"));
            Auto1.listadoDeRuedas.Add(new Rueda("Rueda 4 Auto 1"));

            Auto Auto2 = new Auto("Chevrolet", 5);
            Auto2.listadoDeRuedas.Add(new Rueda("Rueda 1 Auto 2"));
            Auto2.listadoDeRuedas.Add(new Rueda("Rueda 2 Auto 2"));
            Auto2.listadoDeRuedas.Add(new Rueda("Rueda 3 Auto 2"));
            Auto2.listadoDeRuedas.Add(new Rueda("Rueda 4 Auto 2"));

            Auto Auto3 = new Auto("Fiat", 5);
            Auto3.listadoDeRuedas.Add(new Rueda("Rueda 1 Auto 3"));
            Auto3.listadoDeRuedas.Add(new Rueda("Rueda 2 Auto 3"));
            Auto3.listadoDeRuedas.Add(new Rueda("Rueda 3 Auto 3"));
            Auto3.listadoDeRuedas.Add(new Rueda("Rueda 4 Auto 3"));

            Auto Auto4 = new Auto("Porche", 5);
            Auto4.listadoDeRuedas.Add(new Rueda("Rueda 1 Auto 4"));
            Auto4.listadoDeRuedas.Add(new Rueda("Rueda 2 Auto 4"));
            Auto4.listadoDeRuedas.Add(new Rueda("Rueda 3 Auto 4"));
            Auto4.listadoDeRuedas.Add(new Rueda("Rueda 4 Auto 4"));

            miNuevaCarrera.listaDeAutos.Add(Auto1);
            miNuevaCarrera.listaDeAutos.Add(Auto2);
            miNuevaCarrera.listaDeAutos.Add(Auto3);
            miNuevaCarrera.listaDeAutos.Add(Auto4);



            try
            {
                miNuevaCarrera.CorrerCarrera();
            }
            catch (AutoException fe)
            {
                Console.WriteLine(fe.Message + " " + fe.textoHoraDeLaExcepcion);
            }
            catch (PinchaduraException fe)
            {
                Console.WriteLine(fe.Message + " " + fe.textoHoraDeLaExcepcion);
            }
            catch (MiExcepcion fe)
            {
                Console.WriteLine(fe.Message + " " + fe.textoHoraDeLaExcepcion);
            }
            catch (Exception fe)
            {
                Console.WriteLine(fe.Message + " " + DateTime.Now);
            }
            Console.ReadKey();

        }
    }
    

}

//Por cada excepcion se agrega un catch
//Importa el orden, el general debe ir ULTIMO; van de lo particular a lo general
//Permite saber lo que pasa en el sistema cuando no se está en el sistema
//La idea es tener un solo catch que capture un error definido por mi
//Si se le ingresa un alumno a una persona, podes tomar los datos de alumno y agregarlos a program
//Las excepciones son errores pero tambien objetos que se pueden burbujear




