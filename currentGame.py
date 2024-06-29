import shelve
import tkinter as tk
from tkinter import ttk
import os
import random
from PIL import Image, ImageTk
from playerWin import PlayerWin  # Assuming PlayerWin is defined in playerWin.py

class CurrentGame(tk.Toplevel):
    def __init__(self, root):
        self.volume = 50
        shelveFile = shelve.open("shelveData", flag="r")
        self.player1Name = shelveFile["player1Name"]
        self.player2Name = shelveFile["player2Name"]
        self.clicksNumber = int(shelveFile["clicksNumber"])
        if "volume" in shelveFile:
            self.volume = shelveFile["volume"]
        shelveFile.close()

        self.root = root

        self.countPressButton1 = 0
        self.countPressButton2 = 0

        super().__init__(root)
        self.initForm()
        self.title("Нажми на кнопку")
        self.wm_state("zoomed")
        self.resizable(0, 0)
        self.attributes("-fullscreen", True)

    def initForm(self):
        self.btnCloseForm = tk.Button(
            self,
            text="Покинуть игру",
            command=self.destroy,
            background="#13111C",
            foreground="white",
            font="Verdana 10 bold",
            width=12,
            relief="solid",
        )
        self.btnCloseForm.pack(padx=10, pady=5, side=tk.BOTTOM, fill=tk.X)

        content_frame = tk.Frame(self)
        content_frame.pack(fill=tk.BOTH, expand=1)

        f1 = tk.Frame(content_frame, bg="#13111C")
        f1.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        l1 = tk.Label(f1, width=100, height=1, bg="#13111C")
        l1.pack(fill=tk.X)

        self.labelClicksNumberUser1 = tk.Label(
            f1,
            text=self.player1Name,
            fg="white",
            bg="#13111C",
            font="Verdana 40 bold",
            padx=0,
            pady=0,
        )
        self.labelClicksNumberUser1.pack()

        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure(
            "Custom.Horizontal.TProgressbar",
            troughcolor="#E0E0E0",  # Цвет фона прогрессбара
            background="#4E57D6",
        )  # Цвет заполненной части прогрессбара
        self.progress1 = ttk.Progressbar(
            f1,
            orient="horizontal",
            length=400,
            mode="determinate",
            maximum=self.clicksNumber,
            style="Custom.Horizontal.TProgressbar",
        )

        self.progress1.pack(fill=tk.X, pady=(5, 0), ipady=5)

        # Load the hamster_coin.png image
        self.hamster_coin_image = Image.open(os.path.join("Images", "hamster_coin.png"))
        self.hamster_coin_photo = ImageTk.PhotoImage(self.hamster_coin_image)

        # Create a frame to contain the image and the label for player 1
        progress1_frame = tk.Frame(f1, bg="#13111C")
        progress1_frame.pack(pady=(5, 0))

        self.hamster_coin_label1 = tk.Label(progress1_frame, image=self.hamster_coin_photo, bg="#13111C")
        self.hamster_coin_label1.pack(side=tk.LEFT, padx=(0, 10))

        self.progress1_label = tk.Label(
            progress1_frame,
            text=f"0/{self.clicksNumber}",
            fg="white",
            bg="#13111C",
            font="Verdana 20 bold",
        )
        self.progress1_label.pack(side=tk.LEFT)

        black_frame1 = tk.Frame(f1, bg="#1C1F24")
        black_frame1.pack(fill=tk.BOTH, expand=1)

        # Create a Canvas for animations and image
        self.canvas1 = tk.Canvas(black_frame1, bg="#1C1F24", highlightthickness=0)
        self.canvas1.pack(fill=tk.BOTH, expand=1)

        # Load images for player 1
        self.images1 = [
            tk.PhotoImage(file=os.path.join("Images", f"{i}.png")) for i in range(1, 11)
        ]
        self.image_id1 = self.canvas1.create_image(0, 0, image=self.images1[0], anchor=tk.CENTER)
        self.canvas1.bind("<Configure>", lambda event: self.center_image(self.canvas1, self.image_id1))

        # Разделительная линия
        divider = tk.Canvas(
            content_frame, width=2, bg="black", bd=0, highlightthickness=0
        )
        divider.pack(side=tk.LEFT, fill=tk.Y)

        f2 = tk.Frame(content_frame, bg="#13111C")
        f2.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        l2 = tk.Label(f2, width=100, height=1, bg="#13111C")
        l2.pack(fill=tk.X)

        self.labelClicksNumberUser2 = tk.Label(
            f2,
            text=self.player2Name,
            fg="white",
            bg="#13111C",
            font="Verdana 40 bold",
            padx=0,
            pady=0,
        )
        self.labelClicksNumberUser2.pack()

        self.progress2 = ttk.Progressbar(
            f2,
            orient="horizontal",
            length=400,
            mode="determinate",
            maximum=self.clicksNumber,
            style="Custom.Horizontal.TProgressbar",
        )
        self.progress2.pack(fill=tk.X, pady=(5, 0), ipady=5)

        # Create a frame to contain the image and the label for player 2
        progress2_frame = tk.Frame(f2, bg="#13111C")
        progress2_frame.pack(pady=(5, 0))

        self.hamster_coin_label2 = tk.Label(progress2_frame, image=self.hamster_coin_photo, bg="#13111C")
        self.hamster_coin_label2.pack(side=tk.LEFT, padx=(0, 10))

        self.progress2_label = tk.Label(
            progress2_frame,
            text=f"0/{self.clicksNumber}",
            fg="white",
            bg="#13111C",
            font="Verdana 20 bold",
        )
        self.progress2_label.pack(side=tk.LEFT)

        black_frame2 = tk.Frame(f2, bg="#1C1F24")
        black_frame2.pack(fill=tk.BOTH, expand=1)

        # Create a Canvas for animations and image for player 2
        self.canvas2 = tk.Canvas(black_frame2, bg="#1C1F24", highlightthickness=0)
        self.canvas2.pack(fill=tk.BOTH, expand=1)

        # Load images for player 2
        self.images2 = [
            tk.PhotoImage(file=os.path.join("Images", f"{i}.png")) for i in range(1, 11)
        ]
        self.image_id2 = self.canvas2.create_image(0, 0, image=self.images2[0], anchor=tk.CENTER)
        self.canvas2.bind("<Configure>", lambda event: self.center_image(self.canvas2, self.image_id2))

        self.bind("1", self.player1btn)
        self.bind("2", self.player2btn)
        self.bind("<Escape>", self.closeForm)

        self.grab_set()
        self.focus_set()

    def center_image(self, canvas, image_id):
        canvas_width = canvas.winfo_width() / 2
        canvas_height = canvas.winfo_height() / 2
        canvas.coords(image_id, canvas_width, canvas_height)

    def update_progress(self, progressbar, label, count, canvas, images, image_id):
        progressbar["value"] = count
        label.config(text=f"{count}/{self.clicksNumber}")
        if count < self.clicksNumber:
            percentage = (count / self.clicksNumber) * 100
            image_index = int(percentage // 10)
            canvas.itemconfig(image_id, image=images[image_index])

    def player1btn(self, event):
        self.countPressButton1 += 1
        self.update_progress(
            self.progress1,
            self.progress1_label,
            self.countPressButton1,
            self.canvas1,
            self.images1,
            self.image_id1,
        )
        self.show_plus_one_animation(self.canvas1)
        if self.countPressButton1 == self.clicksNumber:
            PlayerWin(
                self.root, 
                self.player1Name, 
                self.countPressButton1, 
                self.player2Name, 
                self.countPressButton2,
                self.clicksNumber  # Added clicksNumber here
            )
            self.destroy()

    def player2btn(self, event):
        self.countPressButton2 += 1
        self.update_progress(
            self.progress2,
            self.progress2_label,
            self.countPressButton2,
            self.canvas2,
            self.images2,
            self.image_id2,
        )
        self.show_plus_one_animation(self.canvas2)
        if self.countPressButton2 == self.clicksNumber:
            PlayerWin(
                self.root, 
                self.player2Name, 
                self.countPressButton2, 
                self.player1Name, 
                self.countPressButton1,
                self.clicksNumber  # Added clicksNumber here
            )
            self.destroy()

    def closeForm(self, event):
        self.destroy()

    def show_plus_one_animation(self, canvas):
        # Calculate random coordinates within the canvas area
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()
        rand_x = random.randint(0, canvas_width)
        rand_y = random.randint(0, canvas_height)
        
        # Create a text item on the canvas for +1 animation
        text = "+" + str(random.randint(1, 25))
        text_item = canvas.create_text(rand_x, rand_y, text=text, fill="white", font=("Arial", 40, "bold"))

        # Start the animation
        self.animate_plus_one(canvas, text_item)

    def animate_plus_one(self, canvas, text_item):
        def update_animation(alpha=1.0, y_shift=0):
            alpha -= 0.03
            y_shift -= 2
            if alpha <= 0:
                canvas.delete(text_item)
            else:
                canvas.itemconfig(text_item, fill=f"#{int(255*alpha):02x}{int(255*alpha):02x}{int(255*alpha):02x}")
                canvas.move(text_item, 0, y_shift)
                self.after(30, update_animation, alpha, y_shift)

        update_animation()




# import shelve
# import tkinter as tk
# from tkinter import ttk
# from threading import Thread
# import os
# import random
# from PIL import Image, ImageDraw, ImageTk, ImageFont
# from playerWin import PlayerWin  # Assuming PlayerWin is defined in playerWin.py


# class CurrentGame(tk.Toplevel):
#     def __init__(self, root):
#         self.volume = 50
#         shelveFile = shelve.open("shelveData", flag="r")
#         self.player1Name = shelveFile["player1Name"]
#         self.player2Name = shelveFile["player2Name"]
#         self.clicksNumber = int(shelveFile["clicksNumber"])
#         if "volume" in shelveFile:
#             self.volume = shelveFile["volume"]
#         shelveFile.close()

#         self.root = root

#         self.countPressButton1 = 0
#         self.countPressButton2 = 0

#         super().__init__(root)
#         self.initForm()
#         self.title("Нажми на кнопку")
#         self.wm_state("zoomed")
#         self.resizable(0, 0)
#         self.attributes("-fullscreen", True)

#     def initForm(self):
#         self.btnCloseForm = tk.Button(
#             self,
#             text="Покинуть игру",
#             command=self.destroy,
#             background="#13111C",
#             foreground="white",
#             font="Verdana 10 bold",
#             width=12,
#             # borderwidth=2,
#             relief="solid",
#         )
#         self.btnCloseForm.pack(padx=10, pady=5, side=tk.BOTTOM, fill=tk.X)

#         content_frame = tk.Frame(self)
#         content_frame.pack(fill=tk.BOTH, expand=1)

#         f1 = tk.Frame(content_frame, bg="#13111C")
#         f1.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

#         l1 = tk.Label(f1, width=100, height=1, bg="#13111C")
#         l1.pack(fill=tk.X)

#         self.labelClicksNumberUser1 = tk.Label(
#             f1,
#             text=self.player1Name,
#             fg="white",
#             bg="#13111C",
#             font="Verdana 40 bold",
#             padx=0,
#             pady=0,
#         )
#         self.labelClicksNumberUser1.pack()

#         self.style = ttk.Style()
#         self.style.theme_use("default")
#         self.style.configure(
#             "Custom.Horizontal.TProgressbar",
#             troughcolor="#E0E0E0",  # Цвет фона прогрессбара
#             background="#4E57D6",
#         )  # Цвет заполненной части прогрессбара
#         self.progress1 = ttk.Progressbar(
#             f1,
#             orient="horizontal",
#             length=400,
#             mode="determinate",
#             maximum=self.clicksNumber,
#             style="Custom.Horizontal.TProgressbar",
#         )

#         self.progress1.pack(fill=tk.X, pady=(5, 0), ipady=5)

#         self.progress1_label = tk.Label(
#             f1,
#             text=f"0/{self.clicksNumber}",
#             fg="white",
#             bg="#13111C",
#             font="Verdana 20 bold",
#         )
#         # self.progress1_label.pack(pady=(5, 20))

#         black_frame1 = tk.Frame(f1, bg="#1C1F24")
#         black_frame1.pack(fill=tk.BOTH, expand=1)

#         # Load images
#         self.images1 = [
#             tk.PhotoImage(file=os.path.join("Images", f"{i}.png")) for i in range(1, 11)
#         ]
#         self.hamster_label1 = tk.Label(
#             black_frame1, image=self.images1[0], bg="#1C1F24"
#         )
#         self.hamster_label1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

#         # Разделительная линия
#         divider = tk.Canvas(
#             content_frame, width=2, bg="black", bd=0, highlightthickness=0
#         )
#         divider.pack(side=tk.LEFT, fill=tk.Y)

#         f2 = tk.Frame(content_frame, bg="#13111C")
#         f2.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

#         l2 = tk.Label(f2, width=100, height=1, bg="#13111C")
#         l2.pack(fill=tk.X)

#         self.labelClicksNumberUser2 = tk.Label(
#             f2,
#             text=self.player2Name,
#             fg="white",
#             bg="#13111C",
#             font="Verdana 40 bold",
#             padx=0,
#             pady=0,
#         )
#         self.labelClicksNumberUser2.pack()

#         self.progress2 = ttk.Progressbar(
#             f2,
#             orient="horizontal",
#             length=400,
#             mode="determinate",
#             maximum=self.clicksNumber,
#             style="Custom.Horizontal.TProgressbar",
#         )
#         self.progress2.pack(fill=tk.X, pady=(5, 0), ipady=5)

#         self.progress2_label = tk.Label(
#             f2,
#             text=f"0/{self.clicksNumber}",
#             fg="white",
#             bg="#13111C",
#             font="Verdana 20 bold",
#         )
#         # self.progress2_label.pack(pady=(5, 20))

#         black_frame2 = tk.Frame(f2, bg="#1C1F24")
#         black_frame2.pack(fill=tk.BOTH, expand=1)

#         # Load images
#         self.images2 = [
#             tk.PhotoImage(file=os.path.join("Images", f"{i}.png")) for i in range(1, 11)
#         ]
#         self.hamster_label2 = tk.Label(
#             black_frame2, image=self.images2[0], bg="#1C1F24"
#         )
#         self.hamster_label2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

#         self.bind("1", self.player1btn)
#         self.bind("2", self.player2btn)
#         self.bind("<Escape>", self.closeForm)

#         self.grab_set()
#         self.focus_set()

#     def update_progress(self, progressbar, label, count, image_label, images):
#         progressbar["value"] = count
#         label.config(text=f"{count}/{self.clicksNumber}")
#         if count < self.clicksNumber:
#             percentage = (count / self.clicksNumber) * 100
#             image_index = int(percentage // 10)
#             image_label.config(image=images[image_index])

#     def player1btn(self, event):
#         self.countPressButton1 += 1
#         self.update_progress(
#             self.progress1,
#             self.progress1_label,
#             self.countPressButton1,
#             self.hamster_label1,
#             self.images1,
#         )
#         self.show_plus_one_animation(self.hamster_label1)
#         if self.countPressButton1 == self.clicksNumber:
#             PlayerWin(self.root, self.player1Name, "1")
#             self.destroy()

#     def player2btn(self, event):
#         self.countPressButton2 += 1
#         self.update_progress(
#             self.progress2,
#             self.progress2_label,
#             self.countPressButton2,
#             self.hamster_label2,
#             self.images2,
#         )
#         self.show_plus_one_animation(self.hamster_label2)
#         if self.countPressButton2 == self.clicksNumber:
#             PlayerWin(self.root, self.player2Name, "2")
#             self.destroy()

#     def closeForm(self, event):
#         self.destroy()

#     # def show_plus_one_animation2(self, image_label):
#     #     # Get the dimensions of the image label
#     #     img_width = image_label.winfo_width()
#     #     img_height = image_label.winfo_height()

#     #     # Calculate random coordinates within the image area
#     #     rand_x = random.randint(img_width/2, img_width*2 - img_width/2) - img_width
#     #     rand_y = random.randint(0, img_height)

#     #     # Create a label for +1 animation with transparent background
#     #     text = "+" + str(random.randint(1, 25))
#     #     label_plus_one = tk.Label(self, text=text, fg="white", bg="#13111C", font=("Arial", 40, "bold"))
#     #     label_plus_one.place(in_=image_label, x=rand_x, y=rand_y)

#     #     # Start the animation
#     #     self.animate_plus_one(label_plus_one)

#     def show_plus_one_animation(self, image_label):
#         # Get the dimensions of the image label
#         img_width = image_label.winfo_width()
#         img_height = image_label.winfo_height()

#         # Calculate random coordinates within the image area
#         rand_x = (
#             random.randint(img_width / 2, img_width * 2 - img_width / 2) - img_width
#         )
#         rand_y = random.randint(0, img_height)

#         # Create a label for +1 animation with a specific background color
#         text = "+" + str(random.randint(1, 25))
#         label_plus_one = tk.Label(
#             self, text=text, fg="white", bg="#13111C", font=("Arial", 40, "bold")
#         )
#         label_plus_one.place(in_=image_label, x=rand_x, y=rand_y)

#         # Set the transparent color for the window to the background color of the label
#         # self.wm_attributes('-transparentcolor', label_plus_one.cget('bg'))
#         # self.wm_attributes('-transparentcolor', label_plus_one.cget('bg'))
#         # self.attributes('-transparentcolor', '#111111')

#         # Start the animation
#         self.animate_plus_one(label_plus_one)

#     def animate_plus_one(self, label):
#         def update_animation(alpha=1.0, y=0):
#             alpha -= 0.03
#             y -= 2
#             if alpha <= 0:
#                 label.place_forget()
#             else:
#                 label.place_configure(relx=0.5, rely=0.5, anchor=tk.CENTER, y=y)
#                 label.configure(
#                     fg=f"#{int(255*alpha):02x}{int(255*alpha):02x}{int(255*alpha):02x}"
#                 )
#                 self.after(30, update_animation, alpha, y)

#         update_animation()


# import shelve
# import tkinter as tk
# from tkinter import ttk
# from threading import Thread
# import pyglet
# from pyglet.media import Player
# from tkinter import *
# from playerWin import PlayerWin
# import os

# class CurrentGame(tk.Toplevel):
#     def __init__(self, root):
#         self.music_player = Player()
#         self.volume = 50
#         shelveFile = shelve.open("shelveData", flag="r")
#         self.player1Name = shelveFile["player1Name"]
#         self.player2Name = shelveFile["player2Name"]
#         self.clicksNumber = int(shelveFile["clicksNumber"])
#         if "volume" in shelveFile:
#             self.volume = shelveFile["volume"]
#         shelveFile.close()

#         self.root = root

#         self.countPressButton1 = 0
#         self.countPressButton2 = 0

#         super().__init__(root)
#         self.initForm()
#         self.title("Нажми на кнопку")
#         self.wm_state("zoomed")
#         self.resizable(0, 0)
#         self.attributes("-fullscreen", True)

#     def initForm(self):
#         self.btnCloseForm = tk.Button(
#             self,
#             text="Покинуть игру",
#             command=self.destroy,
#             background="black",
#             foreground="white",
#             font="Verdana 10 bold",
#             width=12,
#             borderwidth=2,
#             relief="solid",
#         )
#         self.btnCloseForm.pack(padx=10, pady=5, side=BOTTOM, fill=X)

#         content_frame = tk.Frame(self)
#         content_frame.pack(fill=BOTH, expand=1)

#         f1 = tk.Frame(content_frame, bg="#E90000")
#         f1.pack(side=LEFT, fill=BOTH, expand=1)

#         l1 = Label(f1, width=100, height=1, bg="#E90000")
#         l1.pack(fill=X)

#         self.labelClicksNumberUser1 = tk.Label(
#             f1,
#             text=self.player1Name,
#             fg="white",
#             bg="#E90000",
#             font="Verdana 40 bold",
#             padx=0,
#             pady=0,
#         )
#         self.labelClicksNumberUser1.pack()

#         self.progress1 = ttk.Progressbar(
#             f1, orient="horizontal", length=400, mode="determinate", maximum=self.clicksNumber
#         )
#         self.progress1.pack(fill=X, pady=(5, 0), ipady=5)

#         self.progress1_label = tk.Label(
#             f1,
#             text=f"0/{self.clicksNumber}",
#             fg="white",
#             bg="#E90000",
#             font="Verdana 20 bold",
#         )
#         self.progress1_label.pack(pady=(5, 20))

#         black_frame1 = tk.Frame(f1, bg="black")
#         black_frame1.pack(fill=BOTH, expand=1)

#         # Load images
#         self.images1 = [tk.PhotoImage(file=os.path.join("Images", f"{i}.png")) for i in range(1, 11)]
#         self.hamster_label1 = tk.Label(black_frame1, image=self.images1[0], bg="black")
#         self.hamster_label1.place(relx=0.5, rely=0.5, anchor=CENTER)

#         # Разделительная линия
#         divider = tk.Canvas(content_frame, width=2, bg="black", bd=0, highlightthickness=0)
#         divider.pack(side=LEFT, fill=Y)

#         f2 = tk.Frame(content_frame, bg="#10C5FF")
#         f2.pack(side=LEFT, fill=BOTH, expand=1)

#         l2 = Label(f2, width=100, height=1, bg="#10C5FF")
#         l2.pack(fill=X)

#         self.labelClicksNumberUser2 = tk.Label(
#             f2,
#             text=self.player2Name,
#             fg="white",
#             bg="#10C5FF",
#             font="Verdana 40 bold",
#             padx=0,
#             pady=0,
#         )
#         self.labelClicksNumberUser2.pack()

#         self.progress2 = ttk.Progressbar(
#             f2, orient="horizontal", length=400, mode="determinate", maximum=self.clicksNumber
#         )
#         self.progress2.pack(fill=X, pady=(5, 0), ipady=5)

#         self.progress2_label = tk.Label(
#             f2,
#             text=f"0/{self.clicksNumber}",
#             fg="white",
#             bg="#10C5FF",
#             font="Verdana 20 bold",
#         )
#         self.progress2_label.pack(pady=(5, 20))

#         black_frame2 = tk.Frame(f2, bg="black")
#         black_frame2.pack(fill=BOTH, expand=1)

#         # Load images
#         self.images2 = [tk.PhotoImage(file=os.path.join("Images", f"{i}.png")) for i in range(1, 11)]
#         self.hamster_label2 = tk.Label(black_frame2, image=self.images2[0], bg="black")
#         self.hamster_label2.place(relx=0.5, rely=0.5, anchor=CENTER)

#         self.bind("1", self.player1btn)
#         self.bind("2", self.player2btn)
#         self.bind("<Escape>", self.closeForm)

#         self.grab_set()
#         self.focus_set()

#     def update_progress(self, progressbar, label, count, image_label, images):
#         progressbar["value"] = count
#         label.config(text=f"{count}/{self.clicksNumber}")
#         if count < self.clicksNumber:
#             percentage = (count / self.clicksNumber) * 100
#             image_index = int(percentage // 10)
#             image_label.config(image=images[image_index])

#     def player1btn(self, event):
#         self.countPressButton1 += 1
#         self.update_progress(
#             self.progress1, self.progress1_label, self.countPressButton1, self.hamster_label1, self.images1
#         )
#         Thread(target=self.musicPlayer1, daemon=True).start()
#         if self.countPressButton1 == self.clicksNumber:
#             PlayerWin(self.root, self.player1Name, "1")
#             self.destroy()

#     def player2btn(self, event):
#         self.countPressButton2 += 1
#         self.update_progress(
#             self.progress2, self.progress2_label, self.countPressButton2, self.hamster_label2, self.images2
#         )
#         Thread(target=self.musicPlayer2, daemon=True).start()
#         if self.countPressButton2 == self.clicksNumber:
#             PlayerWin(self.root, self.player2Name, "2")
#             self.destroy()

#     def musicPlayer1(self):
#         song = pyglet.media.synthesis.Sawtooth(duration=0.08, frequency=350)
#         self.music_player = Player()
#         self.music_player.queue(song)
#         self.music_player.volume = float(self.volume) / 100.0
#         self.music_player.play()

#     def musicPlayer2(self):
#         song = pyglet.media.synthesis.Sawtooth(duration=0.08, frequency=400)
#         self.music_player = Player()
#         self.music_player.queue(song)
#         self.music_player.volume = float(self.volume) / 100.0
#         self.music_player.play()

#     def closeForm(self, event):
#         self.destroy()


# import shelve
# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox
# from threading import Thread
# from playsound import playsound
# import pyglet
# from pyglet.resource import media
# from pyglet.media import Player
# from tkinter import *
# from playerWin import PlayerWin

# class CurrentGame(tk.Toplevel):


#     def __init__(self,root):
#         self.music_player = Player()
#         self.volume = 50
#         shelveFile = shelve.open("shelveData", flag="r")
#         self.player1Name = shelveFile["player1Name"]
#         self.player2Name = shelveFile["player2Name"]
#         self.clicksNumber = shelveFile["clicksNumber"]
#         if "volume" in shelveFile:
#             self.volume = shelveFile["volume"]
#         shelveFile.close()

#         self.root = root


#         self.countPressButton1 = 0
#         self.countPressButton2 = 0

#         super().__init__(root)
#         self.initForm()
#         self.title('Нажми на кнопку')
#         self.wm_state('zoomed')
#         self.resizable(0, 0)
#         self.attributes('-fullscreen', True)

#     def initForm(self):


#         self.btnCloseForm = tk.Button(self, text='Покинуть игру', command=self.destroy, background="black",
#                                       foreground="white", font="Verdana 40 bold", width=12, borderwidth=2,
#                                       relief='solid')
#         self.btnCloseForm.pack(padx=10, pady=5, side=BOTTOM, fill=X)
#         f1 = tk.Frame(self, bg='#E90000')
#         f1.pack(side=LEFT, fill=BOTH, expand=1)
#         l1 = Label(f1, width=100, height=1, bg='#E90000')
#         l1.pack(fill=X)
#         self.labelClicksNumberUser1 = tk.Label(f1, text=self.player1Name + '\n' + '0', fg='white', bg='#E90000', font="Verdana 40 bold", padx=0, pady=0)
#         self.labelClicksNumberUser1.pack(expand=1)

#         f2 = tk.Frame(self, bg='#10C5FF')
#         f2.pack(side=LEFT, fill=BOTH, expand=1)

#         l2 = Label(f2, width=100, height=1, bg='#10C5FF')
#         l2.pack(fill=X)
#         self.labelClicksNumberUser2 = tk.Label(f2, text=self.player2Name + '\n' + '0', fg='white', bg='#10C5FF', font="Verdana 40 bold", padx=0, pady=0)
#         self.labelClicksNumberUser2.pack(expand=1)


#         self.bind('1', self.player1btn)
#         self.bind('2', self.player2btn)
#         self.bind('<Escape>', self.closeForm)


#         self.grab_set()
#         self.focus_set()

#     def player1btn(self, event):
#         self.countPressButton1 = self.countPressButton1 + 1
#         self.labelClicksNumberUser1.configure(text=self.player1Name + '\n' + str(self.countPressButton1))
#         Thread(target=self.musicPlayer1, daemon=True).start()
#         if int(self.countPressButton1) == int(self.clicksNumber):
#             PlayerWin(self.root, self.player1Name, '1')
#             self.destroy()


#     def player2btn(self, event):
#         self.countPressButton2 = self.countPressButton2 + 1
#         self.labelClicksNumberUser2.configure(text=self.player2Name + '\n' + str(self.countPressButton2))
#         Thread(target=self.musicPlayer2, daemon=True).start()
#         if int(self.countPressButton2) == int(self.clicksNumber):
#             PlayerWin(self.root, self.player2Name, '2')
#             self.destroy()

#     def musicPlayer1(self):
#         song = pyglet.media.synthesis.Sawtooth(duration=0.08, frequency=350)
#         self.music_player = Player()
#         self.music_player.queue(song)
#         self.music_player.volume = float(self.volume)/100.0
#         self.music_player.play()

#     def musicPlayer2(self):
#         song = pyglet.media.synthesis.Sawtooth(duration=0.08, frequency=400)
#         self.music_player = Player()
#         self.music_player.queue(song)
#         self.music_player.volume = float(self.volume)/100.0
#         self.music_player.play()

#     def closeForm(self, event):
#         self.destroy()
