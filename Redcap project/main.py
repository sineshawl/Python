import customtkinter as ctk

ctk.set_default_color_theme('blue')

# window = ctk.CTk()

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('CTK APP')
        self.geometry('600x400')
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame1 = ctk.CTkFrame(self)
        self.frame1.grid(row = 0, column=0, padx=10, pady=(30,30), sticky="nsw")

        self.btn1 = ctk.CTkButton(self.frame1, text="Button 1", corner_radius=100)
        self.btn1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")

        self.btn2 = ctk.CTkButton(self.frame1, text="Button 2")
        self.btn2.grid(row=0, column=2, padx=10, pady=(10, 0), sticky="nsw")

        self.btn3 = ctk.CTkButton(self.frame1, text="Button 3")
        self.btn3.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")

        self.frame2 = ctk.CTkFrame(self)
        self.frame2.grid(row = 0, column=1, padx=10, pady=(10,10), sticky="nswe")

        self.btn1 = ctk.CTkButton(self.frame2, text="Button 1")
        self.btn1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

        self.btn2 = ctk.CTkButton(self.frame2, text="Button 2")
        self.btn2.grid(row=0, column=2, padx=10, pady=(10, 0), sticky="w")

        self.btn3 = ctk.CTkButton(self.frame2, text="Button 3")
        self.btn3.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")

        self.frame3 = ctk.CTkFrame(self)
        self.frame3.grid(row = 0, column=2, padx=10, pady=(10,10), sticky="nse")

        self.btn1 = ctk.CTkButton(self.frame3, text="Button 1")
        self.btn1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

        self.btn2 = ctk.CTkButton(self.frame3, text="Button 2")
        self.btn2.grid(row=0, column=2, padx=10, pady=(10, 0), sticky="w")

        self.btn3 = ctk.CTkButton(self.frame3, text="Button 3")
        self.btn3.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")


app = App()

app.mainloop()











