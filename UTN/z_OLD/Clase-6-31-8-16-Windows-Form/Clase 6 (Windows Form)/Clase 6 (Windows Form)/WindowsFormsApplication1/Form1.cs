using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void BtnSaludar_Click(object sender, EventArgs e)
        {
            string aux;
            aux = this.txtNombre.Text;
            MessageBox.Show(aux);
            // Toma datos del texto y muestra datos
            
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            

        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void btnMostrar_Click(object sender, EventArgs e)
        {
            this.lblNombre.Text = "Cambié el texto"; //Cambia el texto al label
        }

        private void brnAprobarMateria_Click(object sender, EventArgs e)
        {
            
        }

        private void btnAprobarMateria_MouseHover(object sender, EventArgs e)
        {
            /*this.btnAprobarMateria.Visible = false; // CASI APRUEBO*/
        }

        private void btnAprobarMateria_MouseLeave(object sender, EventArgs e)
        {
            this.btnAprobarMateria.Visible = true;
        }

        private void btnAprobarMateria_MouseEnter(object sender, EventArgs e)
        {
            this.btnAprobarMateria.Visible = false;
        }
    }
}
