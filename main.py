"""
Fichier principal de l'application web Marmita.
Ce fichier contient toutes les routes de l'application web.
Il permet de lancer le serveur en local.
"""
import sqlite3
from bottle import request, route, run, view, static_file, error, HTTPResponse
# from bottle import get, post, request, route, run, view, static_file, response, error, redirect

DATABASE = 'database/marmita.db'


class Famille():  # pylint: disable=R0903
    """
    Classe qui représente une famille de recettes. Une famille possède les attributs suivants:
    - Id: l'identifiant de la famille dans la base de données
    - nom: le nom de la famille
    - image: l'image de la famille
    """

    def __init__(
            self: object,
            famille_id: int,
            nom: str,
            image: str
        ):

        self.famille_id: int = famille_id
        self.nom: str = nom
        self.image: str = image


class Ingredient():  # pylint: disable=R0903
    """
    Classe qui représente un ingrédient. Un ingrédient possède les attributs suivants:
    - Id: l'identifiant de l'ingrédient dans la base de données
    - nom: le nom de l'ingrédient
    - quantite: la quantité de l'ingrédient
    - unite: l'unité de mesure de la quantité de l'ingrédient
    """

    def __init__(
            self: object,
            ingredient_id: int,
            nom: str,
            quantite: int,
            unite: str = None
        ):

        self.ingredient_id: int = ingredient_id
        self.nom: str = nom
        self.quantite: int = quantite
        self.unite: str = unite


class Etape():  # pylint: disable=R0903
    """
    Classe qui re présente une étape de recette. Une étape possède les attributs suivants:
    - num: le numéro de l'étape dans la recette
    - texte: le texte de l'étape
    """

    def __init__(
            self: object,
            num: int,
            texte: str
        ):

        self.num: int = num
        self.texte: str = texte


class Recette():  # pylint: disable=R0903, R0902
    """
    Classe qui représente une recette. Une recette possède les attributs suivants:
    - Id: l'identifiant de la recette dans la base de données
    - nom: le nom de la recette
    - image: l'image de la recette
    - preparation: le temps de préparation de la recette
    - cuisson: le temps de cuisson de la recette
    - nombre_de_personnes: le nombre de personnes pour lesquelles la recette est prévue
    - difficulte: la difficulté de la recette
    - ingredients: la liste des ingrédients de la recette
    - etapes: la liste des étapes de la recette
    - famille: la famille de la recette
    """

    def __init__(  # pylint: disable=R0913
            self: object,
            recette_id: int,
            nom: str,
            image: str,
            cuisson: int,
            nbpers: int,
            diff: int,
            ingredients: Ingredient,
            etapes: Etape,
            famille_recette: int
        ):

        self.recette_id: int = recette_id
        self.nom: str = nom
        self.image: str = image
        self.cuisson: int = cuisson
        self.nombre_de_personnes: int = nbpers
        self.difficulte: int = diff
        self.ingredients: Ingredient = ingredients
        self.etapes: Etape = etapes
        self.famille: int = famille_recette


def open_sql(database=DATABASE):
    """
    Fonction qui permet d'ouvrir une connexion à la base de données.
    :return: le connecteur et le curseur de la base de données
    """
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    return conn, cur


def close_sql(cur):
    """
    Fonction qui permet de fermer une connexion à la base de données.
    :param cur: le curseur de la base de données
    """
    cur.close()


@route('/')
@view("template/accueil.tpl")
def accueil():
    """
    Fonction qui permet d'afficher la page d'accueil.
    """
    _, cur = open_sql()
    cur.execute("SELECT id, nom, image FROM famille")

    liste_familles = []
    for row in cur:
        famille_id = row[0]
        famille_nom = row[1]
        famille_image = row[2]
        famille_obj = Famille(famille_id, famille_nom, famille_image)
        liste_familles.append(famille_obj)

    close_sql(cur)

    return {"listeFamille": liste_familles}


@route('/famille', method='get')
@view("template/famille.tpl")
def famille():
    """
    Fonction qui permet d'afficher la page d'une famille.
    """
    try:
        id_request = request.query.id  # type: ignore # pylint: disable=no-member

        conn, cur = open_sql()

        # Requête SQL pour récupérer les recettes d'une famille
        cur.execute("SELECT * FROM recettes WHERE id_famille = ?",
                    (id_request,))
        liste_recettes = []
        for row in cur:
            recette_id = row[0]
            recette_nom = row[1]
            recette_image = row[2]
            recette_famille = row[6]
            recette = Recette(recette_id, recette_nom, recette_image,
                              None, None, None, None, None, recette_famille)
            liste_recettes.append(recette)

        cur.execute("SELECT nom FROM famille WHERE ID = ?", (id_request,))
        nom = cur.fetchone()
        conn.commit()

        close_sql(cur)

        return {"listeRecettes": liste_recettes, "nom": nom[0], "id": id_request}

    except TypeError:
        response_code = 404
        HTTPResponse.status_code = response_code # type: ignore # pylint: disable=no-member
        return None


# Affichage d'une recette
@route('/recettes/<id_request>')
@view("template/recette.tpl")
def recettes(id_request):  # pylint: disable=R0914
    """
    Fonction qui permet d'afficher la page d'une recette.
    """
    try:

        conn, cur = open_sql()

        # Requête 1 (attributs de la table Recettes)
        cur.execute("SELECT * FROM Recettes WHERE ID=?", (id_request,))
        infos_recette = cur.fetchone()
        conn.commit()

        recette_id = infos_recette[0]
        recette_nom = infos_recette[1]
        recette_image = infos_recette[2]
        recette_nb_pers = infos_recette[3]
        recette_cuisson = infos_recette[4]
        recette_difficulte = infos_recette[5]
        recette_famille = infos_recette[6]

        # Requête pour récupérer le nom de la famille
        cur.execute("SELECT Nom FROM Famille WHERE ID=?", (recette_famille,))
        nom_famille = cur.fetchone()
        conn.commit()

        # Requête pour récupérer les ingrédients de la recette
        cur.execute("SELECT Ingredients.ID, Ingredients.Nom, Quantite, Unite \
                    FROM IngredientsDeRecette \
                    INNER JOIN Ingredients ON Ingredients.ID=IngredientsDeRecette.ID_ingredients \
                    WHERE ID_recettes=?", (recette_id,))
        liste_ingredients = []
        for row in cur:
            ingredient_id = row[0]
            ingredient_nom = row[1]
            ingredient_quantite = row[2]
            ingredient_unite = row[3]
            if ingredient_quantite.is_integer():
                ingredient_quantite = int(ingredient_quantite)
            ingredient = Ingredient(
                ingredient_id, ingredient_nom, ingredient_quantite, ingredient_unite)
            liste_ingredients.append(ingredient)
        conn.commit()

        # Requête pour récupérer les étapes de la recette
        cur.execute("SELECT Numero, Descriptif FROM EtapesDeRecette \
                    WHERE ID_recettes=?", (recette_id,))
        etapes_recette = []
        for row in cur:
            etape_num = row[0]
            etape_texte = row[1]
            etape = Etape(etape_num, etape_texte)
            etapes_recette.append(etape)
        conn.commit()

        close_sql(cur)

        famille_recette = Famille(recette_famille, nom_famille[0], "")
        recette = Recette(recette_id, recette_nom, recette_image, recette_cuisson,
                          recette_nb_pers, recette_difficulte, liste_ingredients,
                          etapes_recette, famille_recette)
        return {"recette": recette}

    except TypeError:
        response_code = 404
        HTTPResponse.status_code = response_code # type: ignore # pylint: disable=no-member
        return None


@route('/chercheRecettes', method='POST')
@view("template/chercheRecettes.tpl")
def rechercher():
    """
    Fonction qui permet d'afficher la page de recherche de recettes.
    """
    # Récupérer les données du formulaire
    recette_recherchee = request.forms.getunicode('recette')  # type: ignore # pylint: disable=no-member

    if recette_recherchee != "":
        mots_cles = recette_recherchee.split(" ")
        condition = "LIKE '%" + mots_cles[0] + "%'"
        for i in range(1, len(mots_cles)):
            condition += " AND nom LIKE '%" + mots_cles[i] + "%'"
    else:
        condition = "LIKE '%%'"

    _, cur = open_sql()

    # Requête SQL pour récupérer les recettes d'une famille
    cur.execute("SELECT * FROM recettes WHERE nom " + condition)
    liste_recettes = []
    for row in cur:
        recette_id = row[0]
        recette_nom = row[1]
        recette_image = row[2]
        recette_famille = row[6]
        recette = Recette(recette_id, recette_nom, recette_image,
                          None, None, None, None, None, recette_famille)
        liste_recettes.append(recette)

    close_sql(cur)
    return {"listeRecettes": liste_recettes, "recherche": recette_recherchee}


@route('/contact')
@view("static/html/contact.html")
def contact():
    """
    Fonction qui permet d'afficher la page de contact.
    """
    return {}


@route('/mentions')
@view("static/html/mentions.html")
def mentions():
    """
    Fonction qui permet d'afficher la page des mentions légales.
    """
    return {}


@error(404)
@view("static/html/404.html")
def on_error404(_):
    """
    Fonction qui permet d'afficher la page d'erreur 404.
    """
    return {}


@route('/images/<filepath:path>')
def server_static_image(filepath):
    """
    Fonction qui permet d'afficher les images.
    """
    return static_file(filepath, root='static/images/')


@route('/fonts/<filepath:path>')
def server_static_fonts(filepath):
    """
    Fonction qui permet d'afficher les fonts.
    """
    return static_file(filepath, root='static/fonts/')


@route('/css/<filepath:path>')
def server_static_css(filepath):
    """
    Fonction qui permet d'afficher les css.
    """
    return static_file(filepath, root='static/css/')


run(host='0.0.0.0', port=80)
# run(host='localhost', port=8080, debug=True)
