using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Main
{
    public class Numero
    {
        private double _numero;

        //Constructor por defecto, asigna valor 0.
        public Numero():this(0){ }


        //Valida y asigna valor por parametro.
        public Numero(string numero) {
            this.setNumero(numero);
        }


        //Asigna valor pasado por parametro
        public Numero(double numero)
        {
            this._numero = numero;
        }

        //Devuelve valor del numero
        public double getNumero() {
            return this._numero;
        }

        //Valida y setea valor.
        private void setNumero(string numero) {
            this._numero = Numero.validarNumero(numero);
        }

        //Valida el string pasado por parametro, convirtiendolo a numero. Caso contrario, devuelve 0.
        private static double validarNumero(string numero) {
            double numeroAux;
            if (double.TryParse(numero, out numeroAux)) {
                return numeroAux;
            }
            return 0;
        }

        //Sobrecarga operador +, sumando dos objetos Numero.
        public static double operator +(Numero num1, Numero num2) {
            return num1.getNumero() + num2.getNumero();
        }

        //Sobrecarga operador -, restando dos objetos Numero.
        public static double operator -(Numero num1, Numero num2)
        {
            return num1.getNumero() - num2.getNumero();
        }

        //Sobrecarga operador *, multiplicando dos objetos Numero.
        public static double operator *(Numero num1, Numero num2)
        {
            return num1.getNumero() * num2.getNumero();
        }

        //Sobrecarga operador /, dividiendo el primer objeto tipo Numero por el segundo. Si el divisor es 0, la funcion devuelve 0.
        public static double operator /(Numero num1, Numero num2)
        {
            if (num2.getNumero() != 0)
                return num1.getNumero() / num2.getNumero();
            return 0;
        }

    }
}
