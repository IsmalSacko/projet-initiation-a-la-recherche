import spacy
import sqlite3
"""
Cette première partie concerne la détection des entités nommées dans un texte en français, sans utiliser de base de données.
"""
# Charger le modèle linguistique français
nlp = spacy.load("fr_core_news_sm")
# Exemple de données historiques
donnees_historiques = [
    "La Révolution française est un événement de l'histoire de France qui a eu lieu en 1789.",
    "La republique du Mali est un pays d'Afrique de l'Ouest et la devise nationale est Un peuple, un but, une foi.",
    "Le président de la République française est Emmanuel Macron.",
    "En 1789, la Révolution française a commencé.",
    "Napoléon Bonaparte était un empereur français.",
    "L'explorateur Christophe Colomb a découvert l'Amérique en 1492."
]


# Fonction pour détecter les entités nommées dans le texte
def detecter_entites(texte):
    doc = nlp(texte)
    entites = [(entite.text, entite.label_) for entite in doc.ents]
    return entites


# Traiter les données historiques
for texte in donnees_historiques:
    entites_detectees = detecter_entites(texte)
    print(f"Texte: {texte}")
    print(f"Entités nommées détectées: {entites_detectees}")
    print("--------------------------")
# --------------------------------------------------------------------------------------------------

# Cette partie concerne la base de données SQLite et la détection des entités nommées
# Se connecter à la base de données SQLite
conn = sqlite3.connect('entite.db')
c = conn.cursor()

# Sélectionner les données depuis la table 'entites'
c.execute('SELECT texte FROM entites')
donnees_historiques = c.fetchall()


# Fonction pour détecter les entités nommées dans le texte
def detecter_entites(texte):
    doc = nlp(texte)
    entites = [(entite.text, entite.label_) for entite in doc.ents]
    return entites


# Traiter les données historiques et détecter les entités nommées
for texte_tuple in donnees_historiques:
    texte = texte_tuple[0]  # extraire le texte de la tuple
    entites_detectees = detecter_entites(texte)
    print(f"Texte: {texte}")
    print(f"Entités nommées détectées: {entites_detectees}")
    print("--------------------------")

# Fermer la connexion à la base de données
conn.close()
