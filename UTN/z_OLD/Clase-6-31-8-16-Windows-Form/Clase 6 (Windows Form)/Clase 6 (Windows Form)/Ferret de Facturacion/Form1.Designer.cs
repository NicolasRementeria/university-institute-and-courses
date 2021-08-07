namespace Ferret_de_Facturacion
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
            this.txtN1 = new System.Windows.Forms.TextBox();
            this.txtN2 = new System.Windows.Forms.TextBox();
            this.txtN3 = new System.Windows.Forms.TextBox();
            this.lblN1 = new System.Windows.Forms.Label();
            this.lblN2 = new System.Windows.Forms.Label();
            this.lblN3 = new System.Windows.Forms.Label();
            this.btnSumar = new System.Windows.Forms.Button();
            this.btnProm = new System.Windows.Forms.Button();
            this.btnFinal = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // txtN1
            // 
            this.txtN1.Location = new System.Drawing.Point(18, 37);
            this.txtN1.Name = "txtN1";
            this.txtN1.Size = new System.Drawing.Size(85, 20);
            this.txtN1.TabIndex = 0;
            this.txtN1.TextChanged += new System.EventHandler(this.txtN1_TextChanged);
            // 
            // txtN2
            // 
            this.txtN2.Location = new System.Drawing.Point(18, 95);
            this.txtN2.Name = "txtN2";
            this.txtN2.Size = new System.Drawing.Size(84, 20);
            this.txtN2.TabIndex = 1;
            this.txtN2.TextChanged += new System.EventHandler(this.txtN2_TextChanged);
            // 
            // txtN3
            // 
            this.txtN3.Location = new System.Drawing.Point(21, 164);
            this.txtN3.Name = "txtN3";
            this.txtN3.Size = new System.Drawing.Size(77, 20);
            this.txtN3.TabIndex = 2;
            // 
            // lblN1
            // 
            this.lblN1.AutoSize = true;
            this.lblN1.Location = new System.Drawing.Point(23, 11);
            this.lblN1.Name = "lblN1";
            this.lblN1.Size = new System.Drawing.Size(53, 13);
            this.lblN1.TabIndex = 3;
            this.lblN1.Text = "Numero 1";
            // 
            // lblN2
            // 
            this.lblN2.AutoSize = true;
            this.lblN2.Location = new System.Drawing.Point(22, 79);
            this.lblN2.Name = "lblN2";
            this.lblN2.Size = new System.Drawing.Size(53, 13);
            this.lblN2.TabIndex = 4;
            this.lblN2.Text = "Numero 2";
            // 
            // lblN3
            // 
            this.lblN3.AutoSize = true;
            this.lblN3.Location = new System.Drawing.Point(18, 139);
            this.lblN3.Name = "lblN3";
            this.lblN3.Size = new System.Drawing.Size(53, 13);
            this.lblN3.TabIndex = 5;
            this.lblN3.Text = "Numero 3";
            // 
            // btnSumar
            // 
            this.btnSumar.Location = new System.Drawing.Point(174, 44);
            this.btnSumar.Name = "btnSumar";
            this.btnSumar.Size = new System.Drawing.Size(92, 38);
            this.btnSumar.TabIndex = 6;
            this.btnSumar.Text = "Sumar";
            this.btnSumar.UseVisualStyleBackColor = true;
            this.btnSumar.Click += new System.EventHandler(this.btnSumar_Click);
            // 
            // btnProm
            // 
            this.btnProm.Location = new System.Drawing.Point(174, 100);
            this.btnProm.Name = "btnProm";
            this.btnProm.Size = new System.Drawing.Size(91, 38);
            this.btnProm.TabIndex = 7;
            this.btnProm.Text = "Promedio";
            this.btnProm.UseVisualStyleBackColor = true;
            this.btnProm.Click += new System.EventHandler(this.btnProm_Click);
            // 
            // btnFinal
            // 
            this.btnFinal.Location = new System.Drawing.Point(174, 154);
            this.btnFinal.Name = "btnFinal";
            this.btnFinal.Size = new System.Drawing.Size(91, 39);
            this.btnFinal.TabIndex = 8;
            this.btnFinal.Text = "Preco final";
            this.btnFinal.UseVisualStyleBackColor = true;
            this.btnFinal.Click += new System.EventHandler(this.btnFinal_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 262);
            this.Controls.Add(this.btnFinal);
            this.Controls.Add(this.btnProm);
            this.Controls.Add(this.btnSumar);
            this.Controls.Add(this.lblN3);
            this.Controls.Add(this.lblN2);
            this.Controls.Add(this.lblN1);
            this.Controls.Add(this.txtN3);
            this.Controls.Add(this.txtN2);
            this.Controls.Add(this.txtN1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox txtN1;
        private System.Windows.Forms.TextBox txtN2;
        private System.Windows.Forms.TextBox txtN3;
        private System.Windows.Forms.Label lblN1;
        private System.Windows.Forms.Label lblN2;
        private System.Windows.Forms.Label lblN3;
        private System.Windows.Forms.Button btnSumar;
        private System.Windows.Forms.Button btnProm;
        private System.Windows.Forms.Button btnFinal;
    }
}

