<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <meta name="apple-mobile-web-app-capable" content="yes">
	<meta name="apple-mobile-web-app-status-bar-style" content="black">
	<meta name="theme-color" content="black">
    <title>"{{recherche}}" - Marmit@</title>
	<link rel="icon" type="image/x-icon" href="/image/favicon.ico">
    <link href="/css/style.css" rel="stylesheet" text="text/css">
	<link rel="apple-touch-icon" href="/image/icon/touch-icon-iphone.png">
	<link rel="apple-touch-icon" sizes="152x152" href="/image/icon/touch-icon-ipad.png">
	<link rel="apple-touch-icon" sizes="180x180" href="/image/icon/touch-icon-iphone-retina.png">
	<link rel="apple-touch-icon" sizes="167x167" href="/image/icon/touch-icon-ipad-retina.png">
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
      	<a href="">Accueil</a>
    </nav>

	<div class="main-content">
		<div class="content" style="padding-bottom: 30px">
			<h3>Résultats de la recherche pour "{{recherche}}"</h3>
		</div>

        %if listeRecettes == []:
            <div class="content">
                <p>
                    <span class="bigger">Aucun résultat</span>
                </p>
            </div>
        %else:
            <div class="grid-container">
                %for recette in listeRecettes:
                    <a href="recettes/{{recette.recette_id}}">
                        <div class="grid-item-container">
                            <div class="img-overlay"></div>
                            <img src="{{recette.image}}" class="grid-item" alt="Image {{recette.nom}}">
                            <span class="grid-item-text">{{recette.nom}}</span>
                        </div>
                    </a>
                %end
            </div>
        %end
	</div>

    <!-- Ajouter un pied de page avec un logo svg avec le texte "Marmit@" et des liens vers les mentions légales et le contact -->
    <footer>
		<a href="../">
			<img src="image/logo.svg" alt="Logo Marmit@">
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