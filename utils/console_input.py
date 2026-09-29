"""
Auteur: Nino BELAOUD
But: Gérer les entrées console de l'utilisateur
"""

def ask_letter():
    """
    Auteur: Nino BELAOUD
    But: Demander à l'utilisateur une lettre et valider l'entrée
    """
    letter = input("Entrez une lettre : ")

    # Si l'entrée contient plusieurs lettre alors on redemande
    if len(letter) != 1:
        print("Erreur: Veuillez entrer une seule lettre")
        return ask_letter()

    return letter

def ask_replay():
    """
    Auteur: Nino BELAOUD
    But: Demander à l'utilisateur s'il veut rejouer
    """
    replay = input("Voulez-vous rejouer ? (o/n) : ")
    return replay.lower() == 'o'
