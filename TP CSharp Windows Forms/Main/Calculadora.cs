using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Main
{
    class Calculadora
    {
        //Realiza la operacion ingresada, devolviendo el resultado. Si el operador ingresado no es "+", "-", "*" o "/", el resultado devuelve la sumatoria.

        #region DEPRECATED POR SOBRECARGA DE OPERADORES
        /*public static double Operar(Numero num1, Numero num2, string operadorIngresado) {
            switch (Calculadora.OperadorValidado(operadorIngresado)) {
                case "+":
                    return num1.getNumero() + num2.getNumero();
                case "-":
                    return num1.getNumero() - num2.getNumero();
                case "*":
                    return num1.getNumero() * num2.getNumero();
                case "/":
                    //Validacion del numero 2; si el divisor es 0, devuelve 0, caso contrario devuelve la división. 
                    if (num2.getNumero() != 0){
                        return num1.getNumero() / num2.getNumero();
                    }
                    else {
                        return 0;
                    }
                default:
                    return 0;
                    
            }
        }*/
        #endregion

        public static double Operar(Numero numero1, Numero numero2, string operador) {
            switch (Calculadora.validarOperador(operador)) {
                case "+":
                    return numero1 + numero2;
                case "-":
                    return numero1 - numero2;
                case "*":
                    return numero1 * numero2;
                case "/":
                    return numero1 / numero2;
                default:
                    return 0;
            }
        }


        #region DEPRECATED POR VERSION ALTERNATIVA A VALIDAROPERADOR
        //Validacion del operador. En esta versión, si no es un operador ingresado, devuelve NULL.
        /* public static string validarOperador(string operadorIngresado) {
             if (operadorIngresado.Contains("-"))
                 return "-";
             else{
             if (operadorIngresado.Contains("*"))
                 return "*";
             else{
                 if (operadorIngresado.Contains("/"))
                     return "/";
                 else {
                      if (operadorIngresado.Contains("+"))
                         return "+";
                      else
                         return null;
                      }
                  }
             }
         }*/
        #endregion

        //Validacion del operador. Si el operador no es "+", "-", "*" o "/", el operador resultante es un "+".
        public static string validarOperador(string operador)
        {
            if (operador.Contains("-"))
                return "-";
            else
            {
                if (operador.Contains("*"))
                    return "*";
                else
                {
                    if (operador.Contains("/"))
                        return "/";
                    return "+";
                }
            }
        }
    }
}
