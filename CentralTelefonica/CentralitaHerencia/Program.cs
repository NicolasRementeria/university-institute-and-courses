using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CentralitaHerencia
{
    class Program
    {
        static void Main(string[] args)
        {
            Centralita telefonica = new Centralita("Telefonica");
            Local llamada1 = new Local("Lugar1", 30, "Destino1", 2.65);
            Provincial llamada2 = new Provincial("Lugar2", Franja.Franja_1, 21, "Destino2");
            Local llamada3 = new Local("Lugar3", 45, "Lugar3", 1.99);
            Provincial llamada4 = new Provincial(Franja.Franja_3, llamada2);

            telefonica.Llamadas.Add(llamada1);
            telefonica.Llamadas.Add(llamada2);
            telefonica.Llamadas.Add(llamada3);
            telefonica.Llamadas.Add(llamada4);


        }
    }
}
