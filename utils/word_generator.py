"""
Auteur: Nino BELAOUD, Tristan Guieu
But: Générer des mots aléatoires à partir d'un fichier de mots
"""

from random import randint
import csv

class WordGenerator:
    def __init__(self, words_file: str):
        self.words_file = words_file
        self.words = []
        self.load_file()

    def load_file(self):
        """
        But: charger le fichier csv contenant les mots du jeu.
        """
        with open(self.words_file, 'r') as csv_file: #ouvre le fichier csv
            csv_reader = csv.reader(csv_file) #transforme le fichier en variable tableau
            next(csv_reader) #on skip la première ligne
            for row in csv_reader: #on ajoute tous les mots
                self.words.append(row[0])
        csv_file.close()

    def choose_word(self):
        """
        But: retourner un mot aléatoire de la bibliothèque de mots
        Sortie : (str, le mot choisi aléatoirement), (int, la taille du mot)
        """
        index = randint(0, len(self.words) - 1) 
        return self.words[index], len(self.words[index])