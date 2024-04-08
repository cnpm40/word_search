import customtkinter as ctk

class WordSearchApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Word Search")
        self.iconbitmap("./image/w.ico")
        self.geometry("1280x720")

        game_header = ctk.CTkFrame(master= self)
        game_header.pack(fill=ctk.X, side=ctk.TOP)
        heading = ctk.CTkLabel(game_header,
                       text='Word Search Game',
                       font=('Helvetica', 23, 'bold'),
                       fg_color='transparent')
        heading.pack(expand=True, fill=ctk.X, pady=12)

        self.write_button = ctk.CTkButton(self, text= "Write your own words", command= self.type_word)
        self.write_button.pack(pady= 200)

        self.gen_button = ctk.CTkButton(self, text= "Generate Word")
        self.gen_button.pack(pady= 100)
    
    def type_word(self):
        dialog = ctk.CTkInputDialog(text="Type your own words, split by ',' :", title="Type words")
        data = dialog.get_input()
        if data:
            self.words = data.split(",")
            self.words = [word.strip() for word in self.words]
            self.print_word()
        else:
            print("")

    def print_word(self):
        print(self.words)
        
def main():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("dark-blue")

    app = WordSearchApp()
    app.mainloop()

if __name__ == '__main__':
    main()