using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab_2_Indexador
{
    class Program
    {
        static void Main(string[] args)
        {
            //PC PC1 = new PC("IBM");
            //PC PC2 = new PC("DELL", "MACINTOSH");
            Laboratorio miLab = new Laboratorio("Mi laboratorio");

            //miLab[0] = PC1;
            //miLab[1] = PC2;

            //Console.WriteLine(miLab[0].marca + miLab[0].SO + "\n" + miLab[1].marca + miLab[1].SO);

            /*for (int i = 0; i < miLab.listaDePC.Count; i++){
                Console.WriteLine(miLab[i].marca + miLab[i].SO);
            }*/

            miLab[0] = "LG";
            miLab[1] = "EXO";
            miLab[2] = "DELL";
            miLab[3] = "TEST";

            for (int i = 0; i < miLab.listaDePC.Count; i++)
            {
                Console.WriteLine(miLab[i].numero);
                Console.WriteLine(miLab[i].marca + " " + miLab[i].SO);
            }


            Console.ReadKey();

        }
    }
}

//FALTA VER LA LOGICA PARA QUITAR ELEMENTOS O MODIFICARLOS, PORQUE PROBABLEMENTE CADA MOVIMIENTO SUME AL CONTADOR +1 ERRONEAMENTE
