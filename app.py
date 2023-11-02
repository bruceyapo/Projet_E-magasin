from flask import Flask, render_template, request,  redirect, url_for
import pyodbc  as odbccon
# from sqlalchemy import create_engine, Session, String
# from flask_sqlalchemy import SQLAlchemy

# cursor.execute('SELECT * FROM Table')

# for row in cursor:
#     print('row = %r' % (row,))

app = Flask(__name__)
conn = odbccon.connect("Driver={ODBC Driver 17 for SQL Server};"
                      "Server=DESKTOP-QQGKONI\SQLEXPRESS;"
                      "Database=e_magasin;"
                      "Trusted_Connection=yes;")

cursor = conn.cursor()
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
    # cursor = conn.cursor()
    cursor.execute( "SELECT Id, Nom_produit, Categorie, PrixUnitaire, Description FROM Produit ")
    list = cursor.fetchall()
    # Commit des modifications
    conn.commit()
    # conn.close()
    return render_template("Produit.html", list=list)

@app.route("/Ajout_produit/", methods=['GET'])
def Ajout_produit():
    return render_template("Ajout_produit.html")
#Route pour traiter le formulaire d'ajout
@app.route("/Succes_ajout_produit/", methods=['POST'])
def Succes_ajout_produit():
    cursor = conn.cursor()
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
    # cursor = conn.cursor()
    cursor.execute(
        f"INSERT INTO Produit (Nom_produit, Categorie, PrixUnitaire,Description) VALUES ('{list['Nom_produit']}', '{list['Categorie']}', '{list['PrixUnitaire']}', '{list['Description']}')"
    )
    # cursor = conn.cursor()
    cursor.execute( "SELECT Id, Nom_produit, Categorie, PrixUnitaire, Description FROM Produit ")
    list = cursor.fetchall()
    # Commit des modifications
    conn.commit()
    # conn.close()
    return render_template("Succes_ajout_produit.html", list=list)

#Route pour traiter le formulaire de Modification
@app.route("/Modifier_produit/<int:_id>" , methods=['GET'])
def Modifier_produit(_id):
    # cursor = conn.cursor()
    # cursor = conn.cursor()
    cursor.execute( "SELECT * FROM Produit WHERE Id = ?", _id)
    
    list = cursor.fetchall() 
    conn.commit()  
    return render_template("Modifier_produit.html", list=list)
    
    
@app.route("/Succes_modif_prod/<int:_id>", methods=['POST'])
def Succes_modif_prod(_id):
    # id= int(list.Id)
    # cursor = conn.cursor()
    Nom_produit = request.form["Nom_produit"]
    Categorie = request.form["Categorie"]
    PrixUnitaire = request.form["PrixUnitaire"]
    Description = request.form["Description"]
    # Traitement des données
    list= {
        "Nom_produit": Nom_produit,
        "Categorie": Categorie,
        "PrixUnitaire": PrixUnitaire,
        "Description": Description
    }
    cursor.execute("UPDATE Produit SET Nom_produit =?, Categorie =?, PrixUnitaire =?, Description =?, WHERE Id=? ", (list.Nom_produit, list.Categorie, list.PrixUnitaire, list.Description, _id))
    conn.commit()
    # cursor.close()
        # return redirect(url_for('Succes_modif_prod', list=list))
    cursor = conn.cursor()
    cursor.execute( "SELECT * FROM Produit WHERE Id = ?",_id)
    list = cursor.fetchall()
    conn.commit()
    return render_template("Succes_modif_prod.html", list=list)


@app.route("/Supprimer_produit/")
def Supprimer_produit():
    return render_template("Supprimer_produit.html")

@app.route("/Succes_supp_prod/")
def Succes_supp_prod():
    return render_template("Succes_supp_prod.html")

if __name__ == "__main__":
    app.run(debug=True)