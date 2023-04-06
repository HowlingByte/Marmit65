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


def accueil():
    #no input argument
    #return name and image of all families of recipes
    pass

def famille(idFamille):
    #get name and image of the family idFamille
    pass

def recette(idRecette):
    #get name and image of the recipe idRecette
    pass


conn = sqlite3.connect('marmita.db')
cur = conn.cursor()

cur.execute("SELECT * FROM famille")

conn.commit()

cur.close()
conn.close()