"""
Auteur: Nino BELAOUD
But: Gérer les affichages dans la console
"""

def print_word(word: str, guessed_letters: list[str]):
    """
    Auteur: Nino BELAOUD
    But: Afficher le mot avec les lettres devinées
    Entrée:
        word (str): le mot à trouver
        guessed_letters (list[str]): les lettres déjà devinées
    """
    # Pour chaque lettre du mot, afficher la lettre si elle a été devinée sinon afficher un _
    for letter in word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()

def print_defeat():
    """
    Auteur: Nino BELAOUD
    But: Afficher le message de défaite
    """
    print("Vous avez perdu.")

def print_victory():
    """
    Auteur: Nino BELAOUD
    But: Afficher le message de victoire
    """
    print("Vous avez gagné.")

def print_life_lost(lives_left: int):
    """
    Auteur: Nino BELAOUD
    But: Afficher le message de défaite
    Entrée:
        lives_left (int): le nombre de vies restantes après la perte
    """
    print(f"Vous avez perdu une vie ({lives_left} vies restantes).")

def print_best_score(best_score: int):
    """
    Auteur: Nino BELAOUD
    But: Afficher le meilleur score
    Entrée:
        best_score (int): le meilleur score
    """
    print(f"Meilleur score : {best_score}")
