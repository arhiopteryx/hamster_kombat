import tkinter as tk
import shelve
from tkinter import ttk
from currentGame import CurrentGame
from firstPressGame import FirstPressGame
from threading import Thread

class IntermediateGame(tk.Toplevel):
    def __init__(self, root, mode):
        super().__init__(root)
        self.volume = 50
        self.load_data()
        self.frequency = 400
        self.mode = mode
        self.root = root
        self.sec = 0
        
        self.init_form()
        self.title('Скоро игра!!!')
        self.wm_state('zoomed')
        self.resizable(0, 0)
        self.attributes('-fullscreen', True)
        self.tick()

    def load_data(self):
        try:
            with shelve.open("shelveData") as shelveFile:
                if "volume" in shelveFile:            
                    self.volume = shelveFile["volume"]
        except Exception as e:
            print(f"Error loading data: {e}")

    def init_form(self):
        self.configure(bg="#13111C")

        self.time = tk.Label(self, fg='#E90000', bg="#13111C", font="Verdana 250 bold")
        self.time.pack(expand=1, fill=tk.BOTH, side=tk.BOTTOM)

        self.l = tk.Label(self, text='Игра начнётся через', font="Verdana 70 bold", fg='#10C5FF', bg="#13111C")
        self.l.pack(side=tk.TOP)

        self.grab_set()
        self.focus_set()

    def tick(self):
        self.sec += 1
        self.time['text'] = 6 - self.sec
        self.frequency += 150
        
        if self.sec < 6:
            self.time.after(1000, self.tick)
        else:
            if self.mode == 1:
                CurrentGame(self.root)
            else:
                FirstPressGame(self.root)
            self.destroy()
