using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Excepcion_basica
{
    class Program
    {
        public static void Operar()
        {
            string dato;
            int numero;

            try
            {
                dato = Console.ReadLine();
                numero = int.Parse(dato);
                numero = numero / numero;
            }
            catch (Exception ex)
            {
                //Dado en la clase: Operaciones para guardar informacion de la excepcion
                

                throw new Exception("Se quedo sin internet"); //Fuerza la excepcion
            }
        }

        public static void LanzarError() {
            throw new Exception("Se quedò sin memoria RAM"); //El throw no necesita try
        }
        //Dividir sistema que uno muestre mensaje y otra muestre error, o todo en uno

        static void Main(string[] args)
        {
            //string dato;
            //int numero;

            try
            {
                //Solamente se pone lo que puede dar error
                /*Pegado en el metodo static abajo
                 * dato = Console.ReadLine();
                numero = int.Parse(dato);
                numero = numero / numero;
                 * */
                LanzarError(); // Muestra de una que no hay ram, se va del try luego de ejecutarse
                Operar();
            }

            catch (FormatException ex)
            {
                Console.Write("Error de formato: " + ex.Message);
            }
            catch (DivideByZeroException ex)
            {
                Console.Write("No se puede dividir por 0: " + ex.Message);
            }
            catch (Exception ex) //nombre de la excepcion ex
            {
                //si ocurre un error, viene al catch
                //siempre devuelve un objeto de tipo exception

                Console.Write("General: " + ex.Message);

                //throw; // << sacar
            }
            finally{ // < Luego de todos los catch, siempre se ejecuta el finally
                //Se usa para liberar recursos o mostrar un mensaje final

            }
            //LanzarError(); // Va al error donde cayo en la linea
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