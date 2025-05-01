Dans le cadre de ce projet, j'ai intégré quatre fichiers clés dans mon projet FastAPI existant pour ajouter des fonctionnalités de Web Scraping et de gestion des données dans une base de données PostgreSQL.

Voici les quatre fichiers que j'ai ajoutés à mon projet :
1. main.py
Ce fichier est le point d'entrée de ton application FastAPI. Il initialise l'application, définit les routes de l'API, et démarre le serveur.

Rôle principal : Lancer le serveur FastAPI et exposer les points d'accès (endpoints) pour interagir avec l'application.

Fonctionnement :

Le fichier importe l'application FastAPI et les dépendances nécessaires.

Expose des endpoints pour interagir avec les données scrappées et celles stockées dans la base de données PostgreSQL.

Utilise FastAPI pour gérer les requêtes HTTP (GET, POST, etc.) vers le serveur.
2. database.py
Ce fichier est responsable de la gestion de la connexion à la base de données PostgreSQL. Il configure l'interface SQLAlchemy pour se connecter et interagir avec la base de données.

Rôle principal : Configurer la connexion à la base de données PostgreSQL.

Fonctionnement :

Crée une session SQLAlchemy pour interagir avec la base de données.

Configure les informations de connexion à PostgreSQL via SQLAlchemy.

Gère l'ajout, la suppression, et la mise à jour des données dans la base de données.
3. models.py
Ce fichier définit les modèles de données utilisés pour la base de données avec SQLAlchemy. Chaque modèle correspond à une table dans la base de données.

Rôle principal : Définir la structure des données dans la base de données.

Fonctionnement :

Définit un modèle JobPost pour représenter une offre d'emploi dans la base de données.

Utilise SQLAlchemy pour décrire la table et ses colonnes.

Chaque enregistrement dans la table JobPost représente une offre d'emploi avec un titre, un lien et une date.
4. scraper.py
Ce fichier est responsable du web scraping pour extraire les données de la page "Ask HN: Who is hiring?" sur Hacker News. Il récupère les titres des offres d'emploi et leurs liens.

Rôle principal : Scraper les données de la page Hacker News.

Fonctionnement :

Utilise requests pour envoyer une requête HTTP et obtenir la page HTML.

Utilise BeautifulSoup pour analyser le HTML et extraire les informations pertinentes : titre de l'offre d'emploi, lien vers l'offre, et la date.

Les données sont ensuite enregistrées dans la base de données PostgreSQL via SQLAlchemy.
