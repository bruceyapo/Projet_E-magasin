#importation des librairies
from flask import Flask, render_template,request
import pyodbc as odbc

app = Flask(__name__)

conn_str = "Driver={ODBC Driver 17 for SQL Server};Server=Geek_Machine\\SQLEXPRESS;Database=e_magasin;Trusted_connection=yes"
conn = odbc.connect(conn_str)
app.config['SQL_CONN'] = conn

@app.route('/Ajouter/', method=['GET','POST'])
def Ajouter():
    if request.method == 'GET':
         return render_template("Ajouter.html")
     
    if request.method == 'POST':
         Nom = request.form('Nom_magasin')
         Adresse = request.form('Adresse_magasin')
         Telephone = request.form('Telephone')
         email = request.form('mail')
         
    # Open a cursor
    cursor = conn.cursor()

     # Execute a SQL query to insert the new mag
    cursor.execute(
            "INSERT INTO Magasin (Nom_magasin, Addresse_magasin, Telephone, E_mail) VALUES (?, ?, ?, ?)",
            (Nom, Adresse, Telephone, email)
        )

    # Commit the changes to the database
    conn.commit()

        # Close the cursor
    cursor.close()

    return 'Magasin added successfully'

if __name__ == "__main__":
    app.run(debug=True)
    


#création des routes de l'app
@app.route("/")
def Connexion():
    return render_template("connexion.html")

@app.route("/Accueil/")
def index():
    return render_template("Base.html")

@app.route("/Magasin/")
def Magasin():
    return render_template("Magasin.html")

@app.route('/Ajouter/')
def Ajouter():
    return render_template("Ajouter.html")

@app.route("/Succes/")
def Succes():
    return render_template("Succès.html")

@app.route("/Modifier/")
def Modifier():
    return render_template("Modifier.html")

@app.route("/Succes_modif/")
def Succes_modif():
    return render_template("Succes_modif.html")

@app.route("/Supprimer/")
def Supprimer():
    return render_template("Supprimer.html")

@app.route("/Succes_supp/")
def Succes_supp():
    return render_template("Succes_supp.html")
