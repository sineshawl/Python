import customtkinter
import customtkinter as ctk

#ctk.set_appearance_mode('system')
#ctk.set_default_color_theme('dark-blue')

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('CTK APP')
        # self.iconbitmap('Images/icon.webp')
        self.geometry('600x400')
    

        self.resizable(width=True, height=True)
        
        self.mainFrame = ctk.CTkFrame(self)
        self.rowconfigure(0, weight=1) 
        self.columnconfigure(0, weight=1)

        self.mainFrame.grid(row=0, column=0,sticky="nswe")

        self.mainFrame.grid_columnconfigure((0, 2), weight=1)
        self.mainFrame.grid_columnconfigure(1, weight=10)
        self.mainFrame.grid_rowconfigure(0, weight=1)

        self.frame1 = ctk.CTkFrame(self.mainFrame)
        self.frame1.place(relx=0.01, rely=0.02, relwidth=0.18, relheight=0.96)
        # self.frame1.grid(row = 0, column=0, padx=10, pady=(10,10), sticky="nswe")
        self.frame1.rowconfigure(0, weight=1)
        self.frame1.rowconfigure(1, weight=15)
        self.frame1.columnconfigure(0, weight=1)

        self.frame1_1 = ctk.CTkFrame(self.frame1, fg_color="gray", corner_radius=100 , width=120, height=120)
        self.frame1_1.grid(row = 0, column=0, padx=20, pady=(10, 0))


        self.frame1_2 = ctk.CTkFrame(self.frame1, fg_color="gray", corner_radius=10)
        self.frame1_2.grid(row = 1, column=0, padx=10, pady=(10, 10), sticky="nsew")

        self.label_user = ctk.CTkLabel(self.frame1_2, text="user", font=('Arial', 20))
        self.label_user.pack()

        

        
        self.switch_theme =ctk.CTkSwitch(self.frame1_2, text=f"switch to Theme", command=self.switch_theme, onvalue="on", offvalue="of")
        self.switch_theme.pack(side='bottom', pady=10)

        



        self.frame2 = ctk.CTkFrame(self.mainFrame)
        self.frame2.place(relx=0.21, rely=0.02, relwidth=0.54, relheight=0.96)
        # self.frame2.grid(row = 0, column=1, padx=10, pady=(10,10), sticky="nsew")

        self.frame2.rowconfigure(0, weight=1)
        self.frame2.rowconfigure(1, weight=15)
        self.frame2.columnconfigure(0, weight=5)
        
        self.frame2_1 = ctk.CTkFrame(self.frame2, fg_color="gray", corner_radius=35, height=120 )
        self.frame2_1.grid(row = 0, column=0, padx=10, pady=(10,0), sticky="nsew")



        self.frame2_2 = ctk.CTkFrame(self.frame2, fg_color="gray", corner_radius=10  )
        self.frame2_2.grid(row = 1, column=0, padx=10, pady=(10,10), sticky="nsew")





        self.frame3 = ctk.CTkFrame(self.mainFrame)
        self.frame3.place(relx=0.77, rely=0.02, relwidth=0.22, relheight=0.96)

        # self.frame3.grid(row = 0, column=2, padx=10, pady=(10,10), sticky="nsew")

        self.frame3.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
        self.frame3.columnconfigure(0, weight=1)



        self.combo_data_category = ctk.CTkComboBox(self.frame3, values=['Select Data Category','Extraction Layout', 'Assay Layout', 'Raw Data'])
        self.combo_data_category.grid(row=0, column=0, padx=5, pady=5, sticky='ew')

        self.combo_google_sheet_url = ctk.CTkComboBox(self.frame3, values=['Google Sheet Url','Dark', 'Light'])
        self.combo_google_sheet_url.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

        self.combo_redcap_project = ctk.CTkComboBox(self.frame3, values=['Redcap Project','Dark', 'Light'])
        self.combo_redcap_project.grid(row=2, column=0, padx=5, pady=5, sticky='ew')

        self.btn_hide = ctk.CTkButton(self.frame3, text='Hide User Frame', command=self.show_hide_frame )
        self.btn_hide.grid(row=3, column=0, padx=5, pady=5, sticky='nsew')
        self.frame_status= True
        self.frame1_start = 0.01
        self.frame2_start = 0.21
        self.frame3_start = 0.79
        self.frame1_width = 0.18
        self.frame2_width = 0.54
        self.frame3_width = 0.22
    def show_hide_frame(self):
        if self.frame_status:
            self.hide_frame()
            self.frame_status=False
        elif not self.frame_status:
            self.show_frame()
            self.frame_status=True
    def hide_frame(self):
        print('Hide Frame')
        if self.frame1_start > -0.17:
            self.frame1_start -=0.05
            self.frame2_start -=0.05
            self.frame3_start -=0.05
            self.frame2_width +=0.05
            


            self.frame1.place(relx=self.frame1_start, rely=0.02, relwidth=0.18, relheight=0.96)
            self.frame2.place(relx=self.frame2_start, rely=0.02, relwidth=self.frame2_width, relheight=0.96)
            self.after(1, self.hide_frame)
    def show_frame(self):
        
        if self.frame1_start < 0.01:
            self.frame1_start +=0.05
            self.frame2_start +=0.05
            self.frame2_width -=0.05

            self.frame1.place(relx=self.frame1_start, rely=0.02, relwidth=0.18, relheight=0.96)
            self.frame2.place(relx=self.frame2_start, rely=0.02, relwidth=self.frame2_width, relheight=0.96)
            self.after(1, self.show_frame)

    def switch_theme(self):
        if self._get_appearance_mode() == 'dark':
            customtkinter.set_appearance_mode('light')
        else:
            customtkinter.set_appearance_mode('dark')



            



app = App()

app.mainloop()









