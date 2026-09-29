"""
Auteur: Nino BELAOUD, Tristan Guieu
But: Afficher le jeu avec une fenêtre tkinter
"""

import tkinter as tk
import tkinter.messagebox as tkm

class afficher_tkinter(tk.Tk):
    def __init__(self, on_click):
        super().__init__()

        self.title("Jeu du pendu")
        self.geometry("400x250")

        self.Images = {0 : '',
                       1 : './resources/Images/bonhomme1.gif',
                       2 : './resources/Images/bonhomme2.gif',
                       3 : './resources/Images/bonhomme3.gif',
                       4 : './resources/Images/bonhomme4.gif',
                       5 : './resources/Images/bonhomme5.gif',
                       6 : './resources/Images/bonhomme6.gif',
                       7 : './resources/Images/bonhomme7.gif',
                       8 : './resources/Images/bonhomme8.gif'}

        self.word=tk.StringVar()
        self.Nb_Vie = tk.StringVar()
        self.MeilleurScore = tk.StringVar()
        self.Letters = tk.StringVar()

        self.MeilleurScore.set("Aucun score pour l'instant")

        self.creer_widgets()

        self.on_click = on_click

    def creer_widgets(self):
        self.labelMot = tk.Label(self, textvariable=self.word)
        self.labelLettresGuessed = tk.Label(self, textvariable=self.Letters)
        self.labelVie = tk.Label(self, textvariable=self.Nb_Vie)
        self.labelMeilleurScore = tk.Label(self, textvariable=self.MeilleurScore)

        self.buttonSend = tk.Button(self, text='Valider', command=self.bouton_clique)

        self.sprite = tk.PhotoImage(file='')

        self.entry = tk.Entry(textvariable='')

        self.labelMot.pack()
        self.labelLettresGuessed.pack()
        self.labelVie.pack()
        self.labelMeilleurScore.pack()
        tk.Label(self, image=self.sprite).pack()
        self.entry.pack()
        self.buttonSend.pack()

    def update_labelMot(self, letter_or_word, guessed_letters):
        word = ''
        for letter in letter_or_word:
                if letter in guessed_letters:
                    word += letter
                else :
                    word += '_'

        self.word.set(word)
        self.Letters.set(str(guessed_letters)[1: -1].replace("'", ""))

    def update_labelVie(self, Nb_vie):
        self.Nb_Vie.set("Nombre de vies : " + str(Nb_vie))

        self.update_sprite(Nb_vie)

    def update_labelMeilleurScore(self, score):
        self.MeilleurScore.set("Meilleur score : " + str(score))

    def update_sprite(self, Nb_Vie):
        self.sprite.config(file=self.Images[Nb_Vie])

    def bouton_clique(self):
        self.on_click(self.entry.get())
        self.entry.delete(0, tk.END)

    def create_alert(self, alert_type, message):
        if alert_type == 'error' :
            tkm.showerror('error', message)
        elif alert_type == 'info' :
            tkm.showinfo('info', message)
        else :
            tkm.showwarning('warning', message)