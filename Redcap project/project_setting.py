import customtkinter as ctk
from PIL import Image, ImageTk

class projectSetting(ctk.CTkFrame):
    def minimize(self):
       self.place(relx=0, rely=0, relwidth=0, relheight=0)
    def __init__(self, master):
        super().__init__(master)
        self.place(relx=0.01, rely=0.01, relwidth=0.5, relheight=0.99)

        self.btn_back = ctk.CTkButton(self, text="⇠",font=('Arial', 20) ,text_color=('black', 'white'), fg_color=('white', 'black'), command=self.minimize)
        self.btn_back.place(relx=0.92, rely=0.02, relwidth=0.07, relheight=.03)

        self.inner_frame = ctk.CTkScrollableFrame(self)
        self.inner_frame.place(relx=0.02, rely=0.02, relwidth=0.89, relheight=0.98)

        self.lbl_category = ctk.CTkLabel(self.inner_frame, text='project 1')
        counter = 0

        self.edit_icon = Image.open('Images/edit.png').resize((20, 20))
        self.edit_image = ImageTk.PhotoImage(self.edit_icon)

        self.delete_icon = Image.open('Images/delete.png').resize((20, 20))
        self.delete_image = ImageTk.PhotoImage(self.delete_icon)

        for i in range(5):
            self.lbl_category = ctk.CTkLabel(self.inner_frame, text=f'Category {i+1}')
            self.lbl_category.grid(row = counter, column=0, padx=10, pady=5, sticky='ew')
            for j in range(5):
                counter +=1
                self.lbl_project = ctk.CTkLabel(self.inner_frame, text=f'MNTD Project    {j+1}')
                self.lbl_project.grid(row = counter, column=1, padx=1, pady=1, sticky='nsew')

                self.btn_edit = ctk.CTkButton(self.inner_frame,text=None, width=30, fg_color="transparent",  image=self.edit_image)
                self.btn_edit.grid(row = counter, column=2, padx=1, pady=1, sticky='nsew')   
                
                self.btn_delete = ctk.CTkButton(self.inner_frame, text=None, width=30, fg_color="transparent", image=self.delete_image)
                self.btn_delete.grid(row = counter, column=3, padx=1, pady=1, sticky='nsew')   

            counter += 1  

    # def minimize(self):
    # #    self.place(relx=0, rely=0)
    #     pass
            

