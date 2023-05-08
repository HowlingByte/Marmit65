import sqlite3
from bottle import get, post, request, route, run, view, static_file, response, error, redirect

class Recette():
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
    def __init__(self, Id,nom,image):
        self.Id=Id
        self.nom=nom
        self.image=image

class Ingredient():
    def __init__(self,Id, nom, quantite,unite=None):
        self.Id=Id
        self.nom=nom
        self.quantite=quantite
        self.unite=unite

class Etape():
    def __init__(self,num,texte):
        self.num=num
        self.texte=texte

def open_sql():
    conn = sqlite3.connect('marmita.db')
    cur = conn.cursor()
    return conn,cur

def close_sql(cur):
    cur.close()

@route('/style.css')
@view('style.css')
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
    id=request.query.id

    conn, cur = open_sql()

    # Requête SQL pour récupérer les recettes d'une famille
    cur.execute("SELECT * FROM recettes WHERE id_famille = ?", (id,))
    listeRecettes = []
    for row in cur:
        recette_id = row[0]
        recette_nom = row[1]
        recette_image = row[2]
        recette_nb_pers = row[3]
        recette_cuisson = row[4]
        recette_difficulte = row[5]
        recette_famille = row[6]
        recette = Recette(recette_id, recette_nom, recette_image, None, recette_cuisson, recette_nb_pers, recette_difficulte, None, None, recette_famille)
        listeRecettes.append(recette)

    cur.execute("SELECT nom FROM famille WHERE ID = ?", (id,))
    nom = cur.fetchone()
    conn.commit()

    close_sql(cur)

    return dict(listeRecettes=listeRecettes, nom=nom[0])

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

@route('/contact')
@view("template/contact.tpl")
def contact():
    return {}

@route('/mentions')
@view("template/mentions.tpl")
def mentions():
    return {}

@error(404)
@view("template/404.tpl")
def on_error404(error):
    return {}

# Route pour les images
@route('/image/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='image/')

@route('/static/css/<filename:path>')
def serve_css(filename):
    return static_file(filename, root='static/css')

run(host='localhost', port=8080, debug=True)

