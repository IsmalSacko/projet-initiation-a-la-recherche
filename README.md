# projet-initiation-a-la-recherche
# Author: 
 Ismaila Sacko - Tahinarisoa Daniella Rakotondratsimba - Cynthia Ramaliarisoa - Herinantenainasoa Randriamiarijaona - Verdiane Kocouvisso Plomey
# Pour cloner le projet : 
1. Ouvrir un terminal
2. Se placer dans le dossier où vous voulez cloner le projet
3. Taper la commande suivante : 
git clone https://github.com/IsmalSacko/projet-initiation-a-la-recherche.git
4. Se placer dans le dossier du projet avec la cd nom_du_dossier
5. Taper les commandes suivantes :
6. python -m venv venv # pour créer un environnement virtuel
8. Installer les dépendances avec la commande suivante :
9. pip install -r requirements.txt #pour installer les dépendances rapidement car toues les dépendances sont dans le fichier requirements.txt
ou vous les installer individuellement avec les commandes suivantes :
10. pip install spacy
11. python -m spacy download fr_core_news_sm # pour télécharger le modèle français
12. pip install sqlite3 # pour installer sqlite3......
# Test de l'application :
Tous les fichier de modèles sont dans le dossier Models.
Pour tester l'application, il faut lancer le fichier api-antites-nommees.py ou
Ou exécuter chaque fichier de modèle individuellement.
# Vous pouvez aussi tester l'application via le fichier notebooktraitement.ipynb qui est un notebook jupyter.

# Résultats :
1. Recuperation des données depuis Gallica via l'API avec requests
2. Traitement des données avec Spacy
3. Nommage des entités nommées
4.  Stockage des données dans une base de données SQLite
4. Validation des données par comparaison avec les données de recupees par Spacy et FAIR

