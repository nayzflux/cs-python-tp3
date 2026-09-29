"""
Auteur: Nino BELAOUD, Tristan Guieu
But: Générer des mots aléatoires à partir d'un fichier de mots
"""

class WordGenerator:
    def __init__(self, words_file: str):
        self.words_file = words_file
