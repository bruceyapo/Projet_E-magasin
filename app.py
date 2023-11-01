from flask import Flask, render_template, request,  redirect, url_for
import pyodbc  as odbccon
conn = odbccon.connect("Driver={ODBC Driver 17 for SQL Server};"
                      "Server=DESKTOP-QQGKONI\SQLEXPRESS;"
                      "Database=e_magasin;"
                      "Trusted_Connection=yes;")

cursor = conn.cursor()
# cursor.execute('SELECT * FROM Table')

# for row in cursor:
#     print('row = %r' % (row,))

app = Flask(__name__)

## Magasin
@app.route("/")
def Connexion():
    return render_template("connexion.html")

@app.route("/Accueil/")
def index():
    return render_template("Base.html")

@app.route("/Magasin/")
def Magasin():
    return render_template("Magasin.html")

@app.route("/Ajouter/")
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


##Produits

@app.route("/List_produit/")
def Produit():
    # Exécution de la requête de sélection
    cursor = conn.cursor()
    cursor.execute( "SELECT Id, Nom_produit, Categorie, PrixUnitaire, Description FROM Produit ")
    list = cursor.fetchall()
    # Commit des modifications
    conn.commit()
    # conn.close()
    return render_template("Produit.html", list=list)

@app.route("/Ajout_produit/", methods=['GET'])
def Ajout_produit():
    return render_template("Ajout_produit.html")
# --------------------------------
# @app.route('/Ajouter/')
# def Ajouter():
#     return render_template("Ajouter.html")

# @app.route('/submit_add/', methods=['POST'])
# def submit_add():
#     Nom = request.form['Nom_magasin']
#     Adresse = request.form['Adresse_magasin']
#     Telephone = request.form['Telephone']
#     email = request.form['mail']

#     cursor = conn.cursor()
#     cursor.execute(
#             "INSERT INTO Magasin (Nom_magasin, Addresse_magasin, Telephone, E_mail) VALUES (?, ?, ?, ?)",
#             (Nom, Adresse, Telephone, email)
#         )
#     conn.commit()
#     cursor.close()
#     return render_template("Magasin.html")
# ---------------------------------
#Route pour traiter le formulaire d'ajout
@app.route("/Succes_ajout_produit/", methods=['POST'])
def Succes_ajout_produit():
      
    # Récupération des données du formulaire
    Nom_produit = request.form["Nom_produit"]
    Categorie = request.form["Categorie"]
    PrixUnitaire = request.form["PrixUnitaire"]
    Description = request.form["Description"]

    # Traitement des données
    list = {
        "Nom_produit": Nom_produit,
        "Categorie": Categorie,
        "PrixUnitaire": PrixUnitaire,
        "Description": Description
    }
    # Exécution de la requête d'insertion
    cursor = conn.cursor()
    cursor.execute(
        f"INSERT INTO Produit (Nom_produit, Categorie, PrixUnitaire,Description) VALUES ('{list['Nom_produit']}', '{list['Categorie']}', '{list['PrixUnitaire']}', '{list['Description']}')"
    )
    cursor = conn.cursor()
    cursor.execute( "SELECT Id, Nom_produit, Categorie, PrixUnitaire, Description FROM Produit ")
    listaj = cursor.fetchall()
    # Commit des modifications
    conn.commit()
    # conn.close()
    return render_template("Succes_ajout_produit.html", list=list ,listaj=listaj)

#Route pour traiter le formulaire de Modification
@app.route("/Modifier_produit/")
def Modifier_produit():
    #cursor = conn.cursor()
    #cursor.execute( "SELECT Id, Nom_produit, Categorie, PrixUnitaire, Description FROM Produit ")
    #list = cursor.fetchall()
    
    # Commit des modifications
    #conn.commit()
    #conn.close()
    return render_template("Modifier_produit.html")

@app.route("/Succes_modif_prod/<int:Id>", methods=["POST"])
def Succes_modif_prod():
    cursor = conn.cursor()
    Nom_produit = request.form["Nom_produit"]
    Categorie = request.form["Categorie"]
    PrixUnitaire = request.form["PrixUnitaire"]
    Description = request.form["Description"]

    # Traitement des données
    list = {
        "Nom_produit": Nom_produit,
        "Categorie": Categorie,
        "PrixUnitaire": PrixUnitaire,
        "Description": Description
    }
    cursor.execute(f"UPDATE Produit SET Nom_produit = '{list.Nom_produit}', Categorie = '{list.Categorie}', PrixUnitaire = '{list.PrixUnitaire}', Description = '{list.Description}' ")
    conn.commit()
    cursor.close()
    return redirect("url_for('Produit')")


@app.route("/Supprimer_produit/")
def Supprimer_produit():
    return render_template("Supprimer_produit.html")

@app.route("/Succes_supp_prod/")
def Succes_supp_prod():
    return render_template("Succes_supp_prod.html")

if __name__ == "__main__":
    app.run(debug=True)