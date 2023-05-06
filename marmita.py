import sqlite3

from bottle import get, post, request, route, run, view, static_file, response

def open_sql():
    conn = sqlite3.connect('marmita.db')
    cur = conn.cursor()
    return cur

# Page d'accueil
@route('/accueil')
@view("accueil.tpl")
def accueil():
    # votre code (plusieurs lignes)
    
    listeFamille = cur.fetchall()
    cur.close()
    conn.close()
    
    return dict(listeFamille=listeFamille)

# Pour acceder au fichier css relie au fichier accueil.tpl
@route('/styleAccueil.css')
@view('styleAccueil.css')
def style():
    response.content_type="text/css"
    return {}

# Affichage des recettes d'une famille
@route('/famille',method='get')
@view("famille.tpl")
def famille():
    id=request.query.id
    
    #Requete SQL pour recuperer les recettes d'une famille

    cur.execute("SELECT Nom FROM Famille WHERE ID=?",(id,))
    nom=cur.fetchone()
    conn.commit()
    
    cur.close()
    conn.close()
    return dict(listeRecettes=listeRecettes,nom=nom[0])

# Pour acceder au fichier css relie au fichier famille.tpl
@route('/styleFamille.css')
@view('styleFamille.css')
def style():
    response.content_type="text/css"
    return {}

# Affichage d'une recette
@route('/recettes/<id>')
@view("recette.tpl")
def recettes(id):
    conn = sqlite3.connect('MarmitonDB2.db')
    cur = conn.cursor()
    
    #requete 1 (attributs de la table Recettes)
    infosRecette=cur.fetchall()
    conn.commit()

    cur.execute("SELECT Nom FROM Famille WHERE ID=?",(infosRecette[0][7],))
    nomFamille=cur.fetchone()
    conn.commit()

    # Requete pour recuperer les ingredients de la recette
    
    listeIngredients=cur.fetchall()
    conn.commit()

    # Requete pour recuperer les etapes de la recette
    
    etapesRecette=cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    
    
    return dict(...)
    
# Route pour les images
@route('/images/<filename>')
def server_static(filename):
    return static_file(filename, root='images')



# Programme principal

run(host='localhost', port=8080, debug=True)

