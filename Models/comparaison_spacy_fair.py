import spacy
from bs4 import BeautifulSoup
import requests
import pandas as pd
from flair.data import Sentence
from flair.models import SequenceTagger
import sqlite3

def compare_entites_nommees_spacy_fair(url):
    try:
        # Récupération du contenu HTML du document
        response = requests.get(url)
        text = response.text
        
        # Suppression des balises HTML
        soup = BeautifulSoup(text, "html.parser")
        clean_text = soup.get_text()

        # Modèle de langue française avec réseaux neuronaux de SpaCy
        nlp_spacy = spacy.load("fr_core_news_sm")

        # Traitement NER avec SpaCy
        doc_spacy = nlp_spacy(clean_text)
        entities_spacy = [(ent.text, ent.label_) for ent in doc_spacy.ents if ent.label_ in ['PER', 'ORG']]

        # stocker les entités nommées extraites avec SpaCy dans une base de données SQLite
        conn = sqlite3.connect("entites_spacy.db")
        df_spacy = pd.DataFrame(entities_spacy, columns=["entite", "label"])
        df_spacy.to_sql("entites_spacy", conn, if_exists="replace", index=False)
        conn.close()

        


        # Traitement NER avec Flair
        tagger = SequenceTagger.load('ner-ontonotes')
        sentence = Sentence(clean_text)
        tagger.predict(sentence)
        entities_flair = [(entity.text, entity.get_labels()[0].value) for entity in sentence.get_spans('ner')]

        # stocker les entités nommées extraites avec Flair dans une base de données SQLite
        conn = sqlite3.connect("entites_flair.db")
        df_flair = pd.DataFrame(entities_flair, columns=["entite", "label"])
        df_flair.to_sql("entites_flair", conn, if_exists="replace", index=False)
        conn.close()

        # Stockage des entités nommées dans des DataFrames
        df_spacy = pd.DataFrame(entities_spacy, columns=['Entité', 'Type (SpaCy)'])
        df_flair = pd.DataFrame(entities_flair, columns=['Entité', 'Type (Flair)'])

        return df_spacy, df_flair

    except requests.RequestException as e:
        print("Erreur lors de la requête :", str(e))
        return None, None
    
# Appel de la méthode pour extraire les entités nommées avec SpaCy et Flair et les comparer
url_gallica = "https://gallica.bnf.fr/ark:/12148/bpt6k1426047z"
df_spacy, df_flair = compare_entites_nommees_spacy_fair(url_gallica)

# Affichage des DataFrames pour comparaison
if df_spacy is not None and df_flair is not None:
    print("Résultats de SpaCy:")
    print(df_spacy.head())  # Affiche les 5 premières entités de SpaCy
    print("\nRésultats de Flair:")
    print(df_flair.head())  # Affiche les 5 premières entités de Flair

