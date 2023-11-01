from flask import Flask, render_template, request
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
    data = {
        "Nom_produit": Nom_produit,
        "Categorie": Categorie,
        "PrixUnitaire": PrixUnitaire,
        "Description": Description
    }
    # Exécution de la requête d'insertion
    cursor = conn.cursor()
    cursor.execute(
        f"INSERT INTO Produit (Nom_produit, Categorie, PrixUnitaire,Description) VALUES ('{data['Nom_produit']}', '{data['Categorie']}', '{data['PrixUnitaire']}', '{data['Description']}')"
    )
    cursor = conn.cursor()
    cursor.execute( "SELECT Id, Nom_produit, Categorie, PrixUnitaire, Description FROM Produit ")
    listaj = cursor.fetchall()
    # Commit des modifications
    conn.commit()
    # conn.close()
    return render_template("Succes_ajout_produit.html", data=data ,listaj=listaj)

#Route pour traiter le formulaire de Modification
@app.route("/Modifier_produit/")
def Modifier_produit():
    return render_template("Modifier_produit.html")

@app.route("/Succes_modif_prod/", methods=["POST"])
def Succes_modif_prod():
    # Récupération des données du formulaire
    Nom_produit = request.form["Nom_produit"]
    Categorie = request.form["Categorie"]
    PrixUnitaire = request.form["PrixUnitaire"]
    Description = request.form["Description"]
    # Traitement des données
    data = {
        "Nom_produit": Nom_produit,
        "Categorie": Categorie,
        "PrixUnitaire": PrixUnitaire,
        "Description": Description
    }
    # Exécution de la requête de mise à jour
    cursor = conn.cursor()
    cursor.execute(
        f"UPDATE Produit SET Nom_produit = '{data['Nom_produit']}', Categorie = '{data['Categorie']}', PrixUnitaire = '{data['PrixUnitaire']}', Description = '{data['Description']}' WHERE Id = {data['Id']}"
    )
    # Commit des modifications
    #cursor.execute( "SELECT Id, Nom_produit, Categorie, PrixUnitaire, Description FROM Produit ")
    #listModif = cursor.fetchall()
    conn.commit()
    return render_template("Succes_modif_prod.html", data=data)


@app.route("/Supprimer_produit/")
def Supprimer_produit():
    return render_template("Supprimer_produit.html")

@app.route("/Succes_supp_prod/")
def Succes_supp_prod():
    return render_template("Succes_supp_prod.html")

if __name__ == "__main__":
    app.run(debug=True)