CREATE TABLE IF NOT EXISTS "Ingredients" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"Nom"	TEXT,
	PRIMARY KEY("ID" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Famille" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"Nom"	TEXT,
	"Image"	TEXT,
	PRIMARY KEY("ID" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Recettes" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"Nom"	TEXT,
	"Image"	TEXT,
	"Nombre de personnes"	INTEGER,
	"Cuisson"	INTEGER,
	"Difficulte"	INTEGER,
	"ID_Famille"	INTEGER,
	FOREIGN KEY("ID_Famille") REFERENCES "Famille"("ID"),
	PRIMARY KEY("ID" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "IngredientsDeRecette" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"ID_recettes"	INTEGER,
	"ID_ingredients"	INTEGER,
	"Quantite"	REAL,
	"Unite"	TEXT,
	FOREIGN KEY("ID_recettes") REFERENCES "Recettes"("ID"),
	FOREIGN KEY("ID_ingredients") REFERENCES "IngredientsDeRecette"("ID"),
	PRIMARY KEY("ID" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "EtapesDeRecette" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"ID_recettes"	INTEGER,
	"Numero"	INTEGER,
	"Descriptif"	TEXT,
	FOREIGN KEY("ID_recettes") REFERENCES "Recettes"("ID"),
	PRIMARY KEY("ID" AUTOINCREMENT)
);


INSERT INTO "Famille" ("Nom", "Image") VALUES 
("Entrees", "image\famille\entrees.png"),
("Plats", "image\famille\plats.png"),
("Desserts", "image\famille\desserts.png"),
("Sauces", "image\famille\sauces.png"),
("Boissons", "image\famille\boissons.png"),
("Apéritifs", "image\famille\aperitifs.png"),
("Autres", "image\famille\autres.png");

INSERT INTO "Recettes" ("Nom", "Image", "Nombre de personnes", "Cuisson", "Difficulte", "ID_Famille") VALUES
("Salade de chèvre chaud", "image\recettes\salade_chevre.png", 4, 0, 1, 1),
("Boeuf bourguignon", "image\recettes\boeuf_bourguignon.png", 6, 180, 3, 2),
("Tarte aux pommes", "image\recettes\tarte_pommes.png", 8, 50, 2, 3),
("Sauce tomate", "image\recettes\sauce_tomate.png", 4, 30, 1, 4),
("Mojito", "image\recettes\mojito.png", 2, 0, 2, 5),
("Feuilletés au fromage", "image\recettes\feuilletes_fromage.png", 6, 20, 2, 6),
("Crème brûlée", "image\recettes\creme_brulee.png", 4, 45, 3, 7);

INSERT INTO "Ingredients" ("Nom") VALUES
/* "Salade de chèvre chaud" */
("Salade verte"),
("Tomates cerises"),
("Chèvre frais"),
("Pain de mie"),
("Miel"),
("Vinaigrette"),
/* "Boeuf bourguignon" */
("Boeuf"),
("Carottes"),
("Oignons"),
("Ail"),
("Lardons"),
("Vin rouge"),
("Bouquet garni"),
/* "Tarte aux pommes" */
("Pâte brisée"),
("Pommes"),
("Sucre"),
("Cannelle"),
("Beurre"),
/* "Sauce tomate" */
("Tomates"),
("Oignons"),
("Ail"),
("Huile d'olive"),
("Bouquet garni"),
("Vin blanc"),
("Sucre"),
("Sel"),
("Poivre"),
/* "Mojito" */
("Menthe"),
("Citron vert"),
("Sucre"),
("Eau gazeuse"),
("Rhum"),
/* "Feuilletés au fromage" */
("Pâte feuilletée"),
("Fromage"),
("Oeuf"),
("Lait"),
/* "Crème brûlée" */
("Crème fraîche"),
("Lait"),
("Oeuf"),
("Sucre"),
("Vanille");

INSERT INTO "IngredientsDeRecette" ("ID_recettes", "ID_ingredients", "Quantite", "Unite") VALUES
/* "Salade de chèvre chaud" */
(1, 1, 1, "salade"),
(1, 2, 150, "g"),
(1, 3, 150, "g"),
(1, 4, 4, "tranches"),
(1, 5, 1, "cuillière à soupe"),
(1, 6, 1, "portion"),
/* "Boeuf bourguignon" */
(2, 7, 800, "g"),
(2, 8, 4, ""),
(2, 9, 2, ""),
(2, 10, 2, "gousses"),
(2, 11, 150, "g"),
(2, 12, 750, "ml"),
(2, 13, 1, ""),
/* "Tarte aux pommes" */
(3, 14, 1, "pâte"),
(3, 15, 6, ""),
(3, 16, 100, "g"),
(3, 17, 1, "cuillère à café"),
(3, 18, 25, "g"),
/* "Sauce tomate" */
(4, 19, 800, "g"),
(4, 20, 1, ""),
(4, 21, 2, "gousses"),
(4, 22, 1, "cuillère à soupe"),
(4, 23, 1, ""),
(4, 24, 25, "cl"),
(4, 25, 1, "cuillère à café"),
(4, 26, 1, "cuillère à café"),
(4, 27, 1, "cuillère à café"),
/* "Mojito" */
(5, 28, 10, "feuilles"),
(5, 29, 1, ""),
(5, 30, 1, "cuillère à café"),
(5, 31, 1, "verre"),
(5, 32, 4, "cl"),
/* "Feuilletés au fromage" */
(6, 33, 1, "pâte"),
(6, 34, 200, "g"),
(6, 35, 1, ""),
(6, 36, 25, "cl"),
/* "Crème brûlée" */
(7, 37, 25, "cl"),
(7, 38, 25, "cl"),
(7, 39, 3, ""),
(7, 40, 100, "g"),
(7, 41, 1, "gousse");

INSERT INTO "EtapesDeRecette" ("ID_recettes", "Numero", "Descriptif") VALUES
/* "Salade de chèvre chaud" */
(1, 1, "Laver et couper les légumes"),
(1, 2, "Faire griller les tranches de pain de mie"),
(1, 3, "Disposer la salade, les tomates et le chèvre sur les tranches de pain"),
(1, 4, "Arroser de miel et de vinaigrette"),
(1, 5, "Passer sous le grill pendant 2-3 minutes"),
/* "Boeuf bourguignon" */
(2, 1, "Couper le boeuf en cubes"),
(2, 2, "Éplucher et couper les carottes et les oignons"),
(2, 3, "Faire revenir les lardons dans une cocotte"),
(2, 4, "Ajouter les légumes et l'ail dans la cocotte et faire dorer"),
(2, 5, "Ajouter le boeuf dans la cocotte et faire dorer"),
(2, 6, "Verser le vin rouge et ajouter le bouquet garni"),
(2, 7, "Laisser mijoter à feu doux pendant 2h30"),
/* "Tarte aux pommes" */
(3, 1, "Éplucher et couper les pommes en quartiers"),
(3, 2, "Étaler la pâte dans un moule à tarte"),
(3, 3, "Disposer les pommes sur la pâte"),
(3, 4, "Saupoudrer de sucre et de cannelle"),
(3, 5, "Faire cuire à 180°C pendant 30 minutes"),
/* "Sauce tomate" */
(4, 1, "Éplucher et couper les oignons et l'ail"),
(4, 2, "Faire revenir les oignons et l'ail dans une cocotte"),
(4, 3, "Ajouter les tomates et le bouquet garni"),
(4, 4, "Laisser mijoter à feu doux pendant 1h"),
(4, 5, "Ajouter le vin blanc, le sucre, le sel et le poivre"),
(4, 6, "Laisser mijoter à feu doux pendant 1h"),
(4, 7, "Passer au mixeur"),
(4, 8, "Laisser mijoter à feu doux pendant 1h"),
(4, 9, "Passer au mixeur"),
/* "Mojito" */
(5, 1, "Mettre les feuilles de menthe dans un verre"),
(5, 2, "Presser le citron vert dans le verre"),
(5, 3, "Ajouter le sucre"),
(5, 4, "Ajouter le rhum"),
(5, 5, "Remplir le verre d'eau gazeuse"),
(5, 6, "Mélanger le tout"),
/* "Feuilletés au fromage" */
(6, 1, "Étaler la pâte feuilletée dans un moule à tarte"),
(6, 2, "Couper le fromage en fines tranches"),
(6, 3, "Disposer les tranches de fromage sur la pâte"),
(6, 4, "Badigeonner le tout d'oeuf battu"),
(6, 5, "Faire cuire à 180°C pendant 20 minutes"),
/* "Crème brûlée" */
(7, 1, "Faire bouillir le lait"),
(7, 2, "Mélanger les jaunes d'oeufs et le sucre"),
(7, 3, "Ajouter la vanille"),
(7, 4, "Verser le lait bouillant sur le mélange"),
(7, 5, "Remettre le tout dans la casserole et faire cuire à feu doux en remuant sans arrêt"),
(7, 6, "Verser la crème dans des ramequins"),
(7, 7, "Laisser refroidir"),
(7, 8, "Passer au four à 180°C pendant 10 minutes"),
(7, 9, "Saupoudrer de sucre et passer sous le grill pendant 2 minutes");
