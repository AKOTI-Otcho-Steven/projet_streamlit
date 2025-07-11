PROJET STREAMLIT
-----------------------
Présentation du projet
-----------------------

Notre projet consiste à analyser une base de données de films et d'émissions de télévision.
Nous avons téléchargé notre base sur Kaggle. C'est le dataset Amazon Prime Movies and TV Shows. 
C'est le fichier amazon_prime_titles.csv qui a 12 colonnes.
Nous avons donc parcouru tout le fichier et nous avons compris le contexte qu'il représente.
C'est un ensemble de films et d'émissions télé avec leur titre, leur directeur, leurs participants et personnages, 
leur pays de production, leur date d'ajout sur Amazon Prime, leur année de sortie, leur note, leur durée, leur catégorie et leur description.
Ce sont les différentes colonnes du dataset.

------------------------------------------
Instructions d'installation et d'exécution
------------------------------------------

Nous avons créé un dépôt GitHub que nous avons cloné sur une machine localement. 
Nous avons donc apporté les différentes modifications mon camarade et moi. Pour cela nous avons créé des branches pour travailler séparément.
Ensuite nous avons tout fusionné sur le main du dépôt pour avoir la version finale.
L'application s'ouvre dans le navigateur web par défaut à l'adresse locale indiquée (généralement http://localhost:8501) On peut alors interagir avec l'application à partir de là.
Nous avons utilisé Python, et installé les dépendances nécessaires dans le fichier requirements.txt. Nous avons aussi créé un environnement pour notre applcation. 
On a aussi un fichier principal qui est exécuté pour lancer l'applcation.

-------------------------------
Description des fonctionnalités
-------------------------------

Sur notre application, on peut charger un fichier CSV et le parcourir pour voir son contenu. 
On a aussi une barre à gauche pour les filtres selon le pays et la catégorie.
En appliquant les filtres on a le nombre de lignes sélectionnées qui est montré. 
Ensuite on a quatre indicateurs clés de performance (KPI) différents, chacun représenté par une visualisation distincte.
Les visualisations sont interactives et changent selon les filtres appliqués.
Enfin on a un aperçu du DataFrame filtré, celui obtenu après application des filtres. 

----------------------------------------------------
Répartition des tâches entre les membres de l'équipe
----------------------------------------------------

Moi, Steven, j'ai été chargé d'écrire le code pour téléverser le fichier CSV, stocker et interroger ces données avec DuckDB.
Ensuite pour les indicateurs clés, j'ai écrit le code pour le KPI 3 : Top 10 pays et le KPI 4 : Répartition par note. 
J'ai aussi configuré l'affichage en grille et l'aperçu des données filtrées.

Mon collaborateur, Kretus, a écrit le code pour les filtres, et pour les KPI 1 : Movies / TV Shows par année et KPI 2 : Répartition Movie / TV Show.



Voici comment nous avons organisé tout notre travail.







