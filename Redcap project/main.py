import customtkinter
import customtkinter as ctk

# ctk.set_appearance_mode('system')
# ctk.set_default_color_theme('dark-blue')

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('CTK APP')
        self.iconbitmap('Images/redcap-icon.png')
        self.geometry('800x600')
    

        self.resizable(width=True, height=True)
        
        self.mainFrame = ctk.CTkFrame(self)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.mainFrame.grid(row=0, column=0,sticky="nswe")

        self.mainFrame.grid_columnconfigure((0, 2), weight=1)
        self.mainFrame.grid_columnconfigure(1, weight=10)
        self.mainFrame.grid_rowconfigure(0, weight=1)

        self.frame1 = ctk.CTkFrame(self.mainFrame)
        self.frame1.grid(row = 0, column=0, padx=10, pady=(10,10), sticky="nswe")
        self.frame1.rowconfigure(0, weight=1)
        self.frame1.rowconfigure(1, weight=15)
        self.frame1.columnconfigure(0, weight=1)

        self.frame1_1 = ctk.CTkFrame(self.frame1, fg_color="gray", corner_radius=100 , width=120, height=120)
        self.frame1_1.grid(row = 0, column=0, padx=20, pady=(10, 0))


        self.frame1_2 = ctk.CTkFrame(self.frame1, fg_color="gray", corner_radius=10)
        self.frame1_2.grid(row = 1, column=0, padx=10, pady=(10, 10), sticky="nsew")

        self.label_user = ctk.CTkLabel(self.frame1_2, text="user", font=('Arial', 20))
        self.label_user.pack()

        
        self.combo_theme = ctk.CTkComboBox(self.frame1_2, values=['Dark', 'Light'], command=self.switchTheme)
        self.combo_theme.pack(side="bottom", pady=10)





        self.frame2 = ctk.CTkFrame(self.mainFrame)
        self.frame2.grid(row = 0, column=1, padx=10, pady=(10,10), sticky="nsew")

        self.frame2.rowconfigure(0, weight=1)
        self.frame2.rowconfigure(1, weight=15)
        self.frame2.columnconfigure(0, weight=5)
        
        self.frame2_1 = ctk.CTkFrame(self.frame2, fg_color="gray", corner_radius=35, height=120 )
        self.frame2_1.grid(row = 0, column=0, padx=10, pady=(10,0), sticky="nsew")



        self.frame2_2 = ctk.CTkFrame(self.frame2, fg_color="gray", corner_radius=10  )
        self.frame2_2.grid(row = 1, column=0, padx=10, pady=(10,10), sticky="nsew")





        self.frame3 = ctk.CTkFrame(self.mainFrame)
        self.frame3.grid(row = 0, column=2, padx=10, pady=(10,10), sticky="nsew")

        self.frame3.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
        self.frame3.columnconfigure(0, weight=1)



        self.combo_data_category = ctk.CTkComboBox(self.frame3, values=['Select Data Category','Extraction Layout', 'Assay Layout', 'Raw Data'])
        self.combo_data_category.grid(row=0, column=0, padx=2, pady=2, sticky='ew')

        self.combo_google_sheet_url = ctk.CTkComboBox(self.frame3, values=['Google Sheet Url','Dark', 'Light'])
        self.combo_google_sheet_url.grid(row=1, column=0, padx=2, pady=2, sticky='ew')

        self.combo_redcap_project = ctk.CTkComboBox(self.frame3, values=['Redcap Project','Dark', 'Light'])
        self.combo_redcap_project.grid(row=2, column=0, padx=2, pady=2, sticky='ew')




    def switchTheme(self, choice):
        if choice == 'Dark':
            customtkinter.set_appearance_mode('dark')
        elif choice == 'Light':
            self.mainFrame._set_appearance_mode('light')
            customtkinter.set_appearance_mode('light')


            



app = App()

app.mainloop()









