using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab_2_Indexador
{
    public class Laboratorio
    {
        public string nombre;
        public List<PC> listaDePC;

        public Laboratorio(string nombreDado) {
            this.nombre = nombreDado;
            this.listaDePC = new List<PC>();
        }

        //INDEXADOR PARA TRATAR A LA CLASE COMO ARRAY
        public PC this[int indice] {
            get {
                //validar la cantidad de elementos, para que si el largo es de 5 elementos y el indice dado es > 5, no pinche
                //revisar
                if (indice >= 0 && indice <= this.listaDePC.Count)
                    return this.listaDePC[indice];
                else
                    return null;
            }
            set {
                //Si el indice = count, agregue
                if (indice == listaDePC.Count)
                    this.listaDePC.Add(value);
                else
                    if (indice >= 0 && indice < this.listaDePC.Count)
                        this.listaDePC[indice] = value;

                //this.listaDePC[indice] = value;
            }
        }

    }
}
