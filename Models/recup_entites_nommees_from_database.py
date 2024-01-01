import sqlite3
# fonction pour récupérer les entités nommées normalisées à partir de la base de données
def recuperer_entites_nommees_via_bdd():
    try:
        # Connexion à la base de données SQLite
        conn = sqlite3.connect("entites.db")
        cursor = conn.cursor()
        
        # Récupération des entités nommées
        cursor.execute("""
            SELECT entite, label FROM entites_nommees
        """)
        entites_normalisees = cursor.fetchall()
        
        # Fermeture de la connexion à la base de données
        conn.close()
        
        return entites_normalisees
        
    except sqlite3.Error as e:
        print("Erreur lors de la requête SQL :", str(e))
        return None
# Appel de la méthode pour récupérer les entités nommées
entites_normalisees = recuperer_entites_nommees_via_bdd()

# Affichage des entités nommées normalisées récupérées depuis la base de données
if entites_normalisees:
    print("Entités nommées normalisées de puis la base de données:")
    for entite, label in entites_normalisees:
        print(f"{entite}: {label}")
        