from currentGame import CurrentGame
from intermediateGame import IntermediateGame
import shelve
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from threading import Thread


class Main(tk.Frame):
    def __init__(self, root):
        self.userName1 = tk.StringVar()
        self.userName2 = tk.StringVar()
        self.clicksNumber = tk.StringVar()

        self.volume = 50
        self.userName1DB = "Хомяк 1"
        self.userName2DB = "Хомяк 2"
        self.userClicksDB = "61"

        try:
            file = open("shelveData.dat")
        except IOError as e:
            shelveFile = shelve.open("shelveData", flag="n")
            shelveFile.close()
        else:
            with file:
                shelveFile = shelve.open("shelveData", flag="r")
                if "volume" in shelveFile:
                    self.volume = shelveFile["volume"]
                if "player1Name" in shelveFile:
                    self.userName1DB = shelveFile["player1Name"]
                if "player2Name" in shelveFile:
                    self.userName2DB = shelveFile["player2Name"]
                if "clicksNumber" in shelveFile:
                    self.userClicksDB = shelveFile["clicksNumber"]
                shelveFile.close()

        super().__init__(root)
        root.title("Игра в кнопки")
        root.resizable(0, 0)
        root.attributes("-fullscreen", True)
        root.wm_state("zoomed")

        self.init_main()

    def init_main(self):
        self.configure(bg="#13111C")

        self.btnCloseForm = tk.Button(
            self,
            text="Покинуть игру",
            command=root.destroy,
            background="#FF4500",  # Оранжевый цвет для выделения
            foreground="white",
            font="Verdana 20 bold",
            width=20,
            borderwidth=2,
            relief="solid",
        )
        self.btnCloseForm.pack(padx=10, pady=10, side=BOTTOM, fill=X)

        # self.labelVolume = tk.Label(
        #     root, text="Громкость", fg="white", bg="#13111C", font="Verdana 10 bold"
        # )
        # self.labelVolume.pack(side=BOTTOM, fill=X)
        # self.scal = tk.Scale(
        #     root,
        #     orient=HORIZONTAL,
        #     length=300,
        #     from_=0,
        #     to=100,
        #     tickinterval=10,
        #     resolution=5,
        #     bg="#13111C",
        #     fg="white",
        #     troughcolor="#1C1F24",
        #     highlightbackground="#13111C",
        # )
        # self.scal.pack(side=BOTTOM, fill=X)
        # self.scal.set(self.volume)
        # self.scal.bind("<B1-Motion>", self.get_val_motion)

        f1 = tk.Frame(root, bg="#13111C")
        f2 = LabelFrame(f1, bg="#13111C", fg="white", font="Verdana 20 bold")
        f3 = LabelFrame(f1, bg="#13111C", fg="white", font="Verdana 20 bold")

        self.labelPlayer1Name = tk.Label(
            f2, text="Хомяк 1", fg="white", bg="#13111C", font="Impacted 40"
        )
        self.labelPlayer1Name.pack(padx=20, pady=20)
        self.entryPlayer1Name = ttk.Entry(
            f2,
            width=23,
            textvariable=self.userName1,
            justify="center",
            font="Impacted 30 italic",
        )
        self.entryPlayer1Name.pack(padx=20, pady=20)

        self.labelPlayer2Name = tk.Label(
            f3, text="Хомяк 2", fg="white", bg="#13111C", font="Impacted 40"
        )
        self.labelPlayer2Name.pack(padx=20, pady=20)
        self.entryPlayer2Name = ttk.Entry(
            f3,
            width=23,
            textvariable=self.userName2,
            justify="center",
            font="Impacted 30 italic",
        )
        self.entryPlayer2Name.pack(padx=20, pady=20)

        self.entryPlayer1Name.insert(0, self.userName1DB)
        self.entryPlayer2Name.insert(0, self.userName2DB)

        f1.pack(side=TOP, fill=BOTH, expand=True)
        f2.pack(side=LEFT, padx=20, pady=20, fill=BOTH, expand=True)
        f3.pack(side=RIGHT, padx=20, pady=20, fill=BOTH, expand=True)

        fClicksNumber = tk.Frame(root, bg="#13111C")

        self.labelClicksNumber = tk.Label(
            fClicksNumber, text="Счет", fg="white", bg="#13111C", font="Verdana 40 bold"
        )
        self.labelClicksNumber.pack(padx=20, pady=20, side=LEFT)
        self.entryClicksNumber = ttk.Entry(
            fClicksNumber,
            width=23,
            textvariable=self.clicksNumber,
            justify="center",
            font="Impacted 30 italic",
        )
        self.entryClicksNumber.pack(padx=20, pady=20, side=LEFT)

        self.entryClicksNumber.insert(0, self.userClicksDB)

        fClicksNumber.pack(anchor=CENTER)

        fBtn = tk.Frame(root, bg="#13111C")

        self.btnStartGame = tk.Button(
            fBtn,
            text="Начать игру",
            command=self.initGameForm,
            background="#4E57D6",  # Темно-синий цвет для кнопки
            foreground="white",
            font="Verdana 40 bold",
            width=20,
            borderwidth=2,
            relief="solid",
        )
        self.btnStartGame.pack(padx=50, pady=20, side=LEFT)

        fBtn.pack(anchor=CENTER)

    def get_val_motion(self, event):
        shelveFile = shelve.open("shelveData", flag="n")
        # shelveFile["volume"] = str(self.scal.get())
        shelveFile.close()

    def initGameForm(self):
        if (
            str(self.entryPlayer1Name.get()) == ""
            or str(self.entryPlayer2Name.get()) == ""
            or str(self.entryClicksNumber.get()) == ""
        ):
            messagebox.showinfo("Ошибка", "Заполните пустые поля")
            return
        if not self.entryClicksNumber.get().isdigit():
            messagebox.showinfo("Ошибка", "Введите только цифры в поле количества нажатий")
            return
        if int(self.entryClicksNumber.get()) < 1:
            messagebox.showinfo("Ошибка", "Некоректное количество нажатий")
            return

        shelveFile = shelve.open("shelveData", flag="n")
        shelveFile["player1Name"] = str(self.entryPlayer1Name.get())
        shelveFile["player2Name"] = str(self.entryPlayer2Name.get())
        shelveFile["clicksNumber"] = str(self.entryClicksNumber.get())
        # shelveFile["volume"] = str(self.scal.get())
        shelveFile.close()

        IntermediateGame(root, 1)


if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="#13111C")
    app = Main(root)
    app.pack(fill=BOTH, expand=True)
    root.mainloop()
