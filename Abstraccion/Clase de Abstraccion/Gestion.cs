using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Clase_de_Abstraccion
{
    public class Gestion
    {
        static float MostrarImp(IAfip algo) {
            return algo.RetornarImpuesto();
        }



    }
}

/*EJERCICIO:
 1- IMPLEMENTAR MOSTRAR AFIP
 * rta: es solo usar el metodo de iafip sobre el parametro dado en el metodo static
 2- VERIFICAR SI LA IMPLEMENTACION SE HEREDA O NO
 * rta: Si, se hereda; privada y comercial heredan de avion, que heredan de iafip y vehiculo
 3- CREAR PROPIEDADES SIMPLES, QUE SOLO DEVUELVAN O MUESTREN
 3A- ABSTRACTAS (abstract)
 3B- VIRTUALES (SOLO CLASES NO ABSTRACTAS) (virtual)
 3C- EN LA INTERFACE
 */

