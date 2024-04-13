import tkinter as tk
import word_search_generator

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
        entry_window.geometry('600x350')
        entry_window.iconbitmap("./image/w.ico")

        text_label = tk.Label(entry_window, text= 'Type your words here, split by ",":', font=("", 12))
        text_label.pack(pady= 10, ipady= 10)

        entry = tk.Text(entry_window, width= 70, height= 10, borderwidth= 10)
        entry.pack(pady= 10)
        


    def print_word(self):
        print(self.words)

        
def main():
    app = WordSearchApp()
    app.mainloop()

if __name__ == '__main__':
    main()