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
    return cur

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
    cur=open_sql()
    cur.execute("SELECT nom, image FROM famille")
    listeFamille = cur.fetchall()
    close_sql(cur)
    return dict(listeFamille=listeFamille)

def famille(idFamille):
    cur=open_sql()
    cur.execute("SELECT nom, image FROM recettes WHERE ID = ?", (idFamille,))
    nom=[]
    image=[]
    for row in cur:
        nom.append(row[0])
        image.append(row[1])
    close_sql(cur)
    return {"nom" : nom, "image" : image}

def recette(idRecette):
    cur=open_sql()
    cur.execute("SELECT * FROM recettes WHERE ID = ?", (idRecette,))
    id=[]
    nom=[]
    image=[]
    nb_pers=[]
    cuisson=[]
    difficulte=[]
    id_famille=[]
    for row in cur:
        id.append(row[0])
        nom.append(row[1])
        image.append(row[2])
        nb_pers.append(row[3])
        cuisson.append(row[4])
        difficulte.append(row[5])
        id_famille.append(row[6])
    close_sql(cur)
    return {"id" : id, "nom" : nom, "image" : image, "nb_pers" : nb_pers, "cuisson" : cuisson, "difficulte" : difficulte, "id_famille" : id_famille}

@route('/contact')
@view("template/contact.tpl")
def contact():
    return {}

@route('/mentions')
@view("template/mentions.tpl")
def mentions():
    return {}

# Route pour les images
@route('/image/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='image/')

# Programme principal

run(host='localhost', port=8080, debug=True)
