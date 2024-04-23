import tkinter as tk
from WordList import *
from PlayAgainMenu import *

class GridWord:
    def __init__(self, master, grid_data, words, hint, wordlist):
        self.master = master # Master of grid word

        # Frame of grid word
        self.frame = tk.Frame(master, width=630, height=630)
        self.frame.place(x=332, y=37)

        # Canvas of grid word
        self.canvas = tk.Canvas(self.frame, width=630, height=630, bg="#F3F3F3")
        self.canvas.place(x= 0, y=0)
        
        self.grid_data = grid_data # Grid of characters of puzzle

        self.words = words # List of words

        self.hint = hint # List of hints position

        self.is_hinted = [[False for _ in range(len(self.grid_data[0]))] for _ in range(len(self.grid_data))] # Grid of characters have been hinted

        self.wordlist = wordlist # WordList object

        self.is_correct = [False for _ in range(len(self.words))] # List of words have been found

        self.cell_width = int(630 / len(self.grid_data)) # Width of single rectangle
        self.cell_height = int(630 / len(self.grid_data)) # Height of single rectangle
        
        # Vẽ lưới chữ cái
        self.draw_grid()
        
        # Bắt đầu và kết thúc của từ (mô phỏng)
        self.start_pos = None
        self.end_pos = None
        self.highlight_id = None
        
        # Bắt đầu nghe sự kiện chuột
        self.canvas.bind("<ButtonPress-1>", self.start_highlight)
        self.canvas.bind("<B1-Motion>", self.draw_highlight)
        self.canvas.bind("<ButtonRelease-1>", self.end_highlight)
        self.canvas.bind("<Leave>", self.clear_highlight)
    
    # Draw grid on the window
    def draw_grid(self):
        for i in range(len(self.grid_data)):
            for j in range(len(self.grid_data[i])):
                x0 = j * self.cell_width
                y0 = i * self.cell_height
                x1 = x0 + self.cell_width
                y1 = y0 + self.cell_height 
                if (self.grid_data[i][j] != ''):
                    self.canvas.create_rectangle(x0, y0, x1, y1, outline="black", width=2, fill= "white")
                    self.canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=self.grid_data[i][j], font=("Arial", 12))
    
    # Event press left mouse button to start highlight word
    def start_highlight(self, event):
        # Get the position of event
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        column = event.x // self.cell_width
        row = event.y // self.cell_height
        self.start_pos = (row, column)

        self.delete_hint(event)

    # Event hold left mouse button to draw highlight word
    def draw_highlight(self, event):
        self.clear_highlight(event) 
        self.delete_hint(event)

        # Get the position of event
        self.end_x = self.canvas.canvasx(event.x)
        self.end_y = self.canvas.canvasy(event.y)

        # Draw highlight
        self.highlight_id = self.canvas.create_line(
            self.start_x, self.start_y, self.end_x, self.end_y, fill = "blue", width= self.cell_height * 4 / 5, capstyle="round", joinstyle="round", stipple='gray50')
  
    # Event release left mouse button to end highlight word
    def end_highlight(self, event):
        # Get the position of event
        column = event.x // self.cell_width
        row = event.y // self.cell_height
        self.end_pos = (row, column)

        if self.check():
            # Draw hightlight
            self.canvas.create_line(
                self.start_x, self.start_y, self.end_x, self.end_y, fill = "blue", width= self.cell_height * 4 / 5, capstyle="round", joinstyle="round", stipple='gray50')
            self.wordlist.disable_word() # If word is correct, disable this word in WordList column
        else:  
            self.clear_highlight(event) 
        if self.check_if_end():
            PlayAgainMenu(self.master, 2) # If all the words have been found, open play again menu
         
    # Delete highlight
    def clear_highlight(self, event):
        if self.highlight_id:
            self.canvas.delete(self.highlight_id)

    # Check if the word highlighted is correct
    def check(self):
        word = ''  

        # Check if the highlight is out of the grid 
        if self.end_pos[0] < 0 or self.end_pos[1] < 0 or self.end_pos[0] > len(self.grid_data) - 1 or self.end_pos[1] > len(self.grid_data) - 1:
            return False

        # Get row
        if self.start_pos[0] == self.end_pos[0]:
            y0 = min(self.start_pos[1], self.end_pos[1])
            y1 = max(self.start_pos[1], self.end_pos[1])
            for y in range(y0, y1 + 1):
                word += self.grid_data[self.start_pos[0]][y]

        # Get column
        if self.start_pos[1] == self.end_pos[1]:
            x0 = min(self.start_pos[0], self.end_pos[0])
            x1 = max(self.start_pos[0], self.end_pos[0])
            for x in range(x0, x1 + 1):
                word += self.grid_data[x][self.start_pos[1]]

        # Get diagonal
        if abs(self.start_pos[0] - self.end_pos[0]) == abs(self.start_pos[1] - self.end_pos[1]):
            dx = 1 if self.start_pos[0] < self.end_pos[0] else -1
            dy = 1 if self.start_pos[1] < self.end_pos[1] else -1
            x, y = self.start_pos[0], self.start_pos[1]

            while x != self.end_pos[0] + dx and y != self.end_pos[1] + dy:
                word += self.grid_data[x][y]
                x += dx
                y += dy

        # Check word and reverse word        
        if (word in self.words) or (word[::-1] in self.words):
            if word in self.words:
                index = self.words.index(word)
            else: index = self.words.index(word[::-1])
            self.is_correct[index] = True
            return True
        else: return False

    # Get hint of word
    def get_hint(self, word):
        # Find hint position 
        index = self.words.index(word)
        (col, row) = eval(self.hint[index])
        col, row = col - 1, row - 1
        self.is_hinted[row][col] = True
        x0 = col * self.cell_width
        y0 = row * self.cell_height
        x1 = (col + 1) * self.cell_width
        y1 = (row + 1) * self.cell_height

        # Highlight hint
        self.canvas.create_rectangle(x0, y0, x1, y1, outline="black", width=2, fill= "yellow")
        self.canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=self.grid_data[row][col], font=("Arial", 12))

    # Delete highlighted hint
    def delete_hint(self, event):
        # Find hint position 
        col = event.x // self.cell_width
        row = event.y // self.cell_height

        # Delete hint
        if self.is_hinted[row][col] == True:
            x0 = col * self.cell_width
            y0 = row * self.cell_height
            x1 = (col + 1) * self.cell_width
            y1 = (row + 1) * self.cell_height
            if self.grid_data[row][col] != '':
                self.canvas.create_rectangle(x0, y0, x1, y1, outline="black", width=2, fill= "white")
                self.canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=self.grid_data[row][col], font=("Arial", 12))
            self.is_hinted[row][col] = False
    
    # Check if all the words have been found
    def check_if_end(self):
        return all(self.is_correct)
        