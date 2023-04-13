import sqlite3

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

conn = sqlite3.connect('marmita.db')
cur = conn.cursor()

def accueil():
    cur.execute("SELECT * FROM famille")
    cur.close()
    return cur.fetchall()

def famille(idFamille):
    cur.execute("SELECT nom, image FROM recettes WHERE ID = ?", (idFamille,))
    cur.close()
    return cur.fetchall()

def recette(idRecette):
    cur.execute("SELECT * FROM recettes WHERE ID = ?", (idRecette,))
    cur.close()
    return cur.fetchall()

cur.execute("SELECT * FROM famille")
conn.commit()
conn.close()