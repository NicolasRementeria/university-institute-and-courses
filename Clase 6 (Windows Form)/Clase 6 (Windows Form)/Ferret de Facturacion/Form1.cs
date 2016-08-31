using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Ferret_de_Facturacion
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void txtN1_TextChanged(object sender, EventArgs e)
        {

        }

        private void txtN2_TextChanged(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void btnSumar_Click(object sender, EventArgs e)
        {
            MessageBox.Show((float.Parse(txtN1.Text)+float.Parse(txtN2.Text)+float.Parse(txtN3.Text)).ToString());
        }

        private void btnProm_Click(object sender, EventArgs e)
        {
            MessageBox.Show(((float.Parse(txtN1.Text) + float.Parse(txtN2.Text) + float.Parse(txtN3.Text))/3).ToString());
        }

        private void btnFinal_Click(object sender, EventArgs e)
        {
            float suma = (float.Parse(txtN1.Text) + float.Parse(txtN2.Text) + float.Parse(txtN3.Text));
            MessageBox.Show((suma + suma*21/100).ToString());
        }
    }
}
