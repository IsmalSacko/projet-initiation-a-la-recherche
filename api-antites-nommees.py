# Extraction des antités nommées via l'API de Gallica
import Models.recup_entites_nommees_from_database

# Normalisation des entités nommées via l'API de Gallica
import Models.normaliser_inserer_inttes_nommees

# Recupération des entités nommées normalisées via la base de données
import Models.recup_entites_nommees_from_database

# Teste les modèles de comparaison de similarité entre deux entités nommées (spacy et fair)
import Models.comparaison_spacy_fair 