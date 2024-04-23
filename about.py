from customtkinter import *
from pathlib import Path
import tkinter as tk 
from tkinter import Button, PhotoImage


# Get path of image
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# AboutMenu
class About:

    # Constructor
    def __init__(self, master):
        # Master of about menu
        self.master = master

        # Make window for about menu
        self.toplevel = tk.Toplevel(master, height = 1000, width = 600, bg="#FFFFFF")
        window_width = self.toplevel.winfo_reqwidth()
        window_height = self.toplevel.winfo_reqheight()
        position_right = int(self.toplevel.winfo_screenwidth()/2 - window_width/2)
        position_down = int(self.toplevel.winfo_screenheight()/2 - window_height/2)
        self.toplevel.geometry("+{}+{}".format(position_right - 110, position_down + 150))

        # Canvas about menu
        self.canvas = tk.Canvas(
            self.toplevel,
            bg = "#FFFFFF",
            height = 600,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.pack()

        # Canvas image background
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("help_image_1.png"))
        self.image_1 = self.canvas.create_image(
            590.0,
            354.0,
            image=self.image_image_1
        )

        # Canvas TEXT
        self.canvas.create_text(
            111.0,
            46.0,
            anchor="nw",
            text="WELCOME\nWORD SEARCH GENERATOR\n",
            fill="#BD946F",
            font=("Nunito Bold", 32 * -1)
        )
        self.canvas.create_text(
            111.0,
            174.0,
            anchor="nw",
            text="ABOUT\n\nThis is a word search generator that\ncreates a word search puzzle from a list\nof words. The words can be placed in any\norientation, and in any direction.\n\nThe puzzle can be printed or saved as a\nPDF file.\n",
            fill="#BD946F",
            font=("Nunito Bold", 32 * -1)
        )

        # Canvas BUTTON 1: HOME
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("help_button_1.png"))
        self.button_1 = Button(
            self.toplevel,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.run_home,
            relief="flat"
        )
        self.button_1.place(
            x=7.0,
            y=0.0,
            width=35.0,
            height=35.0
        )

    # Exit about menu
    def run_home(self):
        self.toplevel.destroy()    


