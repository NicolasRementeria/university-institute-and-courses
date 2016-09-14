namespace CarreraUI
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.btnCrearCarrera = new System.Windows.Forms.Button();
            this.gpbCarrera = new System.Windows.Forms.GroupBox();
            this.txtLugar = new System.Windows.Forms.TextBox();
            this.lblLugar = new System.Windows.Forms.Label();
            this.txtFecha = new System.Windows.Forms.TextBox();
            this.lblFecha = new System.Windows.Forms.Label();
            this.txtNombre = new System.Windows.Forms.TextBox();
            this.lblNombre = new System.Windows.Forms.Label();
            this.gpbAuto = new System.Windows.Forms.GroupBox();
            this.cmbFabricante = new System.Windows.Forms.ComboBox();
            this.btnAgregarAuto = new System.Windows.Forms.Button();
            this.txtNombrePiloto = new System.Windows.Forms.TextBox();
            this.lblNombrePiloto = new System.Windows.Forms.Label();
            this.lblFabricante = new System.Windows.Forms.Label();
            this.gpbResultado = new System.Windows.Forms.GroupBox();
            this.txtCorrerCarrera = new System.Windows.Forms.TextBox();
            this.btnCorrerCarrera = new System.Windows.Forms.Button();
            this.gpbListadoDeAutos = new System.Windows.Forms.GroupBox();
            this.lsbAutos = new System.Windows.Forms.ListBox();
            this.gpbCarrera.SuspendLayout();
            this.gpbAuto.SuspendLayout();
            this.gpbResultado.SuspendLayout();
            this.gpbListadoDeAutos.SuspendLayout();
            this.SuspendLayout();
            // 
            // btnCrearCarrera
            // 
            this.btnCrearCarrera.Location = new System.Drawing.Point(18, 81);
            this.btnCrearCarrera.Name = "btnCrearCarrera";
            this.btnCrearCarrera.Size = new System.Drawing.Size(103, 38);
            this.btnCrearCarrera.TabIndex = 0;
            this.btnCrearCarrera.Text = "Crear Carrera";
            this.btnCrearCarrera.UseVisualStyleBackColor = true;
            this.btnCrearCarrera.Click += new System.EventHandler(this.button1_Click);
            // 
            // gpbCarrera
            // 
            this.gpbCarrera.Controls.Add(this.txtLugar);
            this.gpbCarrera.Controls.Add(this.lblLugar);
            this.gpbCarrera.Controls.Add(this.txtFecha);
            this.gpbCarrera.Controls.Add(this.lblFecha);
            this.gpbCarrera.Controls.Add(this.txtNombre);
            this.gpbCarrera.Controls.Add(this.lblNombre);
            this.gpbCarrera.Controls.Add(this.btnCrearCarrera);
            this.gpbCarrera.Location = new System.Drawing.Point(12, 25);
            this.gpbCarrera.Name = "gpbCarrera";
            this.gpbCarrera.Size = new System.Drawing.Size(512, 151);
            this.gpbCarrera.TabIndex = 1;
            this.gpbCarrera.TabStop = false;
            this.gpbCarrera.Text = "Carrera";
            this.gpbCarrera.Enter += new System.EventHandler(this.grpCarrera_Enter);
            // 
            // txtLugar
            // 
            this.txtLugar.Location = new System.Drawing.Point(339, 45);
            this.txtLugar.Name = "txtLugar";
            this.txtLugar.Size = new System.Drawing.Size(147, 20);
            this.txtLugar.TabIndex = 6;
            this.txtLugar.TextChanged += new System.EventHandler(this.txtLugar_TextChanged);
            // 
            // lblLugar
            // 
            this.lblLugar.AutoSize = true;
            this.lblLugar.Location = new System.Drawing.Point(339, 20);
            this.lblLugar.Name = "lblLugar";
            this.lblLugar.Size = new System.Drawing.Size(34, 13);
            this.lblLugar.TabIndex = 5;
            this.lblLugar.Text = "Lugar";
            this.lblLugar.Click += new System.EventHandler(this.label3_Click);
            // 
            // txtFecha
            // 
            this.txtFecha.Location = new System.Drawing.Point(173, 45);
            this.txtFecha.Name = "txtFecha";
            this.txtFecha.Size = new System.Drawing.Size(147, 20);
            this.txtFecha.TabIndex = 4;
            // 
            // lblFecha
            // 
            this.lblFecha.AutoSize = true;
            this.lblFecha.Location = new System.Drawing.Point(173, 20);
            this.lblFecha.Name = "lblFecha";
            this.lblFecha.Size = new System.Drawing.Size(37, 13);
            this.lblFecha.TabIndex = 3;
            this.lblFecha.Text = "Fecha";
            this.lblFecha.Click += new System.EventHandler(this.lblFecha_Click);
            // 
            // txtNombre
            // 
            this.txtNombre.Location = new System.Drawing.Point(15, 45);
            this.txtNombre.Name = "txtNombre";
            this.txtNombre.Size = new System.Drawing.Size(147, 20);
            this.txtNombre.TabIndex = 2;
            this.txtNombre.TextChanged += new System.EventHandler(this.txtNombre_TextChanged);
            // 
            // lblNombre
            // 
            this.lblNombre.AutoSize = true;
            this.lblNombre.Location = new System.Drawing.Point(15, 20);
            this.lblNombre.Name = "lblNombre";
            this.lblNombre.Size = new System.Drawing.Size(44, 13);
            this.lblNombre.TabIndex = 1;
            this.lblNombre.Text = "Nombre";
            this.lblNombre.Click += new System.EventHandler(this.label1_Click);
            // 
            // gpbAuto
            // 
            this.gpbAuto.Controls.Add(this.cmbFabricante);
            this.gpbAuto.Controls.Add(this.btnAgregarAuto);
            this.gpbAuto.Controls.Add(this.txtNombrePiloto);
            this.gpbAuto.Controls.Add(this.lblNombrePiloto);
            this.gpbAuto.Controls.Add(this.lblFabricante);
            this.gpbAuto.Location = new System.Drawing.Point(19, 184);
            this.gpbAuto.Name = "gpbAuto";
            this.gpbAuto.Size = new System.Drawing.Size(260, 199);
            this.gpbAuto.TabIndex = 2;
            this.gpbAuto.TabStop = false;
            this.gpbAuto.Text = "Auto";
            this.gpbAuto.Enter += new System.EventHandler(this.gpbAuto_Enter);
            // 
            // cmbFabricante
            // 
            this.cmbFabricante.FormattingEnabled = true;
            this.cmbFabricante.Location = new System.Drawing.Point(11, 44);
            this.cmbFabricante.Name = "cmbFabricante";
            this.cmbFabricante.Size = new System.Drawing.Size(146, 21);
            this.cmbFabricante.TabIndex = 8;
            this.cmbFabricante.SelectedIndexChanged += new System.EventHandler(this.cmbFabricante_SelectedIndexChanged);
            // 
            // btnAgregarAuto
            // 
            this.btnAgregarAuto.Location = new System.Drawing.Point(14, 141);
            this.btnAgregarAuto.Name = "btnAgregarAuto";
            this.btnAgregarAuto.Size = new System.Drawing.Size(97, 43);
            this.btnAgregarAuto.TabIndex = 7;
            this.btnAgregarAuto.Text = "Agregar Auto";
            this.btnAgregarAuto.UseVisualStyleBackColor = true;
            this.btnAgregarAuto.Click += new System.EventHandler(this.btnAgregarAuto_Click);
            // 
            // txtNombrePiloto
            // 
            this.txtNombrePiloto.Location = new System.Drawing.Point(11, 105);
            this.txtNombrePiloto.Name = "txtNombrePiloto";
            this.txtNombrePiloto.Size = new System.Drawing.Size(147, 20);
            this.txtNombrePiloto.TabIndex = 6;
            this.txtNombrePiloto.TextChanged += new System.EventHandler(this.txtNombrePiloto_TextChanged);
            // 
            // lblNombrePiloto
            // 
            this.lblNombrePiloto.AutoSize = true;
            this.lblNombrePiloto.Location = new System.Drawing.Point(11, 80);
            this.lblNombrePiloto.Name = "lblNombrePiloto";
            this.lblNombrePiloto.Size = new System.Drawing.Size(90, 13);
            this.lblNombrePiloto.TabIndex = 5;
            this.lblNombrePiloto.Text = "Nombre del Piloto";
            // 
            // lblFabricante
            // 
            this.lblFabricante.AutoSize = true;
            this.lblFabricante.Location = new System.Drawing.Point(11, 25);
            this.lblFabricante.Name = "lblFabricante";
            this.lblFabricante.Size = new System.Drawing.Size(57, 13);
            this.lblFabricante.TabIndex = 3;
            this.lblFabricante.Text = "Fabricante";
            this.lblFabricante.Click += new System.EventHandler(this.lblFabricante_Click);
            // 
            // gpbResultado
            // 
            this.gpbResultado.Controls.Add(this.txtCorrerCarrera);
            this.gpbResultado.Controls.Add(this.btnCorrerCarrera);
            this.gpbResultado.Location = new System.Drawing.Point(33, 398);
            this.gpbResultado.Name = "gpbResultado";
            this.gpbResultado.Size = new System.Drawing.Size(246, 154);
            this.gpbResultado.TabIndex = 3;
            this.gpbResultado.TabStop = false;
            this.gpbResultado.Text = "Resultado";
            // 
            // txtCorrerCarrera
            // 
            this.txtCorrerCarrera.Location = new System.Drawing.Point(3, 30);
            this.txtCorrerCarrera.Multiline = true;
            this.txtCorrerCarrera.Name = "txtCorrerCarrera";
            this.txtCorrerCarrera.Size = new System.Drawing.Size(138, 113);
            this.txtCorrerCarrera.TabIndex = 1;
            this.txtCorrerCarrera.TextChanged += new System.EventHandler(this.txtCorrerCarrera_TextChanged);
            // 
            // btnCorrerCarrera
            // 
            this.btnCorrerCarrera.Location = new System.Drawing.Point(147, 19);
            this.btnCorrerCarrera.Name = "btnCorrerCarrera";
            this.btnCorrerCarrera.Size = new System.Drawing.Size(93, 45);
            this.btnCorrerCarrera.TabIndex = 0;
            this.btnCorrerCarrera.Text = "Correr Carrera";
            this.btnCorrerCarrera.UseVisualStyleBackColor = true;
            this.btnCorrerCarrera.Click += new System.EventHandler(this.btnCorrerCarrera_Click);
            // 
            // gpbListadoDeAutos
            // 
            this.gpbListadoDeAutos.Controls.Add(this.lsbAutos);
            this.gpbListadoDeAutos.Location = new System.Drawing.Point(303, 184);
            this.gpbListadoDeAutos.Name = "gpbListadoDeAutos";
            this.gpbListadoDeAutos.Size = new System.Drawing.Size(221, 368);
            this.gpbListadoDeAutos.TabIndex = 4;
            this.gpbListadoDeAutos.TabStop = false;
            this.gpbListadoDeAutos.Text = "Listado de Autos";
            this.gpbListadoDeAutos.Enter += new System.EventHandler(this.groupBox3_Enter);
            // 
            // lsbAutos
            // 
            this.lsbAutos.FormattingEnabled = true;
            this.lsbAutos.Location = new System.Drawing.Point(17, 28);
            this.lsbAutos.Name = "lsbAutos";
            this.lsbAutos.Size = new System.Drawing.Size(198, 329);
            this.lsbAutos.TabIndex = 0;
            this.lsbAutos.SelectedIndexChanged += new System.EventHandler(this.lsbAutos_SelectedIndexChanged);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(536, 591);
            this.Controls.Add(this.gpbListadoDeAutos);
            this.Controls.Add(this.gpbResultado);
            this.Controls.Add(this.gpbAuto);
            this.Controls.Add(this.gpbCarrera);
            this.Name = "Form1";
            this.Text = "Form1";
            this.gpbCarrera.ResumeLayout(false);
            this.gpbCarrera.PerformLayout();
            this.gpbAuto.ResumeLayout(false);
            this.gpbAuto.PerformLayout();
            this.gpbResultado.ResumeLayout(false);
            this.gpbResultado.PerformLayout();
            this.gpbListadoDeAutos.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btnCrearCarrera;
        private System.Windows.Forms.GroupBox gpbCarrera;
        private System.Windows.Forms.GroupBox gpbAuto;
        private System.Windows.Forms.GroupBox gpbResultado;
        private System.Windows.Forms.GroupBox gpbListadoDeAutos;
        private System.Windows.Forms.TextBox txtLugar;
        private System.Windows.Forms.Label lblLugar;
        private System.Windows.Forms.TextBox txtFecha;
        private System.Windows.Forms.Label lblFecha;
        private System.Windows.Forms.TextBox txtNombre;
        private System.Windows.Forms.Label lblNombre;
        private System.Windows.Forms.Button btnAgregarAuto;
        private System.Windows.Forms.TextBox txtNombrePiloto;
        private System.Windows.Forms.Label lblNombrePiloto;
        private System.Windows.Forms.Label lblFabricante;
        private System.Windows.Forms.ComboBox cmbFabricante;
        private System.Windows.Forms.ListBox lsbAutos;
        private System.Windows.Forms.Button btnCorrerCarrera;
        private System.Windows.Forms.TextBox txtCorrerCarrera;
    }
}

/*namespace CarreraUI
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.btnCrearCarrera = new System.Windows.Forms.Button();
            this.gpbCarrera = new System.Windows.Forms.GroupBox();
            this.txtLugar = new System.Windows.Forms.TextBox();
            this.lblLugar = new System.Windows.Forms.Label();
            this.txtFecha = new System.Windows.Forms.TextBox();
            this.lblFecha = new System.Windows.Forms.Label();
            this.txtNombre = new System.Windows.Forms.TextBox();
            this.lblNombre = new System.Windows.Forms.Label();
            this.gpbAuto = new System.Windows.Forms.GroupBox();
            this.cmbFabricante = new System.Windows.Forms.ComboBox();
            this.btnAgregarAuto = new System.Windows.Forms.Button();
            this.txtNombrePiloto = new System.Windows.Forms.TextBox();
            this.lblNombrePiloto = new System.Windows.Forms.Label();
            this.lblFabricante = new System.Windows.Forms.Label();
            this.gpbResultado = new System.Windows.Forms.GroupBox();
            this.txtCorrerCarrera = new System.Windows.Forms.TextBox();
            this.btnCorrerCarrera = new System.Windows.Forms.Button();
            this.gpbListadoDeAutos = new System.Windows.Forms.GroupBox();
            this.lsbAutos = new System.Windows.Forms.ListBox();
            this.gpbCarrera.SuspendLayout();
            this.gpbAuto.SuspendLayout();
            this.gpbResultado.SuspendLayout();
            this.gpbListadoDeAutos.SuspendLayout();
            this.SuspendLayout();
            // 
            // btnCrearCarrera
            // 
            this.btnCrearCarrera.Location = new System.Drawing.Point(18, 81);
            this.btnCrearCarrera.Name = "btnCrearCarrera";
            this.btnCrearCarrera.Size = new System.Drawing.Size(103, 38);
            this.btnCrearCarrera.TabIndex = 0;
            this.btnCrearCarrera.Text = "Crear Carrera";
            this.btnCrearCarrera.UseVisualStyleBackColor = true;
            this.btnCrearCarrera.Click += new System.EventHandler(this.button1_Click);
            // 
            // gpbCarrera
            // 
            this.gpbCarrera.Controls.Add(this.txtLugar);
            this.gpbCarrera.Controls.Add(this.lblLugar);
            this.gpbCarrera.Controls.Add(this.txtFecha);
            this.gpbCarrera.Controls.Add(this.lblFecha);
            this.gpbCarrera.Controls.Add(this.txtNombre);
            this.gpbCarrera.Controls.Add(this.lblNombre);
            this.gpbCarrera.Controls.Add(this.btnCrearCarrera);
            this.gpbCarrera.Location = new System.Drawing.Point(12, 25);
            this.gpbCarrera.Name = "gpbCarrera";
            this.gpbCarrera.Size = new System.Drawing.Size(512, 151);
            this.gpbCarrera.TabIndex = 1;
            this.gpbCarrera.TabStop = false;
            this.gpbCarrera.Text = "Carrera";
            this.gpbCarrera.Enter += new System.EventHandler(this.grpCarrera_Enter);
            // 
            // txtLugar
            // 
            this.txtLugar.Location = new System.Drawing.Point(339, 45);
            this.txtLugar.Name = "txtLugar";
            this.txtLugar.Size = new System.Drawing.Size(147, 20);
            this.txtLugar.TabIndex = 6;
            this.txtLugar.TextChanged += new System.EventHandler(this.txtLugar_TextChanged);
            // 
            // lblLugar
            // 
            this.lblLugar.AutoSize = true;
            this.lblLugar.Location = new System.Drawing.Point(339, 20);
            this.lblLugar.Name = "lblLugar";
            this.lblLugar.Size = new System.Drawing.Size(34, 13);
            this.lblLugar.TabIndex = 5;
            this.lblLugar.Text = "Lugar";
            this.lblLugar.Click += new System.EventHandler(this.label3_Click);
            // 
            // txtFecha
            // 
            this.txtFecha.Location = new System.Drawing.Point(173, 45);
            this.txtFecha.Name = "txtFecha";
            this.txtFecha.Size = new System.Drawing.Size(147, 20);
            this.txtFecha.TabIndex = 4;
            // 
            // lblFecha
            // 
            this.lblFecha.AutoSize = true;
            this.lblFecha.Location = new System.Drawing.Point(173, 20);
            this.lblFecha.Name = "lblFecha";
            this.lblFecha.Size = new System.Drawing.Size(37, 13);
            this.lblFecha.TabIndex = 3;
            this.lblFecha.Text = "Fecha";
            this.lblFecha.Click += new System.EventHandler(this.lblFecha_Click);
            // 
            // txtNombre
            // 
            this.txtNombre.Location = new System.Drawing.Point(15, 45);
            this.txtNombre.Name = "txtNombre";
            this.txtNombre.Size = new System.Drawing.Size(147, 20);
            this.txtNombre.TabIndex = 2;
            this.txtNombre.TextChanged += new System.EventHandler(this.txtNombre_TextChanged);
            // 
            // lblNombre
            // 
            this.lblNombre.AutoSize = true;
            this.lblNombre.Location = new System.Drawing.Point(15, 20);
            this.lblNombre.Name = "lblNombre";
            this.lblNombre.Size = new System.Drawing.Size(44, 13);
            this.lblNombre.TabIndex = 1;
            this.lblNombre.Text = "Nombre";
            this.lblNombre.Click += new System.EventHandler(this.label1_Click);
            // 
            // gpbAuto
            // 
            this.gpbAuto.Controls.Add(this.cmbFabricante);
            this.gpbAuto.Controls.Add(this.btnAgregarAuto);
            this.gpbAuto.Controls.Add(this.txtNombrePiloto);
            this.gpbAuto.Controls.Add(this.lblNombrePiloto);
            this.gpbAuto.Controls.Add(this.lblFabricante);
            this.gpbAuto.Location = new System.Drawing.Point(19, 184);
            this.gpbAuto.Name = "gpbAuto";
            this.gpbAuto.Size = new System.Drawing.Size(260, 199);
            this.gpbAuto.TabIndex = 2;
            this.gpbAuto.TabStop = false;
            this.gpbAuto.Text = "Auto";
            this.gpbAuto.Enter += new System.EventHandler(this.gpbAuto_Enter);
            // 
            // cmbFabricante
            // 
            this.cmbFabricante.FormattingEnabled = true;
            this.cmbFabricante.Location = new System.Drawing.Point(11, 44);
            this.cmbFabricante.Name = "cmbFabricante";
            this.cmbFabricante.Size = new System.Drawing.Size(146, 21);
            this.cmbFabricante.TabIndex = 8;
            this.cmbFabricante.SelectedIndexChanged += new System.EventHandler(this.cmbFabricante_SelectedIndexChanged);
            // 
            // btnAgregarAuto
            // 
            this.btnAgregarAuto.Location = new System.Drawing.Point(14, 141);
            this.btnAgregarAuto.Name = "btnAgregarAuto";
            this.btnAgregarAuto.Size = new System.Drawing.Size(97, 43);
            this.btnAgregarAuto.TabIndex = 7;
            this.btnAgregarAuto.Text = "Agregar Auto";
            this.btnAgregarAuto.UseVisualStyleBackColor = true;
            this.btnAgregarAuto.Click += new System.EventHandler(this.btnAgregarAuto_Click);
            // 
            // txtNombrePiloto
            // 
            this.txtNombrePiloto.Location = new System.Drawing.Point(11, 105);
            this.txtNombrePiloto.Name = "txtNombrePiloto";
            this.txtNombrePiloto.Size = new System.Drawing.Size(147, 20);
            this.txtNombrePiloto.TabIndex = 6;
            this.txtNombrePiloto.TextChanged += new System.EventHandler(this.txtNombrePiloto_TextChanged);
            // 
            // lblNombrePiloto
            // 
            this.lblNombrePiloto.AutoSize = true;
            this.lblNombrePiloto.Location = new System.Drawing.Point(11, 80);
            this.lblNombrePiloto.Name = "lblNombrePiloto";
            this.lblNombrePiloto.Size = new System.Drawing.Size(90, 13);
            this.lblNombrePiloto.TabIndex = 5;
            this.lblNombrePiloto.Text = "Nombre del Piloto";
            // 
            // lblFabricante
            // 
            this.lblFabricante.AutoSize = true;
            this.lblFabricante.Location = new System.Drawing.Point(11, 25);
            this.lblFabricante.Name = "lblFabricante";
            this.lblFabricante.Size = new System.Drawing.Size(57, 13);
            this.lblFabricante.TabIndex = 3;
            this.lblFabricante.Text = "Fabricante";
            this.lblFabricante.Click += new System.EventHandler(this.lblFabricante_Click);
            // 
            // gpbResultado
            // 
            this.gpbResultado.Controls.Add(this.txtCorrerCarrera);
            this.gpbResultado.Controls.Add(this.btnCorrerCarrera);
            this.gpbResultado.Location = new System.Drawing.Point(33, 398);
            this.gpbResultado.Name = "gpbResultado";
            this.gpbResultado.Size = new System.Drawing.Size(246, 154);
            this.gpbResultado.TabIndex = 3;
            this.gpbResultado.TabStop = false;
            this.gpbResultado.Text = "Resultado";
            // 
            // txtCorrerCarrera
            // 
            this.txtCorrerCarrera.Location = new System.Drawing.Point(3, 30);
            this.txtCorrerCarrera.Multiline = true;
            this.txtCorrerCarrera.Name = "txtCorrerCarrera";
            this.txtCorrerCarrera.Size = new System.Drawing.Size(138, 113);
            this.txtCorrerCarrera.TabIndex = 1;
            this.txtCorrerCarrera.TextChanged += new System.EventHandler(this.txtCorrerCarrera_TextChanged);
            // 
            // btnCorrerCarrera
            // 
            this.btnCorrerCarrera.Location = new System.Drawing.Point(147, 19);
            this.btnCorrerCarrera.Name = "btnCorrerCarrera";
            this.btnCorrerCarrera.Size = new System.Drawing.Size(93, 45);
            this.btnCorrerCarrera.TabIndex = 0;
            this.btnCorrerCarrera.Text = "Correr Carrera";
            this.btnCorrerCarrera.UseVisualStyleBackColor = true;
            this.btnCorrerCarrera.Click += new System.EventHandler(this.btnCorrerCarrera_Click);
            // 
            // gpbListadoDeAutos
            // 
            this.gpbListadoDeAutos.Controls.Add(this.lsbAutos);
            this.gpbListadoDeAutos.Location = new System.Drawing.Point(303, 184);
            this.gpbListadoDeAutos.Name = "gpbListadoDeAutos";
            this.gpbListadoDeAutos.Size = new System.Drawing.Size(221, 368);
            this.gpbListadoDeAutos.TabIndex = 4;
            this.gpbListadoDeAutos.TabStop = false;
            this.gpbListadoDeAutos.Text = "Listado de Autos";
            this.gpbListadoDeAutos.Enter += new System.EventHandler(this.groupBox3_Enter);
            // 
            // lsbAutos
            // 
            this.lsbAutos.FormattingEnabled = true;
            this.lsbAutos.Location = new System.Drawing.Point(17, 28);
            this.lsbAutos.Name = "lsbAutos";
            this.lsbAutos.Size = new System.Drawing.Size(198, 329);
            this.lsbAutos.TabIndex = 0;
            this.lsbAutos.SelectedIndexChanged += new System.EventHandler(this.lsbAutos_SelectedIndexChanged);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(536, 591);
            this.Controls.Add(this.gpbListadoDeAutos);
            this.Controls.Add(this.gpbResultado);
            this.Controls.Add(this.gpbAuto);
            this.Controls.Add(this.gpbCarrera);
            this.Name = "Form1";
            this.Text = "Form1";
            this.gpbCarrera.ResumeLayout(false);
            this.gpbCarrera.PerformLayout();
            this.gpbAuto.ResumeLayout(false);
            this.gpbAuto.PerformLayout();
            this.gpbResultado.ResumeLayout(false);
            this.gpbResultado.PerformLayout();
            this.gpbListadoDeAutos.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btnCrearCarrera;
        private System.Windows.Forms.GroupBox gpbCarrera;
        private System.Windows.Forms.GroupBox gpbAuto;
        private System.Windows.Forms.GroupBox gpbResultado;
        private System.Windows.Forms.GroupBox gpbListadoDeAutos;
        private System.Windows.Forms.TextBox txtLugar;
        private System.Windows.Forms.Label lblLugar;
        private System.Windows.Forms.TextBox txtFecha;
        private System.Windows.Forms.Label lblFecha;
        private System.Windows.Forms.TextBox txtNombre;
        private System.Windows.Forms.Label lblNombre;
        private System.Windows.Forms.Button btnAgregarAuto;
        private System.Windows.Forms.TextBox txtNombrePiloto;
        private System.Windows.Forms.Label lblNombrePiloto;
        private System.Windows.Forms.Label lblFabricante;
        private System.Windows.Forms.ComboBox cmbFabricante;
        private System.Windows.Forms.ListBox lsbAutos;
        private System.Windows.Forms.Button btnCorrerCarrera;
        private System.Windows.Forms.TextBox txtCorrerCarrera;
    }
}

*/
