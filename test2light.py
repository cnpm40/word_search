import tkinter as tk

class GridWord:
    def __init__(self, master, grid_data, words):
        self.master = master

        self.frame = tk.Frame(master, width=560, height=560)
        self.frame.place(x=320, y=40)

        self.canvas = tk.Canvas(self.frame, width=560, height=560, bg="white")
        self.canvas.pack()
        
        # Tạo lưới chữ cái (mô phỏng)
        self.grid_data = grid_data

        self.words = words
        
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
    
    def draw_grid(self):
        cell_width = (880 - 320) / len(self.grid_data)
        cell_height = (600 - 40) / len(self.grid_data)
        for i in range(len(self.grid_data)):
            for j in range(len(self.grid_data[i])):
                x0 = j * cell_width
                y0 = i * cell_height
                x1 = x0 + cell_width
                y1 = y0 + cell_height 
                self.canvas.create_rectangle(x0, y0, x1, y1, outline="black", width=2)
                self.canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=self.grid_data[i][j], font=("Arial", 12))
    
    def start_highlight(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        column = event.x // 40
        row = event.y // 40
        self.start_pos = (row, column)

    def draw_highlight(self, event):
        self.clear_highlight(event) 

        self.end_x = self.canvas.canvasx(event.x)
        self.end_y = self.canvas.canvasy(event.y)

        self.highlight_id = self.canvas.create_line(
            self.start_x, self.start_y, self.end_x, self.end_y, fill = "blue", width=32, capstyle="round", joinstyle="round", stipple='gray50')  

    def end_highlight(self, event):
        column = event.x // 40
        row = event.y // 40
        self.end_pos = (row, column)
        print(self.start_pos, self.end_pos)
        if self.check():
            self.canvas.create_line(
                self.start_x, self.start_y, self.end_x, self.end_y, fill = "blue", width=32, capstyle="round", joinstyle="round", stipple='gray50')
        else:  
            self.clear_highlight(event)   

    def clear_highlight(self, event):
        if self.highlight_id:
            self.canvas.delete(self.highlight_id)


    def check(self):
        word = ''   
        if self.end_pos[0] < 0 or self.end_pos[1] < 0 or self.end_pos[0] > len(self.grid_data) - 1 or self.end_pos[1] > len(self.grid_data) - 1:
            return False

        if self.start_pos[0] == self.end_pos[0]:
            y0 = min(self.start_pos[1], self.end_pos[1])
            y1 = max(self.start_pos[1], self.end_pos[1])
            for y in range(y0, y1 + 1):
                word += self.grid_data[self.start_pos[0]][y]

        if self.start_pos[1] == self.end_pos[1]:
            x0 = min(self.start_pos[0], self.end_pos[0])
            x1 = max(self.start_pos[0], self.end_pos[0])
            for x in range(x0, x1 + 1):
                word += self.grid_data[x][self.start_pos[1]]

        if abs(self.start_pos[0] - self.end_pos[0]) == abs(self.start_pos[1] - self.end_pos[1]):
            dx = 1 if self.start_pos[0] < self.end_pos[0] else -1
            dy = 1 if self.start_pos[1] < self.end_pos[1] else -1
            x, y = self.start_pos[0], self.start_pos[1]

            while x != self.end_pos[0] + dx and y != self.end_pos[1] + dy:
                word += self.grid_data[x][y]
                x += dx
                y += dy
        print(word)
        if (word in self.words) or (word[::-1] in self.words):
            return True
        else: return False

    
    

# root = tk.Tk()
# app = GridWord(root)
# root.mainloop()
