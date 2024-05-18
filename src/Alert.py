from pathlib import Path
from tkinter import Canvas, Button, PhotoImage
import tkinter as tk

# Get path of image
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Alert window
class Alert:

    # Constructor
    def __init__(self, master, mode, wait_time =None):
        # Master of alert window
        self.master = master

        # Mode text
        # 1: Word       2: Topic     3: Subject     4: Remove word      5: Check Internet       6: Delay
        self.mode = mode
        if self.mode == 1:
            self.warn_text = "! YOU MUST TO TYPE WORD LIST"
        if self.mode == 2:
            self.warn_text = "! YOU MUST TO TYPE TOPIC NAME"
        if self.mode == 3:
            self.warn_text = "! YOU MUST TO TYPE SUBJECT NAME"
        if self.mode == 4:
            self.warn_text = "! WORDS THAT DO NOT FIT THE TABLE SIZE\n WILL BE AUTOMATICALLY DELETED"
        if self.mode == 5:
            self.warn_text = "! NO INTERNET CONNECTION.\nCONNECT TO THE INTERNET TO GENERATE WORDS."
        if self.mode == 6:
            self.warn_text = f"WAIT! PLEASE WAIT {wait_time} MORE SECONDS\n BEFORE PRESSING THE AI BUTTON AGAIN."
            
        # Make window
        self.toplevel = tk.Toplevel(master, height = 563, width = 275, bg="#FFFFFF")
        self.toplevel.grab_set()
        window_width = self.toplevel.winfo_reqwidth()
        window_height = self.toplevel.winfo_reqheight()
        position_right = int(self.toplevel.winfo_screenwidth()/2 - window_width/2)
        position_down = int(self.toplevel.winfo_screenheight()/2 - window_height/2)
        self.toplevel.geometry("+{}+{}".format(position_right - 50, position_down + 120))

        # Canvas for window
        self.canvas = Canvas(
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
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("alert_image_1.png"))
        self.image_1 = self.canvas.create_image(
            281.0,
            137.0,
            image=self.image_image_1
        )

        # Canvas TEXT
        self.canvas.create_text(
            563.0 / 2,
            101.0,
            anchor="center",
            text=self.warn_text,
            fill="#A97E54",
            font=("Nunito Bold", 20 * -1),
            justify="center"
        )

        # Canvas BUTTON: OK
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("alert_button_1.png"))
        self.button_1 = Button(
            self.toplevel,
            image=self.button_image_1,
            text="OK",
            compound="center",  # Add this line
            borderwidth=0,
            highlightthickness=0,
            command=self.ok_button,
            relief="flat",
            font=("Nunito Bold", 20 * -1),  # Change the font size here,
            fg = "#A97E54",
        )
        self.button_1.place(
            x=233.0,
            y=143.0,
            width=97.0,
            height=37.0
        )

    # Exit Alert window
    def ok_button(self):
        self.toplevel.destroy()




    


