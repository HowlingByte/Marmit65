"""
/******************************************************************
 *                                                                *
 *   Main file of the Marmita web application.                    *
 *   This file contains all the routes for the web application.   *
 *   It is used to launch the server locally.                     *
 *                                                                *
 *   Copyright Marmit@ - HowlingByte © 2023                       *
 *   Mozilla Public License 2.0                                   *
 *                                                                *
 ******************************************************************/
"""

__author__ = "HowlingByte"
__version__ = "v.1.13"
__license__ = "MPL 2.0"

import sqlite3
from bottle import request, route, run, view, static_file, error, HTTPResponse, redirect
# from bottle import get, post, request, route, run, view, static_file, response, error, redirect

DATABASE = "database/marmita.db"


class Famille:  # pylint: disable=R0903
    """
    Class representing a family of recipes. A family has the following attributes:
    - famille_id: the family identifier in the database
    - nom: the name of the family
    - image: the image of the family
    """

    def __init__(self, famille_id: int, nom: str, image: str):
        self.famille_id: int = famille_id
        self.nom: str = nom
        self.image: str = image


class Ingredient:  # pylint: disable=R0903
    """
    Class representing an ingredient. An ingredient has the following attributes:
    - ingredient_id: the identifier of the ingredient in the database
    - nom: the name of the ingredient
    - quantite: the quantity of the ingredient
    - unite: the unit of measurement for the quantity of the ingredient
    """

    def __init__(
        self, ingredient_id: int, nom: str, quantite: int, unite: str|None = None
    ):
        self.ingredient_id: int = ingredient_id
        self.nom: str = nom
        self.quantite: int = quantite
        self.unite: str|None = unite


class Etape:  # pylint: disable=R0903
    """
    Class that presents a recipe step. A step has the following attributes:
    - num: the number of the step in the recipe
    - texte: the text of the step
    """

    def __init__(self, num: int, texte: str):
        self.num: int = num
        self.texte: str = texte


class Recette:  # pylint: disable=R0903, R0902
    """
    Class representing a recipe. A recipe has the following attributes:
    - recette_id: the recipe identifier in the database
    - nom: the name of the recipe
    - image: the image of the recipe
    - cuisson: the recipe cooking time
    - nbpers: the number of people for whom the recipe is intended
    - diff: the difficulty of the recipe
    - ingredients: the list of ingredients in the recipe
    - etapes: the list of steps in the recipe
    - famille_recette: the recipe family
    """

    def __init__(  # pylint: disable=R0913
        self,
        recette_id: int,
        nom: str,
        image: str,
        cuisson: int|None,
        nbpers: int|None,
        diff: int|None,
        ingredients: list[Ingredient]|None,
        etapes: list[Etape]|None,
        famille_recette: int|Famille,
    ):
        self.recette_id: int = recette_id
        self.nom: str = nom
        self.image: str = image
        self.cuisson: int|None = cuisson
        self.nombre_de_personnes: int|None = nbpers
        self.difficulte: int|None = diff
        self.ingredients: list[Ingredient]|None = ingredients
        self.etapes: list[Etape]|None = etapes
        self.famille: int|Famille = famille_recette


def open_sql(database: str = DATABASE):
    """
    Function used to open a connection to the database.
    :return: the connector and the database cursor
    """
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    return conn, cur


def close_sql(cur: sqlite3.Cursor):
    """
    Function used to close a connection to the database.
    :param cur: the database cursor
    """
    cur.close()


@route("/")
@view("template/accueil.tpl")
def accueil() -> dict[str, list[Famille]]:
    """
    Function used to display the home page.
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


@route("/famille", method="get")
@view("template/famille.tpl")
def famille() -> dict[str, list[Recette]|str|int] | None:
    """
    Function used to display a family page.
    """
    try:
        id_request: int = request.query.id  # type: ignore # pylint: disable=no-member

        conn, cur = open_sql()

        # SQL query to retrieve a family's recipes
        cur.execute("SELECT * FROM recettes WHERE id_famille = ?", (id_request,))
        liste_recettes = []
        for row in cur:
            recette_id = row[0]
            recette_nom = row[1]
            recette_image = row[2]
            recette_famille = row[6]
            recette = Recette(
                recette_id,
                recette_nom,
                recette_image,
                None,
                None,
                None,
                None,
                None,
                recette_famille,
            )
            liste_recettes.append(recette)

        cur.execute("SELECT nom FROM famille WHERE ID = ?", (id_request,))
        nom = cur.fetchone()
        conn.commit()

        close_sql(cur)

        return {"listeRecettes": liste_recettes, "nom": nom[0], "id": id_request}

    except TypeError:
        response_code = 404
        HTTPResponse.status_code = response_code  # type: ignore # pylint: disable=no-member
        return None


@route("/recettes/<id_request>")
@view("template/recette.tpl")
def recettes(id_request: int) -> dict[str, Recette] | None:  # pylint: disable=R0914
    """
    Function used to display a recipe page.
    """
    try:
        conn, cur = open_sql()

        # Query 1 (attributes from the Recipes table)
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

        # Query to retrieve the family name
        cur.execute("SELECT Nom FROM Famille WHERE ID=?", (recette_famille,))
        nom_famille = cur.fetchone()
        conn.commit()

        # Query to retrieve recipe ingredients
        cur.execute(
            "SELECT Ingredients.ID, Ingredients.Nom, Quantite, Unite \
                    FROM IngredientsDeRecette \
                    INNER JOIN Ingredients ON Ingredients.ID=IngredientsDeRecette.ID_ingredients \
                    WHERE ID_recettes=?",
            (recette_id,),
        )
        liste_ingredients = []
        for row in cur:
            ingredient_id = row[0]
            ingredient_nom = row[1]
            ingredient_quantite = row[2]
            ingredient_unite = row[3]
            if ingredient_quantite.is_integer():
                ingredient_quantite = int(ingredient_quantite)
            ingredient = Ingredient(
                ingredient_id, ingredient_nom, ingredient_quantite, ingredient_unite
            )
            liste_ingredients.append(ingredient)
        conn.commit()

        # Query to retrieve recipe steps
        cur.execute(
            "SELECT Numero, Descriptif FROM EtapesDeRecette \
                    WHERE ID_recettes=?",
            (recette_id,),
        )
        etapes_recette = []
        for row in cur:
            etape_num = row[0]
            etape_texte = row[1]
            etape = Etape(etape_num, etape_texte)
            etapes_recette.append(etape)
        conn.commit()

        close_sql(cur)

        famille_recette = Famille(recette_famille, nom_famille[0], "")
        recette = Recette(
            recette_id,
            recette_nom,
            recette_image,
            recette_cuisson,
            recette_nb_pers,
            recette_difficulte,
            liste_ingredients,
            etapes_recette,
            famille_recette,
        )
        return {"recette": recette}

    except TypeError:
        response_code = 404
        HTTPResponse.status_code = response_code  # type: ignore # pylint: disable=no-member
        return None


@route("/chercheRecettes", method="POST")
@view("template/chercheRecettes.tpl")
def rechercher() -> dict[str, list[Recette]|str] | None:
    """
    Function used to display the recipe search page.
    """
    # Retrieve data from the form
    recette_recherchee: str = request.forms.getunicode("recette")  # type: ignore # pylint: disable=no-member

    if recette_recherchee != "":
        mots_cles = recette_recherchee.split(" ")
        condition = "LIKE '%" + mots_cles[0] + "%'"
        for i in range(1, len(mots_cles)):
            condition += " AND nom LIKE '%" + mots_cles[i] + "%'"
    else:
        condition = "LIKE '%%'"

    if (
        recette_recherchee.lower() == "apple"
        or recette_recherchee.lower() == "🍎"
        or recette_recherchee.lower() == "pomme"
    ):
        redirect("https://apple.com")
        return None

    _, cur = open_sql()

    # SQL query to retrieve a family's recipes
    cur.execute("SELECT * FROM recettes WHERE nom " + condition)
    liste_recettes = []
    for row in cur:
        recette_id = row[0]
        recette_nom = row[1]
        recette_image = row[2]
        recette_famille = row[6]
        recette = Recette(
            recette_id,
            recette_nom,
            recette_image,
            None,
            None,
            None,
            None,
            None,
            recette_famille,
        )
        liste_recettes.append(recette)

    close_sql(cur)
    return {"listeRecettes": liste_recettes, "recherche": recette_recherchee}


@route("/contact")
@view("static/html/contact.html")
def contact() -> None:
    """
    Function used to display the contact page.
    """
    return None


@route("/mentions")
@view("static/html/mentions.html")
def mentions() -> None:
    """
    Function used to display the legal information page.
    """
    return None


@error(404)
@view("static/html/404.html")
def on_error404(_) -> None:
    """
    Function used to display the 404 error page.
    """
    return None


@route("/images/<filepath:path>")
def server_static_image(filepath: str) -> HTTPResponse:
    """
    Function used to display images.
    """
    return static_file(filepath, root="static/images/")


@route("/fonts/<filepath:path>")
def server_static_fonts(filepath: str) -> HTTPResponse:
    """
    Function used to display fonts.
    """
    return static_file(filepath, root="static/fonts/")


@route("/css/<filepath:path>")
def server_static_css(filepath: str) -> HTTPResponse:
    """
    Function used to display css files.
    """
    return static_file(filepath, root="static/css/")


run(host="0.0.0.0", port=80)
# run(host='localhost', port=8080, debug=True)
