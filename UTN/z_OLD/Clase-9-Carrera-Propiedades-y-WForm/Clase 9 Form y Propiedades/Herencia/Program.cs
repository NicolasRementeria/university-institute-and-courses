using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Herencia
{
    //Polimorfismo

    class Program
    {
        static void Main(string[] args)
        {

            Factura miFactura = new Factura(111);
            Remito miRemito = new Remito(666);
            FacturaA miFacturaA = new FacturaA(5, miFactura);
            FacturaPagada miFacturaPagada = new FacturaPagada("A", miFactura);


            //miFactura.Mostrar(); //Heredado de documento. Factura ES un documento, NO tiene un documento.
            
            List<Documentos> miListado = new List<Documentos>();
            miListado.Add(miFactura); //POLIMORFISMO, agrupa distintos objetos con algo en comun; todos son documentos.

            
            //miRemito.Mostrar();

            miListado.Add(miFactura);
            miListado.Add(miRemito);

            foreach (Documentos item in miListado)
            {
                //Console.Write(item.numero);
                item.Mostrar();
            }
            Console.ReadKey();

        }
    }
}
