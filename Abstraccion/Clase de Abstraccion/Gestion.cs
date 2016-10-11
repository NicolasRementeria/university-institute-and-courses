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
 2- VERIFICAR SI LA IMPLEMENTACION SE HEREDA O NO
 3- CREAR PROPIEDADES SIMPLES, QUE SOLO DEVUELVAN O MUESTREN
 3A- ABSTRACTAS 
 3B- VIRTUALES (SOLO CLASES NO ABSTRACTAS)
 3C- EN LA INTERFACE
 */

