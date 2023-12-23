import requests
from bs4 import BeautifulSoup
import spacy
import pandas as pd
import sqlite3

# fonction pour normaliser les entités nommées détectées dans un document Gallica
def normaliser_entites_nommees(url):
    try:
        # Récupération du contenu HTML du document
        response = requests.get(url)
        text = response.text
        
        # Suppression des balises HTML
        soup = BeautifulSoup(text, "html.parser")
        clean_text = soup.get_text()
        
        # Chargement du modèle de langue française
        nlp = spacy.load("fr_core_news_sm")
        
        # Traitement NER
        doc = nlp(clean_text)
        
        # Normalisation des entités nommées détectées
        entites_normalisees = []
        for ent in doc.ents:
            if ent.label_ == "LOC":  # Exemple : normalisation des lieux
                entite_normalisee = normaliser_lieux(ent.text)
                entites_normalisees.append((entite_normalisee, ent.label_))
            elif ent.label_ == "DATE":  # Exemple : normalisation des dates
                entite_normalisee = normaliser_dates(ent.text)
                entites_normalisees.append((entite_normalisee, ent.label_))
            elif ent.label_ == "PER":  # Exemple : normalisation des personnes
                entite_normalisee = normaliser_personnes(ent.text)
                entites_normalisees.append((entite_normalisee, ent.label_))    
            else:
                entites_normalisees.append((ent.text, ent.label_))
        
        return entites_normalisees
        
    except requests.RequestException as e:
        print("Erreur lors de la requête :", str(e))
        return None

# Fonctions de normalisation des lieux
def normaliser_lieux(entite):
    # Par exemple, convertir en majuscules, supprimer les espaces, etc.
    return entite.upper().replace("  ", " ")

# Fonctions de normalisation des dates
def normaliser_dates(entite):
   return entite
def normaliser_personnes(entite):
    # convertir en majuscules, supprimer les espaces en trop, etc.
    return entite.upper().replace("  ", " ")
    
# Appel de la méthode de normalisation des entités nommées pour l'URL spécifiée
url_gallica = "https://gallica.bnf.fr/ark:/12148/bpt6k1426047z"
entites_normalisees = normaliser_entites_nommees(url_gallica)

# Affichage des entités nommées normalisées
if entites_normalisees:
    print("Entités nommées normalisées:")
    for entite, label in entites_normalisees:
        print(f"{entite}: {label}")


# fonction pour inserer les entites nommées dans une base de données sqlite à parir la liste des entités nommées normalisées
def inserer_entites_nommees(entites_normalisees):
    try:
        # Connexion à la base de données SQLite
        conn = sqlite3.connect("entites.db")
        cursor = conn.cursor()
        
        # Création de la table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS entites_nommees (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                entite TEXT,
                label TEXT
            )
        """)
        
        # Insertion des entités nommées dans la base de données
        cursor.executemany("""
            INSERT INTO entites_nommees (entite, label) VALUES (?, ?)
        """, entites_normalisees)
        
        # Sauvegarde de la transaction
        conn.commit()
        
        # Fermeture de la connexion à la base de données
        conn.close()
        
    except sqlite3.Error as e:
        print("Erreur lors de la requête SQL :", str(e))
        return None
# Appel de la méthode pour insérer les entités nommées dans la base de données
inserer_entites_nommees(entites_normalisees)         