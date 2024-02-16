import customtkinter
import customtkinter as ctk

from project_setting import projectSetting

class leftFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=15)
        self.columnconfigure(0, weight=1)
        
        self.inner_frame1 = ctk.CTkFrame(self, fg_color="gray", corner_radius=100 , width=100, height=100)
        self.inner_frame1.grid(row = 0, column=0,padx=5)


        self.inner_frame2 = ctk.CTkFrame(self, fg_color="gray", corner_radius=10)
        self.inner_frame2.grid(row = 1, column=0, padx=10, pady=(10, 30), sticky="nsew")
    
        self.inner_frame2.columnconfigure(0, weight=1)

        self.label_user = ctk.CTkLabel(self.inner_frame2, text="user", font=('Arial', 20))
        self.label_user.grid(row = 0, column=0, padx=10, pady=2, sticky='ew')
        

        self.btn = ctk.CTkButton(self.inner_frame2, text='project setting', command=lambda: projectSetting(master))
        self.btn.grid(row = 1, column=0, padx=10, pady=(60, 0), sticky='ew')

        for i in range(3):
            self.button = ctk.CTkButton(self.inner_frame2, text=f'Button {i+1}')
            self.button.grid(row = i+2, column=0, padx=10, pady=10, sticky='nsew')


        self.switch_themer =ctk.CTkSwitch(self.inner_frame2, text="switch Theme", command=self.switch_theme, onvalue="on", offvalue="of")
        self.switch_themer.grid(row = 5, column=0, padx=10, pady=10, sticky='nsew')


  



    def switch_theme(self):
        if self._get_appearance_mode() == 'dark':
            customtkinter.set_appearance_mode('light')
        else:
            customtkinter.set_appearance_mode('dark')

        

class middleFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.columnconfigure(0, weight=5)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=8)
        
        self.inner_frame1 = ctk.CTkFrame(self, fg_color="gray", corner_radius=35, height=120 )
        self.inner_frame1.grid(row = 0, column=0, padx=10, pady=(10,0), sticky="nsew")

        self.inner_frame2 = ctk.CTkFrame(self, fg_color="gray", corner_radius=10  )
        self.inner_frame2.grid(row = 1, column=0, padx=10, pady=(10,30), sticky="nsew")
class rightFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
        self.columnconfigure(0, weight=1)

        self.combo_data_category = ctk.CTkComboBox(self, values=['Select Data Category','Extraction Layout', 'Assay Layout', 'Raw Data'])
        self.combo_data_category.grid(row=0, column=0, padx=5, pady=5, sticky='ew')

        self.combo_google_sheet_url = ctk.CTkComboBox(self, values=['Google Sheet Url','Dark', 'Light'])
        self.combo_google_sheet_url.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

        self.combo_redcap_project = ctk.CTkComboBox(self, values=['Redcap Project'])
        self.combo_redcap_project.grid(row=2, column=0, padx=5, pady=5, sticky='ew')

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('GPyRed')
        self.geometry('600x400')
    
        self.resizable(width=True, height=True)
        

        
        self.mainFrame = ctk.CTkFrame(self)
        self.rowconfigure(0, weight=1) 
        self.columnconfigure(0, weight=1)

        self.mainFrame.grid(row=0, column=0,sticky="nswe")

        self.mainFrame.grid_columnconfigure((0, 2), weight=1)
        self.mainFrame.grid_columnconfigure(1, weight=10)
        self.mainFrame.grid_rowconfigure(0, weight=1)

        self.frame1 = leftFrame(self.mainFrame) # Calling class leftFrame
        self.frame1.place(relx=0.01, rely=0.02, relwidth=0.18, relheight=0.92)


        self.btn_side_bar = ctk.CTkButton(self.mainFrame, text="←", font=('Arial',25),text_color=('black', 'white'), hover=False, fg_color=('white', 'black'),command=self.show_hide_frame)
        self.btn_side_bar.place(relx=0.01, rely=0.95, relwidth=0.06, relheight=0.04)

        self.frame2 = middleFrame(self.mainFrame)  # Calling class middleFrame
        self.frame2.place(relx=0.21, rely=0.02, relwidth=0.54, relheight=0.92)

        self.frame3 = rightFrame(self.mainFrame)
        self.frame3.place(relx=0.77, rely=0.02, relwidth=0.22, relheight=0.94)


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

        if self.frame1_start > -0.17:
            self.frame1_start -=0.05
            self.frame2_start -=0.05
            self.frame2_width +=0.05
            self.frame1.place(relx=self.frame1_start, rely=0.02, relwidth=0.18, relheight=0.92)
            self.frame2.place(relx=self.frame2_start, rely=0.02, relwidth=self.frame2_width, relheight=0.92)
            self.after(50, self.hide_frame) # calling function hide_frame after 100 milliseconds
            self.btn_side_bar.configure(text='→')

    def show_frame(self):
        
        if self.frame1_start < -0.01:
            self.frame1_start +=0.05
            self.frame2_start +=0.05
            self.frame2_width -=0.05

            self.frame1.place(relx=self.frame1_start, rely=0.02, relwidth=0.18, relheight=0.92)
            self.frame2.place(relx=self.frame2_start, rely=0.02, relwidth=self.frame2_width, relheight=0.92)
            self.after(50, self.show_frame)

            self.btn_side_bar.configure(text='←')






            


        


app = App()

app.mainloop()









