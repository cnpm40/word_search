import tkinter as tk
import word_search_generator
from word_search_generator import WordSearch

class WordSearchApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Word Search")
        self.iconbitmap("./image/w.ico")
        self.geometry("1280x720")

        game_header = tk.Frame(master= self)
        game_header.pack(fill=tk.X, side=tk.TOP)
        heading = tk.Label(game_header,
                       text='Word Search Game',
                       font=('Helvetica', 23, 'bold'),
                       fg='blue')
        heading.pack(expand=True, fill=tk.X, pady=12)

        self.write_button = tk.Button(self, text= "Write your own words", command= self.make_entry_window)
        self.write_button.pack(pady= 200)

        self.gen_button = tk.Button(self, text= "Generate Word")
        self.gen_button.pack(pady= 100)
    
    def make_entry_window(self):
        entry_window = tk.Toplevel(self)
        entry_window.title("Type Words")
        entry_window.geometry('600x350')
        entry_window.iconbitmap("./image/w.ico")

        text_label = tk.Label(entry_window, text= 'Type your words here, split by ",":', font=("", 12))
        text_label.pack(pady= 10, ipady= 10)

        entry = tk.Text(entry_window, width= 70, height= 10, borderwidth= 10)
        entry.pack(pady= 10)

        button_1 = tk.Button(entry_window, text= "Ok", height= 2, width= 20, command= lambda: self.get_word(entry, entry_window))
        button_1.pack(side= tk.LEFT, padx= 50)

        button_2 = tk.Button(entry_window, text= "Cancel", height= 2, width= 20, command= entry_window.destroy)
        button_2.pack(side= tk.RIGHT, padx= 50)

    def get_word(self, entry, widget):
        self.datas = entry.get("1.0", "end-1c")
        if self.datas:
            self.words = [data.strip() for data in self.datas.split(",")]
            self.generate_word()
            widget.destroy()
        else:
            top_widget = tk.Toplevel(widget)
            top_widget.title("Warning")
            top_widget.geometry('300x100')
            top_widget.iconbitmap("./image/w.ico")

            text_label = tk.Label(top_widget, text= "You haven't typed anything", font=("", 10))
            text_label.pack(side= tk.TOP, pady= 10)

            button = tk.Button(top_widget, text= "Ok", height= 2, width= 20, command= top_widget.destroy)
            button.pack(side= tk.BOTTOM, pady = 10)

    def generate_word(self):
        puzzle = WordSearch(self.datas)
        for row in puzzle._puzzle:
            print(*row)


def main():
    app = WordSearchApp()
    app.mainloop()

if __name__ == '__main__':
    main()