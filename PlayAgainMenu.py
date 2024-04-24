from pathlib import Path
import os
import tkinter as tk 
from tkinter import Button, PhotoImage

# Get path of image
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Play again menu
class PlayAgainMenu:

    # Constructor
    def __init__(self, master, mode):
        # Master of menu
        self.master = master

        # Mode text
        # 1: Play again       2: End game
        self.mode = mode
        if self.mode == 1:
            self.warn_text = "ARE YOU SURE PLAY AGAIN?"
        if self.mode == 2:
            self.warn_text = "YOU HAVE FOUND ALL THE WORDS. PLAY AGAIN?"

        # Make window for menu
        self.toplevel = tk.Toplevel(master, height = 563, width = 275, bg="#FFFFFF")
        window_width = self.toplevel.winfo_reqwidth()
        window_height = self.toplevel.winfo_reqheight()
        position_right = int(self.toplevel.winfo_screenwidth()/2 - window_width/2)
        position_down = int(self.toplevel.winfo_screenheight()/2 - window_height/2)
        self.toplevel.geometry("+{}+{}".format(position_right - 50, position_down + 100))

        # Canvas for window
        self.canvas = tk.Canvas(
            self.toplevel,
            bg = "#FFFFFF",
            height = 275,
            width = 563,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.pack()

        # Canvas image background
        self.pl_image_image_1 = PhotoImage(
            file=relative_to_assets("pl_image_1.png"))
        self.pl_image_1 = self.canvas.create_image(
            281.0,
            137.0,
            image=self.pl_image_image_1
        )

        # Canvas BUTTON 1: YES
        self.pl_button_image_1 = PhotoImage(
            file=relative_to_assets("pl_button_1.png"))
        self.pl_button_1 = Button(
            self.toplevel,
            image=self.pl_button_image_1,
            text="YES",
            compound="center",  # Add this line
            borderwidth=0,
            highlightthickness=0,
            command=self.run_menu,
            relief="flat",
            font=("Nunito Bold", 20 * -1),  # Change the font size here
            fg="#A97E54"  # Change the font color here
        )
        self.pl_button_1.place(
            x=166.0,
            y=147.0,
            width=97.0,
            height=37.0
        )

        # Canvas BUTTON 2: NO
        self.pl_button_image_2 = PhotoImage(
            file=relative_to_assets("pl_button_2.png"))
        self.pl_button_2 = Button(
            self.toplevel,
            image=self.pl_button_image_2,
            text="NO",
            compound="center",  # Add this line
            borderwidth=0,
            highlightthickness=0,
            command=self.run_play,
            relief="flat",
            font=("Nunito Bold", 20 * -1),  # Change the font size here
            fg="#A97E54"  # Change the font color here
        )
        self.pl_button_2.place(
            x=295.0,
            y=147.0,
            width=97.0,
            height=37.0
        )

        # Canvas TEXT
        self.canvas.create_text(
            281.5,
            95.0,
            anchor="center",
            text= self.warn_text,
            fill="#A97E54",
            font=("Nunito Bold", 20 * -1),
            justify= "center"
        )

    # YES
    def run_menu(self):
        self.toplevel.destroy()
        self.master.destroy()
        os.system('python MainMenu.py')

    # NO    
    def run_play(self):
        if self.mode == 1:
            self.toplevel.destroy()
        if self.mode == 2:
            self.toplevel.destroy()
            self.master.destroy()
