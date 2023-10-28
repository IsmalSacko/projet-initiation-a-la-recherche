import sqlite3

# Connexion à la base de données SQLite (crée le fichier s'il n'existe pas)
conn = sqlite3.connect('entite.db')

# Création de la table "entites"
cursor = conn.cursor()
# Supprimer la table si elle existe déjà
cursor.execute('DROP TABLE IF EXISTS entites')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS entites (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL    
    )
''')

# Insérer des données dans la table
donnees_a_inserer = [
    "La Révolution française est un événement de l'histoire de France qui a eu lieu en 1789.",
    "La republique du Mali est un pays d'Afrique de l'Ouest et la devise nationale est Un peuple, un but, une foi.",
    "Le président de la République française est Emmanuel Macron.",
    "En 1789, la Révolution française a commencé.",
    "Napoléon Bonaparte était un empereur français.",
    "L'explorateur Christophe Colomb a découvert l'Amérique en 1492.",
    "L'universite Lyon 2 est une universite francaise situee a Lyon, creee en 1973.",
    "Les frères Lumière sont des industriels français, pionniers du cinéma en France depuis 1895.",


]
for texte in donnees_a_inserer:
    cursor.execute("INSERT INTO entites (nom) VALUES (?)", (texte,))


# Valider les changements
conn.commit()

# Rechercher des entités non nommées
cursor.execute("SELECT * FROM entites")
entites_sans_nom = cursor.fetchall()

# Afficher les entités sans nom
for entite in entites_sans_nom:
    print(entite)

# Fermer la connexion à la base de données
conn.close()
