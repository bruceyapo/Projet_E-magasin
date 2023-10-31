#importation des librairies
from flask import Flask, render_template,request,redirect, url_for
import pyodbc as odbc

#definir l'app
app = Flask(__name__)

# Connexion à la base de données SQL SERVER
conn_str = "Driver={ODBC Driver 17 for SQL Server};Server=Geek_Machine\\SQLEXPRESS;Database=e_magasin;Trusted_connection=yes"
conn = odbc.connect(conn_str)

app.config['SQL_CONN'] = conn

#création des routes de l'app


@app.route("/Magasin/")
def Magasin():
    cursor = conn.cursor()
    cursor.execute( "SELECT Id, Nom_magasin, Addresse_magasin,Telephone, E_mail FROM Magasin ")
    data = cursor.fetchall()
    # conn.close()
    return render_template("Magasin.html", data=data)

@app.route('/Ajouter/')
def Ajouter():
    return render_template("Ajouter.html")

@app.route('/submit_add/', methods=['POST'])
def submit_add():
    Nom = request.form['Nom_magasin']
    Addresse_magasin = request.form['Addresse_magasin']
    Telephone = request.form['Telephone']
    email = request.form['mail']

    cursor = conn.cursor()
    cursor.execute(
            "INSERT INTO Magasin (Nom_magasin, Addresse_magasin, Telephone, E_mail) VALUES (?, ?, ?, ?)",
            (Nom, Addresse_magasin, Telephone, email)
        )
    conn.commit()
    # cursor.close()
    return render_template("Magasin.html")


if __name__ == "__main__":
    app.run(debug=True)