from flask import Flask, render_template

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
    return render_template("Produit.html")

@app.route("/Ajout_produit/")
def Ajout_produit():
    return render_template("Ajout_produit.html")

@app.route("/Succes_ajout_produit/")
def Succes_ajout_produit():
    return render_template("Succes_ajout_produit.html")

@app.route("/Modifier_produit/")
def Modifier_produit():
    return render_template("Modifier_produit.html")

@app.route("/Succes_modif_prod/")
def Succes_modif_prod():
    return render_template("Succes_modif_prod.html")

@app.route("/Supprimer_produit/")
def Supprimer_produit():
    return render_template("Supprimer_produit.html")

@app.route("/Succes_supp_prod/")
def Succes_supp_prod():
    return render_template("Succes_supp_prod.html")

if __name__ == "__main__":
    app.run()