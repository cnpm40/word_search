from customtkinter import *
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
import os
from About import *

# Get path of image
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

'''
WINDOW
'''

# Make window
window = Tk()
window_width = window.winfo_reqwidth()
window_height = window.winfo_reqheight()
position_right = int(window.winfo_screenwidth()/2 - window_width/2)
position_down = int(window.winfo_screenheight()/2 - window_height/2)

window.geometry("+{}+{}".format(position_right-400, position_down-300))
window.geometry("1181x708")
window.configure(bg = "#FFFFFF")


'''
CANVAS
'''
# Canvas frame
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 708,
    width = 1181,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

# Canvas image background
canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("menu_image_1.png"))
image_1 = canvas.create_image(
    646.0,
    356.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("menu_image_2.png"))
image_2 = canvas.create_image(
    56.0,
    356.0,
    image=image_image_2
)

# Canvas welcome text
canvas.create_text(
    350.0,
    240.0,
    anchor="nw",
    text="WORD SEARCH GENERATOR",
    fill="#A97E54",
    font=("Nunito Bold", 35 * -1)
)
canvas.create_text(
    490.0,
    195.0,
    anchor="nw",
    text="WELCOME",
    fill="#A97E54",
    font=("Nunito Bold", 35 * -1)
)


'''
DEF
'''

# AI mode
def run_program_1():
    window.destroy()
    os.system("python Ai.py")

# Human mode
def run_program_2():
    window.destroy()
    os.system("python Human.py")

# About menu    
def run_program_3():
    about_menu = About(window)


'''
BUTTONS
'''
#Button 3: About
button_image_3 = PhotoImage(
    file=relative_to_assets("menu_button_3.png"))
button_3 = Button(
    image=button_image_3,
    text="About",
    compound="center",  # Add this line
    borderwidth=0,
    highlightthickness=0,
    command=run_program_3,
    relief="flat",
    font=("Nunito Bold", 24),  # Change the font size here
    fg="#A97E54"  # Change the font color here
)
button_3.place(
    x=447.0,
    y=451.0,
    width=287.0,
    height=48.0
)

#Button 2: Humanword
button_image_2 = PhotoImage(
    file=relative_to_assets("menu_button_2.png"))
button_2 = Button(
    image=button_image_2,
    text="Human's word",
    compound="center",  # Add this line
    borderwidth=0,
    highlightthickness=0,
    command=run_program_2,
    relief="flat",
    font=("Nunito Bold", 24),  # Change the font size here
    fg="#A97E54"  # Change the font color here
)
button_2.place(
    x=447.0,
    y=385.0,
    width=287.0,
    height=48.0
)

#Button 3: AIword
button_image_1 = PhotoImage(
    file=relative_to_assets("menu_button_1.png"))
button_1 = Button(
    image=button_image_1,
    text="AI's word",
    compound="center",  # Add this line
    borderwidth=0,
    highlightthickness=0,
    command=run_program_1,
    relief="flat",
    font=("Nunito Bold", 24),  # Change the font size here
    fg="#A97E54"  # Change the font color here
)
button_1.place(
    x=447.0,
    y=319.0,
    width=287.0,
    height=48.0
)

window.resizable(False, False)
window.mainloop()
