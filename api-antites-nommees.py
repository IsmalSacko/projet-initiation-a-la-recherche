from reportlab.pdfgen import canvas
import spacy
from bs4 import BeautifulSoup
import requests

# Remplacez l'URL par celle du document Gallica
url = "https://gallica.bnf.fr/ark:/12148/bpt6k1426047z"
response = requests.get(url)
text = response.text

# Par exemple, supprimer les balises HTML

soup = BeautifulSoup(text, "html.parser")
clean_text = soup.get_text()


# Charger le modèle de langue français
nlp = spacy.load("fr_core_news_sm")

# Traitement NER
doc = nlp(clean_text)

# Afficher les entités nommées détectées
for ent in doc.ents:
    print(f"{ent.text}: {ent.label_} ({spacy.explain(ent.label_)})")




# Créer une fonction pour créer un fichier PDF à partir d'un texte
def create_pdf(file_path, text):
    # Créer un objet canvas
    pdf_canvas = canvas.Canvas(file_path)

    # Définir la police et la taille du texte
    pdf_canvas.setFont("Helvetica", 12)

    # Écrire le texte dans le PDF
    pdf_canvas.drawString(30, 750, text)

    # Enregistrer le PDF
    pdf_canvas.save()

# Utilisez le texte nettoyé obtenu précédemment
text_to_save = clean_text

# Définissez le chemin du fichier PDF de sortie
pdf_output_path = "output.pdf"

# Créer le fichier PDF
create_pdf(pdf_output_path, text_to_save)



