<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Marmit@ - {{recette.nom}}</title>
    <link rel="icon" type="image/x-icon" href="/image/favicon.ico">
    <link href="/style.css" rel="stylesheet" text="text/css">
    <!-- Google fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
</head>
<body>
    <!-- Ajouter un en-tête avec un logo svg avec le texte "Marmit@" et une barre de recherche -->
    <header>
        <a href="../">
            <img src="/image/logo_text.svg" alt="Logo Marmit@">
        </a>
        <form class="search-container" action="/chercheRecettes" method="POST">
            <input name="recette" type="text" placeholder="Rechercher une recette" class="search-input">
            <button type="submit" class="search-button"> <img src="/image/loop_search.svg"></button>
        </form>
    </header>

    <nav class="fils">
        <a href="../">Accueil</a> > <a href="/famille?id={{recette.famille.Id}}">{{recette.famille.nom}}</a> > <a href="/recettes/{{recette.Id}}">{{recette.nom}}</a>
    </nav>

    <div class="main-content">
        <div class="content">
            <p><span class="bigger">Des recettes de cuisine faciles et rapides</span></p>
        </div>

        

        <div class="grid-container">
            <div class="grid-item-container-left">
                <img src="/{{recette.image}}" class="grid-item" alt="Image salade de chèvre chaud">
            </div>
            <div class="grid-item-container-right">
                <span class="grid-item-text-recette">{{recette.nom}}
                    <br>
                    <span class="info">👤{{recette.nombreDePersonnes}}&nbsp;&nbsp;•&nbsp;&nbsp;🍳{{recette.cuisson}} min&nbsp;&nbsp;•&nbsp;&nbsp;
                        %for loup in range(recette.difficulte):
                            <img src="/image/logo.svg" alt="Étoile" class="star">
                        %end
                    </span>
                    <br>
                    Ingrédients
                    <br>
                    <span class="info">
                        &nbsp;&nbsp;•&nbsp;&nbsp;
                        %for ingredient in recette.ingredients:
                            %if ingredient.unite=="":
                                {{ingredient.nom}} ({{ingredient.quantite}})&nbsp;&nbsp;•&nbsp;&nbsp;
                            %else:
                                {{ingredient.nom}} ({{ingredient.quantite}} {{ingredient.unite}})&nbsp;&nbsp;•&nbsp;&nbsp;
                            %end
                        %end
                    </span>
                </span>
            </div>
        </div>

        <div class="etape">
                <b><span class="bigger">Étapes</span></b>
                <p>
                    %if recette.etapes==[]:
                        Aucune étape n'est proposée pour cette recette.
                    %else:
                        %for etape in recette.etapes:
                            <span class="bigger">Étape {{etape.num}}</span><br>
                            {{etape.texte}}
                            <br><br>
                        %end
                    %end
            </p>
        </div>
    </div>

    <!-- Ajouter un pied de page avec un logo svg avec le texte "Marmit@" et des liens vers les mentions légales et le contact -->
    <footer>
		<a href="../">
			<img src="/image/logo.svg" alt="Logo Marmit@">
		</a>
        <div class="copyright">Marmit@ © 2023</div>
		<div class="liens">
			<a href="mentions">Mentions légales</a>
		</div>
        <div class="liens">
            <a href="contact">Contact</a>
        </div>
		<div class="liens">
            <a href="https://github.com/Hidden-Warden/Marmit65">GitHub</a>
		</div>
    </footer>
	<div class="overlay"></div>
</body>