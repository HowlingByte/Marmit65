<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <meta name="apple-mobile-web-app-capable" content="yes">
	<meta name="apple-mobile-web-app-status-bar-style" content="black">
	<meta name="theme-color" content="black">
    <title>{{recette.nom}} - Marmit@</title>
	<link rel="icon" type="images/x-icon" href="/images/favicon.ico">
    <link href="/css/style.css" rel="stylesheet" text="text/css">
	<link rel="apple-touch-icon" href="/images/icon/touch-icon-iphone.png">
	<link rel="apple-touch-icon" sizes="152x152" href="/images/icon/touch-icon-ipad.png">
	<link rel="apple-touch-icon" sizes="180x180" href="/images/icon/touch-icon-iphone-retina.png">
	<link rel="apple-touch-icon" sizes="167x167" href="/images/icon/touch-icon-ipad-retina.png">
</head>

<body>
    <!-- Ajouter un en-tête avec un logo svg avec le texte "Marmit@" et une barre de recherche -->
    <header>
        <a href="../">
            <img src="/images/logo_text.svg" alt="Logo Marmit@">
        </a>
        <form class="search-container" action="/chercheRecettes" method="POST">
            <input name="recette" type="text" placeholder="Rechercher une recette" class="search-input">
            <button type="submit" class="search-button"> <img src="/images/loop_search.svg"></button>
        </form>
    </header>

    <nav>
        <a href="../">Accueil</a> > <a href="/famille?id={{recette.famille.famille_id}}">{{recette.famille.nom}}</a> > <a href="/recettes/{{recette.recette_id}}">{{recette.nom}}</a>
    </nav>

    <main>
        <div class="grid-container">
            <div class="grid-item-container-left">
                <img src="/{{recette.image}}" class="grid-item" alt="Image salade de chèvre chaud">
            </div>
            <div class="grid-item-container-right">
                <div class="grid-item-text-recette">{{recette.nom}}
                    <br>
                    <span class="info">👤{{recette.nombre_de_personnes}}&nbsp;&nbsp;•&nbsp;&nbsp;🍳{{recette.cuisson}} min&nbsp;&nbsp;•&nbsp;&nbsp;
                        %for loup in range(recette.difficulte):
                            <img src="/images/logo.svg" alt="Étoile" class="star">
                        %end
                    </span>
                    <div class="ingredient">
                        Ingrédients
                        <br>
                        <span class="info">
                            &nbsp;•
                            %for ingredient in recette.ingredients:
                                %if ingredient.unite=="":
                                    {{ingredient.nom}} ({{ingredient.quantite}}) • 
                                %else:
                                    {{ingredient.nom}} ({{ingredient.quantite}} {{ingredient.unite}}) • 
                                %end
                            %end
                        </span>
                    </div>
                </div>
            </div>
        </div>

        <div class="etape">
            <b><span class="bigger-plus">Étapes</span></b>
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
    </main>

    <!-- Ajouter un pied de page avec un logo svg avec le texte "Marmit@" et des liens vers les mentions légales et le contact -->
    <footer>
        <div>
            <a href="https://github.com/HowlingByte"><img src="/images/howlingbyte.svg" alt="Logo HowlingByte" class="howlingbyte"></a>
            <a href="../"><img src="/images/logo.svg" alt="Logo Marmit@" class="logo"></a>
        </div>
        <div class="copyright">Marmit@ – HowlingByte © 2023</div>
        <div class="liens">
            <a href="/mentions">Mentions légales</a>
        </div>
        <div class="liens">
            <a href="/contact">Contact</a>
        </div>
        <div class="liens">
            <a href="https://github.com/HowlingByte/Marmit65">GitHub</a>
        </div>
    </footer>

    <div class="share-button">
        <div class="share-button_back">
            <a class="share_link" href="https://twitter.com/intent/tweet?text=Superbe+recette+sur+Marmit@+:+{{recette.nom}}&url=https://marmit65.live/recettes/{{recette.recette_id}}&hashtags=marmit65" title="Twitter" target="_blank">
                <img class="share_icon share_icon--twitter" src="/images/icon/twitter.svg" alt="Logo Twitter" />
            </a>
            <a class="share_link " href="https://www.facebook.com/sharer.php?u=https://marmit65.live/recettes/{{recette.recette_id}}" title="Facebook" target="_blank">
                <img class="share_icon share_icon--facebook" src="/images/icon/facebook.svg" alt="Logo Facebook" />
            </a>
            <a class="share_link" href="http://www.reddit.com/submit?url=https://marmit65.live/recettes/{{recette.recette_id}}&title=Superbe+recette+sur+Marmit@+:+{{recette.nom}}" title="Reddit" target="_blank">
                <img class="share_icon share_icon--reddit" src="/images/icon/reddit.svg" alt="Logo Reddit" />
            </a>
            <a class="share_link" href="mailto:?subject=Superbe recette sur Marmit@&body=Je te partage cette magnificette trouvée sur Marmit@ du nom de {{recette.nom}} : https://marmit65.live/recettes/{{recette.recette_id}}" title="Mail" target="_blank">
                <img class="share_icon share_icon--mail" src="/images/icon/mail.svg" alt="Logo Mail" />
            </a>
        </div>
        <div class="share-button_front">
            <p class="share-button_text">Partager</p>
        </div>
    </div>
    
	<div class="overlay"></div>
</body>
