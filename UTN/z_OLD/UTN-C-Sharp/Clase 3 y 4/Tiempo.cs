using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication2
{
    public class Tiempo
    {
        private int _cantidad; // las variables privadas llevan guion bajo al inicio y luego minuscula

        private Tiempo(int cantidad)
        { // Constructor de Tiempo
            this._cantidad = cantidad;
        }

        public static Tiempo sumar(Tiempo tiempoAux, int valor)
        { // intento sobrecargar el operador + pero no es la manera

            tiempoAux._cantidad = tiempoAux._cantidad + valor;

            return tiempoAux;
        }

        /*public static Tiempo operator +(Tiempo tiempoAux, int valor)
        { // intento sobrecargar el operador + pero no es la manera

            tiempoAux.Cantidad = tiempoAux.Cantidad + valor;

            return tiempoAux;
        }*/

        //CLASE 5, SOBRECARGA DE OPERADORES
        public static Tiempo operator +(Tiempo tiempoAux, int valor) {
            tiempoAux._cantidad = tiempoAux._cantidad + valor;
            return tiempoAux;
        }

        public static Tiempo operator +(Tiempo tiempo1, Tiempo tiempo2){
            tiempo1 = tiempo1 + tiempo2._cantidad;
            return tiempo1;
        }

        public static Tiempo operator -(Tiempo tiempoAux, int valor){
            tiempoAux._cantidad = tiempoAux._cantidad - valor;
            return tiempoAux;
        }

        public static Tiempo operator -(Tiempo tiempo1, Tiempo tiempo2){
            tiempo1 = tiempo1 - tiempo2._cantidad;
            return tiempo1;
        }

        public static bool operator ==(Tiempo tiempoAux, int valor){
            return (tiempoAux._cantidad == valor);
        }

        public static bool operator ==(Tiempo tiempo1, Tiempo tiempo2){

            return(tiempo1._cantidad==tiempo2._cantidad);
        }

        // FALTA SOBRECARGAR LAS NEGACIONES
        public static bool operator !=(Tiempo tiempo1, Tiempo tiempo2){
            return !(tiempo1 == tiempo2);
        }

        public static bool operator !=(Tiempo tiempoAux, int valor) {
            return !(tiempoAux._cantidad == valor);
        }
         
        // Sobrecarga explicita o implicita
        public static implicit operator Tiempo(int numero){
            return new Tiempo(numero);
        }


        public static explicit operator int(Tiempo tiempo) {
            return tiempo._cantidad;
        }

    }
}