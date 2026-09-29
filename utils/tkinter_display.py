"""
Auteur: Nino BELAOUD, Tristan Guieu
But: Afficher le jeu avec une fenêtre tkinter
"""

import tkinter as tk
import tkinter.messagebox as tkm

from PIL import Image, ImageTk, ImageSequence


class afficher_tkinter(tk.Tk):
    def __init__(self, on_click):
        super().__init__()

        self.title("Jeu du pendu")
        self.geometry("1600x1000")

        self.Images = {
            0: './resources/Images/skeleton.gif',
            1: './resources/Images/bonhomme1.gif',
            2: './resources/Images/bonhomme2.gif',
            3: './resources/Images/bonhomme3.gif',
            4: './resources/Images/bonhomme4.gif',
            5: './resources/Images/bonhomme5.gif',
            6: './resources/Images/bonhomme6.gif',
            7: './resources/Images/bonhomme7.gif',
            8: './resources/Images/bonhomme8.gif'
        }

        self.word = tk.StringVar()
        self.Nb_Vie = tk.StringVar()
        self.MeilleurScore = tk.StringVar()
        self.Letters = tk.StringVar()

        self.MeilleurScore.set("Aucun score pour l'instant")

        # Gestion de l'animation
        self.animation_id = None
        self.skeleton_frames = []
        self.skeleton_durations = []
        self.current_frame = 0

        self.charger_skeleton()

        self.creer_widgets()

        self.on_click = on_click

    def charger_skeleton(self):
        """Charge toutes les images du GIF skeleton."""
        gif = Image.open(self.Images[0])

        for frame in ImageSequence.Iterator(gif):
            image = frame.copy().convert("RGBA")

            self.skeleton_frames.append(
                ImageTk.PhotoImage(image)
            )

            # durée de la frame en millisecondes
            self.skeleton_durations.append(
                frame.info.get("duration", 100)
            )

    def creer_widgets(self):
        self.labelMot = tk.Label(
            self,
            textvariable=self.word
        )

        self.labelLettresGuessed = tk.Label(
            self,
            textvariable=self.Letters
        )

        self.labelVie = tk.Label(
            self,
            textvariable=self.Nb_Vie
        )

        self.labelMeilleurScore = tk.Label(
            self,
            textvariable=self.MeilleurScore
        )

        self.buttonSend = tk.Button(
            self,
            text='Valider',
            command=self.bouton_clique
        )

        # IMPORTANT : garder le label dans self
        self.labelSprite = tk.Label(self)

        self.entry = tk.Entry(self)

        self.labelMot.pack()
        self.labelLettresGuessed.pack()
        self.labelVie.pack()
        self.labelMeilleurScore.pack()

        self.labelSprite.pack()

        self.entry.pack()
        self.buttonSend.pack()

    def update_labelMot(self, letter_or_word, guessed_letters):
        word = ''

        for letter in letter_or_word:
            if letter in guessed_letters:
                word += letter
            else:
                word += '_'

        self.word.set(word)

        self.Letters.set(
            str(guessed_letters)[1:-1].replace("'", "")
        )

    def update_labelVie(self, Nb_vie):
        self.Nb_Vie.set(
            "Nombre de vies : " + str(Nb_vie)
        )

        self.update_sprite(Nb_vie)

    def update_labelMeilleurScore(self, score):
        self.MeilleurScore.set(
            "Meilleur score : " + str(score)
        )

    def update_sprite(self, Nb_Vie):

        # Arrête une ancienne animation si elle existe
        if self.animation_id is not None:
            self.after_cancel(self.animation_id)
            self.animation_id = None

        # Si on affiche skeleton.gif
        if Nb_Vie == 0:
            self.current_frame = 0
            self.animer_skeleton()

        # Sinon image normale
        else:
            self.sprite = tk.PhotoImage(
                file=self.Images[Nb_Vie]
            )

            self.labelSprite.config(
                image=self.sprite
            )

    def animer_skeleton(self):
        """Anime le GIF skeleton."""

        frame = self.skeleton_frames[self.current_frame]

        self.labelSprite.config(
            image=frame
        )

        delay = self.skeleton_durations[self.current_frame]

        self.current_frame += 1

        if self.current_frame >= len(self.skeleton_frames):
            self.current_frame = 0

        self.animation_id = self.after(
            delay,
            self.animer_skeleton
        )

    def bouton_clique(self):
        self.on_click(
            self.entry.get()
        )

        self.entry.delete(
            0,
            tk.END
        )

    def create_alert(self, alert_type, message):
        if alert_type == 'error':
            tkm.showerror(
                'error',
                message
            )

        elif alert_type == 'info':
            tkm.showinfo(
                'info',
                message
            )

        else:
            tkm.showwarning(
                'warning',
                message
            )

    def ask_replay(self):
        replay = tkm.askyesno(
            'replay',
            'Voulez-vous rejouer ?'
        )

        return replay
