using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Ejercicio_Carrera;

namespace CarreraUI
{
    public partial class Form1 : Form
    {
        private Carrera _miCarrera;

        public Form1()
        {
            InitializeComponent();
            //this._miCarrera = new Carrera(); //Instancia
            foreach (EFabricante tipo in Enum.GetValues(typeof(EFabricante)))
            { //recorre enumerados
                this.cmbFabricante.Items.Add(tipo);
            }
            this.cmbFabricante.SelectedIndex = 1;
            this.cmbFabricante.DropDownStyle = ComboBoxStyle.DropDownList; //Muestra de mejor manera el combo

        }

        private void CargarListado()
        {
            this.lsbAutos.Items.Clear();


            foreach (Auto item in this._miCarrera.listaDeAutos)
            {
                this.lsbAutos.Items.Add(item.DatosEnString); //Era item.retornarStringParaListado(), pero cambia al agregar Datos en String con su get
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //Rueda rueda1 = new Rueda();

            _miCarrera = new Carrera(this.txtNombre.Text, this.txtFecha.Text, this.txtLugar.Text);
            this.gpbCarrera.Enabled = false;

        }

        private void groupBox3_Enter(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void grpCarrera_Enter(object sender, EventArgs e)
        {

        }


        private void lsbAutos_SelectedIndexChanged(object sender, EventArgs e)
        {

        }


        private void txtNombre_TextChanged(object sender, EventArgs e)
        {
            //AGREGAR VALOR POR DEFECTO AL NOMBRE
        }

        private void txtLugar_TextChanged(object sender, EventArgs e)
        {

        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void lblNombre_Click(object sender, EventArgs e)
        {

        }

        private void gpbCarrera_Enter(object sender, EventArgs e)
        {

        }

        private void txtFecha_TextChanged(object sender, EventArgs e)
        {

        }

        private void lblFecha_Click(object sender, EventArgs e)
        {

        }

        private void lblLugar_Click(object sender, EventArgs e)
        {

        }

        private void btnCorrerCarrera_Click(object sender, EventArgs e)
        {
            //ACA TIENE QUE MOSTRAR LOS GANADORES
            this.txtCorrerCarrera.Text = this._miCarrera.CorrerCarrera((Kilometro)50);//Valor placeholder
        }

        private void btnAgregarAuto_Click(object sender, EventArgs e)
        {
            Auto autoAuxiliar = new Auto(this.txtNombrePiloto.Text, (EFabricante)this.cmbFabricante.SelectedItem);
            //this._miCarrera.listaDeAutos.Add(autoAuxiliar);
            this._miCarrera = _miCarrera + autoAuxiliar;
            CargarListado();
        }

        private void gpbAuto_Enter(object sender, EventArgs e)
        {

        }

        private void cmbFabricante_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void txtNombrePiloto_TextChanged(object sender, EventArgs e)
        {

        }

        private void lblFabricante_Click(object sender, EventArgs e)
        {

        }

        private void txtCorrerCarrera_TextChanged(object sender, EventArgs e)
        {

        }


    }
}
