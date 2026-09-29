"""
Auteur: Nino BELAOUD
But: Gérer les entrées console de l'utilisateur
"""

def ask_letter_or_word():
    """
    Auteur: Nino BELAOUD
    But: Demander à l'utilisateur une lettre ou un mot et valider l'entrée
    """
    letter_or_word = input("Entrez une lettre ou un mot (si le mot est faux, alors vous perdez instantanément) : ")

    # Si c'est une lettre
    if len(letter_or_word) == 1:
        return (letter_or_word, False)

    # Si c'est un mot
    return (letter_or_word, True)

def ask_replay():
    """
    Auteur: Nino BELAOUD
    But: Demander à l'utilisateur s'il veut rejouer
    """
    replay = input("Voulez-vous rejouer ? (o/n) : ")
    return replay.lower() == 'o'
