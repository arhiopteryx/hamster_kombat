import shelve
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from threading import Thread
from tkinter import *

class PlayerWin(tk.Toplevel):
    def __init__(self, root, winnerName, winnerScore, loserName, loserScore, clicksNumber):
        super().__init__(root)
        self.root = root
        self.volume = 50
        self.load_data()
        
        self.winnerName = winnerName
        self.winnerScore = winnerScore
        self.loserName = loserName
        self.loserScore = loserScore
        self.clicksNumber = clicksNumber
        self.colorWin = "#4E57D6"
        self.colorBtn = "#13111C"

        self.init_form()
        self.title('Победа!!!')
        self.wm_state('zoomed')
        self.resizable(0, 0)
        self.attributes('-toolwindow', True)
        self.attributes('-fullscreen', True)

    def load_data(self):
        try:
            with shelve.open("shelveData") as shelveFile:
                if "volume" in shelveFile:
                    self.volume = shelveFile["volume"]
        except Exception as e:
            print(f"Error loading data: {e}")

    def init_form(self):
        self.configure(bg="#13111C")

        self.bind('<space>', self.restart_game)
        self.bind('<Escape>', self.close_form)

        l = tk.Label(self, bg=self.colorWin, text=f'Победил\n{self.winnerName}\n{self.winnerScore}/{self.clicksNumber}', font="Verdana 70 bold", fg='white')
        l.pack(expand=1, fill=tk.BOTH)
        
        loser_label = tk.Label(self, bg="#13111C", text=f'{self.loserName}\n{self.loserScore}/{self.clicksNumber}', font="Verdana 30", fg='white')
        loser_label.pack(expand=1, fill=tk.BOTH)

        self.btnCloseForm = tk.Button(
            self, 
            text='Покинуть игру', 
            command=self.destroy, 
            background="black",
            foreground="white", 
            font="Verdana 30 bold", 
            width=12, 
            borderwidth=2,
            relief='solid'
        )
        self.btnCloseForm.pack(padx=2, pady=2, side=tk.BOTTOM, fill=tk.X)
        
        self.btnRestartGame = tk.Button(
            self, 
            text='Переиграть', 
            command=self.restart_game, 
            background=self.colorBtn,
            foreground="white", 
            font="Verdana 30 bold", 
            width=12, 
            borderwidth=2,
            relief='solid'
        )
        self.btnRestartGame.pack(padx=2, pady=2, side=tk.BOTTOM, fill=tk.X)

        self.grab_set()
        self.focus_set()

    def restart_game(self, event=None):
        from intermediateGame import IntermediateGame
        IntermediateGame(self.root, 1)
        self.destroy()

    def close_form(self, event=None):
        self.destroy()
