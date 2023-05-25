<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="apple-mobile-web-app-capable" content="yes">
	<meta name="apple-mobile-web-app-status-bar-style" content="black">
	<meta name="theme-color" content="black">
    <title>Marmit@ - {{recette.nom}}</title>
	<link rel="icon" type="image/x-icon" href="/image/favicon.ico">
    <link href="/style.css" rel="stylesheet" text="text/css">
	<link rel="apple-touch-icon" href="/image/icon/touch-icon-iphone.png">
	<link rel="apple-touch-icon" sizes="152x152" href="/image/icon/touch-icon-ipad.png">
	<link rel="apple-touch-icon" sizes="180x180" href="/image/icon/touch-icon-iphone-retina.png">
	<link rel="apple-touch-icon" sizes="167x167" href="/image/icon/touch-icon-ipad-retina.png">
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
                <div class="grid-item-text-recette">{{recette.nom}}
                    <br>
                    <span class="info">👤{{recette.nombre_de_personnes}}&nbsp;&nbsp;•&nbsp;&nbsp;🍳{{recette.cuisson}} min&nbsp;&nbsp;•&nbsp;&nbsp;
                        %for loup in range(recette.difficulte):
                            <img src="/image/logo.svg" alt="Étoile" class="star">
                        %end
                    </span>
                    <div class="ingredient">
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
    </div>

    <!-- Ajouter un pied de page avec un logo svg avec le texte "Marmit@" et des liens vers les mentions légales et le contact -->
    <footer>
		<a href="../">
			<img src="/image/logo.svg" alt="Logo Marmit@">
		</a>
        <div class="copyright">Marmit@ © 2023</div>
		<div class="liens">
			<a href="/mentions">Mentions légales</a>
		</div>
        <div class="liens">
            <a href="/contact">Contact</a>
        </div>
		<div class="liens">
            <a href="https://github.com/Hidden-Warden/Marmit65">GitHub</a>
		</div>
    </footer>
	<div class="overlay"></div>
    <div class="share-button">
        <div class="share-button_back">
          <a class="share_link" href="https://twitter.com/intent/tweet?text=Superbe+recette+sur+Marmit@+:+{{recette.nom}}&url=https://marmit65.live/recettes/{{recette.Id}}&hashtags=marmit65" title="twitter" target="_blank">
          <svg class="share_icon share_icon--twitter" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="49.652px" height="49.652px" viewBox="0 0 49.652 49.652" style="enable-background:new 0 0 49.652 49.652;" xml:space="preserve">
      <g>
          <g>
              <path d="M24.826,0C11.137,0,0,11.137,0,24.826c0,13.688,11.137,24.826,24.826,24.826c13.688,0,24.826-11.138,24.826-24.826    C49.652,11.137,38.516,0,24.826,0z M35.901,19.144c0.011,0.246,0.017,0.494,0.017,0.742c0,7.551-5.746,16.255-16.259,16.255    c-3.227,0-6.231-0.943-8.759-2.565c0.447,0.053,0.902,0.08,1.363,0.08c2.678,0,5.141-0.914,7.097-2.446    c-2.5-0.046-4.611-1.698-5.338-3.969c0.348,0.066,0.707,0.103,1.074,0.103c0.521,0,1.027-0.068,1.506-0.199    c-2.614-0.524-4.583-2.833-4.583-5.603c0-0.024,0-0.049,0.001-0.072c0.77,0.427,1.651,0.685,2.587,0.714    c-1.532-1.023-2.541-2.773-2.541-4.755c0-1.048,0.281-2.03,0.773-2.874c2.817,3.458,7.029,5.732,11.777,5.972    c-0.098-0.419-0.147-0.854-0.147-1.303c0-3.155,2.558-5.714,5.713-5.714c1.644,0,3.127,0.694,4.171,1.804    c1.303-0.256,2.523-0.73,3.63-1.387c-0.43,1.335-1.333,2.454-2.516,3.162c1.157-0.138,2.261-0.444,3.282-0.899    C37.987,17.334,37.018,18.341,35.901,19.144z"></path>
          </g>
      </g>
      </svg>
      </a>
      <a class="share_link " href="https://www.facebook.com/sharer.php?u=https://marmit65.live/recettes/{{recette.Id}}" title="facebook" target="_blank">
       <svg class="share_icon share_icon--facebook" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="49.652px" height="49.652px" viewBox="0 0 49.652 49.652" style="enable-background:new 0 0 49.652 49.652;" xml:space="preserve">
      <g>
          <g>
              <path d="M24.826,0C11.137,0,0,11.137,0,24.826c0,13.688,11.137,24.826,24.826,24.826c13.688,0,24.826-11.138,24.826-24.826    C49.652,11.137,38.516,0,24.826,0z M31,25.7h-4.039c0,6.453,0,14.396,0,14.396h-5.985c0,0,0-7.866,0-14.396h-2.845v-5.088h2.845    v-3.291c0-2.357,1.12-6.04,6.04-6.04l4.435,0.017v4.939c0,0-2.695,0-3.219,0c-0.524,0-1.269,0.262-1.269,1.386v2.99h4.56L31,25.7z    "></path>
          </g>
      </g>
      </svg>
      </a>
      <a class="share_link" href="http://www.reddit.com/submit?url=https://marmit65.live/recettes/{{recette.Id}}&title=Superbe+recette+sur+Marmit@+:+{{recette.nom}}" title="reddit" target="_blank">
      <svg class="share_icon share_icon--reddit" version="1.1"xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="49.652px" height="49.652px" viewBox="0 0 49.652 49.652" style="enable-background:new 0 0 49.652 49.652;" xml:space="preserve">
      <g>
          <g>
              <g>
                  <path d="M21.5,28.94c-0.161-0.107-0.326-0.223-0.499-0.34c-0.503-0.154-1.037-0.234-1.584-0.241h-0.066     c-2.514,0-4.718,1.521-4.718,3.257c0,1.89,1.889,3.367,4.299,3.367c3.179,0,4.79-1.098,4.79-3.258     c0-0.204-0.024-0.416-0.075-0.629C23.432,30.258,22.663,29.735,21.5,28.94z"></path>
                  <path d="M19.719,22.352c0.002,0,0.002,0,0.002,0c0.601,0,1.108-0.237,1.501-0.687c0.616-0.702,0.889-1.854,0.727-3.077     c-0.285-2.186-1.848-4.006-3.479-4.053l-0.065-0.002c-0.577,0-1.092,0.238-1.483,0.686c-0.607,0.693-0.864,1.791-0.705,3.012     c0.286,2.184,1.882,4.071,3.479,4.121H19.719L19.719,22.352z"></path>
                  <path d="M24.826,0C11.137,0,0,11.137,0,24.826c0,13.688,11.137,24.826,24.826,24.826c13.688,0,24.826-11.138,24.826-24.826     C49.652,11.137,38.516,0,24.826,0z M21.964,36.915c-0.938,0.271-1.953,0.408-3.018,0.408c-1.186,0-2.326-0.136-3.389-0.405     c-2.057-0.519-3.577-1.503-4.287-2.771c-0.306-0.548-0.461-1.132-0.461-1.737c0-0.623,0.149-1.255,0.443-1.881     c1.127-2.402,4.098-4.018,7.389-4.018c0.033,0,0.064,0,0.094,0c-0.267-0.471-0.396-0.959-0.396-1.472     c0-0.255,0.034-0.515,0.102-0.78c-3.452-0.078-6.035-2.606-6.035-5.939c0-2.353,1.881-4.646,4.571-5.572     c0.805-0.278,1.626-0.42,2.433-0.42h7.382c0.251,0,0.474,0.163,0.552,0.402c0.078,0.238-0.008,0.5-0.211,0.647l-1.651,1.195     c-0.099,0.07-0.218,0.108-0.341,0.108H24.55c0.763,0.915,1.21,2.22,1.21,3.685c0,1.617-0.818,3.146-2.307,4.311     c-1.15,0.896-1.195,1.143-1.195,1.654c0.014,0.281,0.815,1.198,1.699,1.823c2.059,1.456,2.825,2.885,2.825,5.269     C26.781,33.913,24.89,36.065,21.964,36.915z M38.635,24.253c0,0.32-0.261,0.58-0.58,0.58H33.86v4.197     c0,0.32-0.261,0.58-0.578,0.58h-1.195c-0.322,0-0.582-0.26-0.582-0.58v-4.197h-4.192c-0.32,0-0.58-0.258-0.58-0.58V23.06     c0-0.32,0.26-0.582,0.58-0.582h4.192v-4.193c0-0.321,0.26-0.58,0.582-0.58h1.195c0.317,0,0.578,0.259,0.578,0.58v4.193h4.194     c0.319,0,0.58,0.26,0.58,0.58V24.253z"></path>
              </g>
          </g>
      </g>
      </svg>
      </a>
      <a class="share_link" href="mailto:?subject=Superbe recette sur Marmit@&body=Je te partage cette magnificette trouvée sur Marmit@ du nom de {{recette.nom}} : https://marmit65.live/recettes/{{recette.Id}}" title="mail">
      <svg class="share_icon share_icon--mail" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 96 96" style="enable-background:new 0 0 96 96;" xml:space="preserve">
      <g>
          <path  d="M49.297,47.914c0.172-0.054,0.343-0.106,0.515-0.157c-0.414-0.928-0.873-1.886-1.395-2.915   c-9.4,2.776-18.399,2.812-20.008,2.784c-0.004,0.124-0.008,0.249-0.008,0.374c0,4.728,1.698,9.271,4.79,12.835   C34.223,59.173,39.68,51.025,49.297,47.914z M60.775,33.144c-3.554-3.059-8.081-4.741-12.775-4.741   c-1.419,0-2.846,0.156-4.248,0.466c1.024,1.381,4.161,5.736,7.106,11.112C57.267,37.526,60.166,33.97,60.775,33.144z    M36.118,63.567C39.567,66.206,43.672,67.6,48,67.6c2.584,0,5.096-0.496,7.469-1.475c-0.331-1.903-1.474-7.7-4.107-14.605   C40.754,55.269,36.754,62.325,36.118,63.567z M46.524,41.325c-3.039-5.36-6.203-9.775-7.071-10.962   c-5.337,2.592-9.262,7.533-10.567,13.298h0.081C30.999,43.661,38.213,43.491,46.524,41.325z M55.566,50.487   c2.324,6.457,3.396,11.832,3.703,13.548c4.257-2.998,7.172-7.602,8.045-12.712c-0.868-0.26-4.006-1.107-7.955-1.107   C58.063,50.216,56.789,50.307,55.566,50.487z M48,0C21.489,0,0,21.49,0,48c0,26.511,21.489,48,48,48s48-21.489,48-48   C96,21.49,74.511,0,48,0z M48,71.492c-12.954,0-23.492-10.538-23.492-23.492S35.046,24.508,48,24.508S71.492,35.046,71.492,48   S60.954,71.492,48,71.492z M52.611,43.378c0.433,0.893,0.839,1.783,1.209,2.651c0.121,0.283,0.24,0.568,0.356,0.852   c1.387-0.166,2.87-0.25,4.41-0.25c4.265,0,7.818,0.627,9.001,0.862c-0.11-4.251-1.612-8.381-4.253-11.694   C62.53,36.825,59.238,40.612,52.611,43.378z"></path>
      </g>
      </svg>
          </a>
        </div>
        <div class="share-button_front">
          <p class="share-button_text">Partager</p>
        </div>
      </div>
</body>