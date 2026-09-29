from utils import console_display
from utils import console_input
from utils.word_generator import WordGenerator
from utils.console_input import ask_letter_or_word

# Nombre de vies maximum
MAX_LIVES = 8

class Game:
    def __init__(self, debug: bool = False):
        self.word_generator = WordGenerator("./resources/words.csv")
        self.best_score = MAX_LIVES
        # Reset
        self.reset()
        # Mode debug
        self.debug = debug

    def reset(self):
        self.word = None
        self.word_size = None
        self.lives_left = MAX_LIVES
        self.guessed_letters = []

    def start(self):
        self.word, self.word_size = self.word_generator.choose_word()

        if self.debug:
            print(f"Word chosen: {self.word}")

        # Lancer la partie
        self.play()

    def play(self):
        if self.word is None:
            print("Error: Can't play without a word")
            return

        # Affichage du mot avec les lettres devinées
        console_display.print_word(self.word, self.guessed_letters)

        # Demande à l'utilisateur une lettre
        letter_or_word, is_word = console_input.ask_letter_or_word()

        # Si on a une lettre
        if not is_word:
            # Si la lettre a déjà été devinée, on la refuse
            if letter_or_word in self.guessed_letters:
                print("Vous avez déjà deviné cette lettre")
                self.play()
                return

            # On ajoute à la liste des lettres devinées
            self.guessed_letters.append(letter_or_word)

            # Si la lettre n'est pas dans le mot, on perd une vie
            if letter_or_word not in self.word:
                self.lives_left -= 1
                console_display.print_life_lost(self.lives_left)

        # Verification de victoire
        if self.has_won(letter_or_word, is_word):
            console_display.print_victory()
            self.end()
            return

        # Verification de défaite
        if self.has_lost(letter_or_word, is_word):
            console_display.print_defeat()
            self.end()
            return

        # On continue le jeu
        self.play()

    def has_lost(self, letter_or_word: str, is_word: bool) -> bool:
        """
        Auteur: Nino BELAOUD
        But: Vérifie si le joueur a perdu la partie.
        """
        # Si le joueur a deviné un mot, vérifier qu'il correspond au mot à deviner
        if is_word and letter_or_word != self.word:
            return True

        # Sinon, verifier qu'il reste des vies
        return self.lives_left == 0


    def has_won(self, letter_or_word: str, is_word: bool) -> bool:
        """
        Auteur: Nino BELAOUD
        But: Vérifie si le joueur a gagné la partie.
        """
        if self.word is None:
            return False

        # Si le joueur a deviné un mot, vérifier qu'il correspond au mot à deviner
        if is_word:
            return letter_or_word == self.word

        # Verifier que toutes les lettres du mot ont été devinées
        for letter in self.word:
            if letter not in self.guessed_letters:
                return False

        return True

    def update_best_score(self):
        """
        Auteur: Nino BELAOUD
        But: Met à jour le meilleur score si le score actuel est supérieur.
        """
        self.best_score = min(self.best_score, len(self.guessed_letters))

    def end(self):
        """
        Auteur: Nino BELAOUD
        But: Termine le jeu et affiche le meilleur score.
        """
        # Met à jour le meilleur score
        self.update_best_score()

        # Affiche le meilleur score
        console_display.print_best_score(self.best_score)

        # Demande à l'utilisateur s'il veut rejouer
        replay = console_input.ask_replay()

        if replay:
            self.reset()
            self.start()
            return
