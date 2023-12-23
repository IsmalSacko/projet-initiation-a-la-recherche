import spacy
import pandas as pd
from bs4 import BeautifulSoup
import requests
import sqlite3

import requests
from bs4 import BeautifulSoup
import spacy

def traitement_document_gallica(url):
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
        
        # Affichage des entités nommées détectées
        for ent in doc.ents:
            print(f"{ent.text}: {ent.label_}")
        
        return doc  # Vous pouvez également retourner le doc ou d'autres données selon vos besoins
        
    except requests.RequestException as e:
        print("Erreur lors de la requête :", str(e))
        return None

# Appel de la méthode pour traiter le document Gallica avec l'URL spécifié
url_gallica = "https://gallica.bnf.fr/ark:/12148/bpt6k1426047z"
traitement_document_gallica(url_gallica)