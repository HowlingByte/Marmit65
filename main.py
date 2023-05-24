"""
Fichier principal de l'application web Marmita.
Ce fichier contient toutes les routes de l'application web.
Il permet de lancer le serveur en local.
"""
import sqlite3
from bottle import get, post, request, route, run, view, static_file, response, error, redirect

class Recette():
    """
    Classe qui représente une recette. Une recette possède les attributs suivants:
    - Id: l'identifiant de la recette dans la base de données
    - nom: le nom de la recette
    - image: l'image de la recette
    - preparation: le temps de préparation de la recette
    - cuisson: le temps de cuisson de la recette
    - nombreDePersonnes: le nombre de personnes pour lesquelles la recette est prévue
    - difficulte: la difficulté de la recette
    - ingredients: la liste des ingrédients de la recette
    - etapes: la liste des étapes de la recette
    - famille: la famille de la recette
    """
    def __init__(self,Id,nom,image,preparation,cuisson,nbpers,diff,ingredients,etapes,famille):
        self.Id=Id
        self.nom=nom
        self.image=image
        self.preparation=preparation
        self.cuisson=cuisson
        self.nombreDePersonnes=nbpers
        self.difficulte=diff
        self.ingredients=ingredients
        self.etapes=etapes
        self.famille=famille

class Famille():
    """
    Classe qui représente une famille de recettes. Une famille possède les attributs suivants:
    - Id: l'identifiant de la famille dans la base de données
    - nom: le nom de la famille
    - image: l'image de la famille
    """
    def __init__(self, Id,nom,image):
        self.Id=Id
        self.nom=nom
        self.image=image

class Ingredient():
    """
    Classe qui représente un ingrédient. Un ingrédient possède les attributs suivants:
    - Id: l'identifiant de l'ingrédient dans la base de données
    - nom: le nom de l'ingrédient
    - quantite: la quantité de l'ingrédient
    - unite: l'unité de mesure de la quantité de l'ingrédient
    """
    def __init__(self,Id, nom, quantite,unite=None):
        self.Id=Id
        self.nom=nom
        self.quantite=quantite
        self.unite=unite

class Etape():
    """
    Classe qui re présente une étape de recette. Une étape possède les attributs suivants:
    - num: le numéro de l'étape dans la recette
    - texte: le texte de l'étape
    """
    def __init__(self,num,texte):
        self.num=num
        self.texte=texte

def open_sql():
    """
    Fonction qui permet d'ouvrir une connexion à la base de données.
    :return: le connecteur et le curseur de la base de données
    """
    conn = sqlite3.connect('database/marmita.db')
    cur = conn.cursor()
    return conn,cur

def close_sql(cur):
    """
    Fonction qui permet de fermer une connexion à la base de données.
    :param cur: le curseur de la base de données
    """
    cur.close()

@route('/style.css')
@view('static/css/style.css')
def style():
    response.content_type="text/css"
    return {}

@route('/')
@view("template/accueil.tpl")
def accueil():
    conn, cur = open_sql()
    cur.execute("SELECT id, nom, image FROM famille")
    familles = []
    for row in cur:
        famille_id = row[0]
        famille_nom = row[1]
        famille_image = row[2]
        famille = Famille(famille_id, famille_nom, famille_image)
        familles.append(famille)
    close_sql(cur)
    return dict(listeFamille=familles)

@route('/famille',method='get')
@view("template/famille.tpl")
def famille():
    id=request.query.id # type: ignore

    conn, cur = open_sql()

    # Requête SQL pour récupérer les recettes d'une famille
    cur.execute("SELECT * FROM recettes WHERE id_famille = ?", (id,))
    listeRecettes = []
    for row in cur:
        recette_id = row[0]
        recette_nom = row[1]
        recette_image = row[2]
        recette_famille = row[6]
        recette = Recette(recette_id, recette_nom, recette_image, None, None, None, None, None, None, recette_famille)
        listeRecettes.append(recette)

    cur.execute("SELECT nom FROM famille WHERE ID = ?", (id,))
    nom = cur.fetchone()
    conn.commit()

    close_sql(cur)

    return dict(listeRecettes=listeRecettes, nom=nom[0], id=id)

# Affichage d'une recette
@route('/recettes/<id>')
@view("template/recette.tpl")
def recettes(id):
    conn, cur=open_sql()

    # Requête 1 (attributs de la table Recettes)
    cur.execute("SELECT * FROM Recettes WHERE ID=?", (id,))
    infosRecette = cur.fetchone()
    conn.commit()

    recette_id = infosRecette[0]
    recette_nom = infosRecette[1]
    recette_image = infosRecette[2]
    recette_nb_pers = infosRecette[3]
    recette_cuisson = infosRecette[4]
    recette_difficulte = infosRecette[5]
    recette_famille = infosRecette[6]

    # Requête pour récupérer le nom de la famille
    cur.execute("SELECT Nom FROM Famille WHERE ID=?", (recette_famille,))
    nomFamille = cur.fetchone()
    conn.commit()

    # Requête pour récupérer les ingrédients de la recette
    cur.execute("SELECT Ingredients.ID, Ingredients.Nom, Quantite, Unite FROM IngredientsDeRecette INNER JOIN Ingredients ON Ingredients.ID=IngredientsDeRecette.ID_ingredients WHERE ID_recettes=?", (recette_id,))
    listeIngredients = []
    for row in cur:
        ingredient_id = row[0]
        ingredient_nom = row[1]
        ingredient_quantite = row[2]
        ingredient_unite = row[3]
        ingredient = Ingredient(ingredient_id, ingredient_nom, ingredient_quantite, ingredient_unite)
        listeIngredients.append(ingredient)
    conn.commit()

    # Requête pour récupérer les étapes de la recette
    cur.execute("SELECT Numero, Descriptif FROM EtapesDeRecette WHERE ID_recettes=?", (recette_id,))
    etapesRecette = []
    for row in cur:
        etape_num = row[0]
        etape_texte = row[1]
        etape = Etape(etape_num, etape_texte)
        etapesRecette.append(etape)
    conn.commit()

    close_sql(cur)

    famille = Famille(recette_famille, nomFamille[0], "")
    recette = Recette(recette_id, recette_nom, recette_image, None, recette_cuisson, recette_nb_pers, recette_difficulte, listeIngredients, etapesRecette, famille)

    return dict(recette=recette)

@route('/chercheRecettes', method='POST')
@view("template/chercheRecettes.tpl")
def rechercher():
    # Récupérer les données du formulaire
    recette_recherchee = request.forms.get('recette')

    if recette_recherchee!="":
        mots_cles = recette_recherchee.split(" ")
        condition = "LIKE '%" + mots_cles[0] + "%'"
        for i in range(1, len(mots_cles)):
            condition += " AND nom LIKE '%" + mots_cles[i] + "%'"
    else:
        condition = "LIKE '%%'"


    conn, cur = open_sql()

    # Requête SQL pour récupérer les recettes d'une famille
    cur.execute("SELECT * FROM recettes WHERE nom " + condition)
    listeRecettes = []
    for row in cur:
        recette_id = row[0]
        recette_nom = row[1]
        recette_image = row[2]
        recette_famille = row[6]
        recette = Recette(recette_id, recette_nom, recette_image, None, None, None, None, None, None, recette_famille)
        listeRecettes.append(recette)

    close_sql(cur)

    return dict(listeRecettes=listeRecettes, recherche=recette_recherchee)

@route('/contact')
@view("static/html/contact.html")
def contact():
    return {}

@route('/mentions')
@view("static/html/mentions.html")
def mentions():
    return {}

@error(404)
@view("static/html/404.html")
def on_error404(error):
    return {}

# Route pour les images
@route('/image/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static/image/')

run(host='0.0.0.0', port=80)
#run(host='localhost', port=8080, debug=True)
