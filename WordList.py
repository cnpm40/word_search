import tkinter as tk
from GridWord import *

class WordList:
    def __init__(self, master, words, hint):
        self.master = master # Master of WordList

        # Frame of WordList
        self.frame = tk.Frame(master, width=567, height=182)
        self.frame.place(x=981.0, y=100.0)

        # Canvas of WordList
        self.canvas = tk.Canvas(self.frame, width=182, height=567, bg="#F3F3F3")
        self.canvas.pack()

        self.words = words # List of words

        self.hint = hint # List of hints
        self.grid = None # Grid Object

        self.word_list = [] # List of text labels of word

        # Draw WordList column on window
        self.draw_word_list()

    # Set Grid
    def setGrid(self, grid):
        self.grid = grid

    # Draw WordList column
    def draw_word_list(self):
        # Set the height of text label
        height = 40
        if height * (len(self.words) + 0.5) > 567:
            height = 567 / len(self.words)

        # Draw text label 
        for i in range(len(self.words)):
            label = self.canvas.create_text(182 / 2, height * (i + 0.5), text=self.words[i], fill="red", anchor="center", tags="label", font=("Nunito", 18, "bold"), justify= "center")
            self.canvas.tag_bind(label, "<Button-1>", lambda event, index=i: self.on_text_click(self.words[index]))
            self.word_list.append(label)

    # Event click the left mouse button to get hint of word
    def on_text_click(self, word):
        self.grid.get_hint(word)

    # Disable text label of word in WordList column
    def disable_word(self):
        # Set the height of text label
        height = 40
        if height * (len(self.words) + 0.5) > 567:
            height = 567 / len(self.words)

        # If word have been found, hightlight and disable the text label of this word in WordList column
        for i in range(len(self.grid.is_correct)):
            if self.grid.is_correct[i] == True:
                self.canvas.create_text(182 / 2, height * (i + 0.5), text=self.words[i], fill="Green", anchor="center", tags="label", font=("Nunito", 18, "bold"), justify= "center")

                


