using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Main
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void txtNumero1_TextChanged(object sender, EventArgs e)
        {

        }

        private void txtNumero2_TextChanged(object sender, EventArgs e)
        {

        }

        private void cmbOperacion_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        //Limpia los numeros del textbox y el resultado del label
        private void btnLimpiar_Click(object sender, EventArgs e)
        {
            this.txtNumero1.Clear();
            this.txtNumero2.Clear();
            this.lblResultado.Visible = false;
        }

        //Opera sobre los 2 numeros ingresados, con el operador ingresado.
        private void button1_Click(object sender, EventArgs e)
        {
            Numero num1 = new Numero(this.txtNumero1.Text);
            Numero num2 = new Numero(this.txtNumero2.Text);
            this.lblResultado.Text = Calculadora.Operar(num1, num2, cmbOperacion.Text).ToString();
            this.lblResultado.Visible = true;
        }
    }
}
