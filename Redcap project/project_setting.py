import customtkinter as ctk
from PIL import Image, ImageTk
import json, requests

from add_project import add_project




project_list= {}
api_list = {}

with open('api_keys_label.json', mode='r') as file:
    project_list=json.load(file)

with open('api_keys.json', mode='r') as file:
    api_list = json.load(file)



class projectSetting(ctk.CTkFrame):
    def minimize(self):
       self.place(relx=0, rely=0, relwidth=0, relheight=0)
       


    def edit_token(self, key, value):
        self.edit_popup = ctk.CTkInputDialog(text=api_list[key][value], title='Edit API token')
    def add_token(self, key):
        self.add_popup = ctk.CTkInputDialog(text='Enter the API token', title='Add new API token', command=lambda:print(self.add_popup.getvar()))
        # print(self.add_popup.getvar())
    def delete_token(self, key, value):
        # self.delete_token = ctk.CTkLabel
        self.edit_popup = ctk.CTkInputDialog(text=api_list[key][value], title='Edit API token')


    def __init__(self, master):
        super().__init__(master)
        self.place(relx=0.01, rely=0.01, relwidth=0.76, relheight=0.99)

        
        self.btn_back = ctk.CTkButton(self, text="⇠",font=('Arial', 20) ,text_color=('black', 'white'), fg_color=('white', 'black'), command=self.minimize)
        self.btn_back.place(relx=0.92, rely=0.02, relwidth=0.07, relheight=.03)
    


        self.inner_frame = ctk.CTkScrollableFrame(self)
        self.inner_frame.place(relx=0.02, rely=0.02, relwidth=0.89, relheight=0.98)



        self.inner_frame.columnconfigure(0, weight=3)
        self.inner_frame.columnconfigure((0,1,2,3), weight=1)

        self.add_icon = Image.open('Images/add.png').resize((20,20))
        self.add_image = ctk.CTkImage(self.add_icon)

        self.edit_icon = Image.open('Images/edit.png').resize((20, 20))
        self.edit_image = ctk.CTkImage(self.edit_icon)
        
        self.delete_icon = Image.open('Images/delete.png').resize((20, 20))
        self.delete_image = ctk.CTkImage(self.delete_icon)

        self.add_category_icon = Image.open('Images/new-folder.png').resize((20,20))
        self.add_category_image = ctk.CTkImage(self.add_category_icon)
        counter = 0

        for key in project_list.keys():
            self.lbl_category = ctk.CTkLabel(self.inner_frame, text=key, anchor='w', font=('Helvetica', 12, 'bold'), text_color='#2682E3')
            self.lbl_category.grid(row = counter, column=0, padx=10, pady=5, sticky='ew')
            for value in project_list[key]:
                counter +=1
                value_index = 0
                self.lbl_project = ctk.CTkLabel(self.inner_frame, text=value, anchor='w')
                self.lbl_project.grid(row = counter, column=0, padx=(10,1), pady=1, sticky='nsew')

                self.btn_edit = ctk.CTkButton(self.inner_frame,text=None, width=30, fg_color="transparent",  image=self.edit_image, command =lambda: self.edit_token(key, value_index))
                self.btn_edit.grid(row = counter, column=1, padx=1, pady=1, sticky='nsew')   
                
                self.btn_delete = ctk.CTkButton(self.inner_frame, text=None, width=30, fg_color="transparent", image=self.delete_image)
                self.btn_delete.grid(row = counter, column=2, padx=1, pady=1, sticky='nsew') 

                value_index +=1
            counter +=1  
            self.btn_add = ctk.CTkButton(self.inner_frame, text=None, width=30, fg_color="transparent", image=self.add_image, command=lambda:add_project(self, key))
            self.btn_add.grid(row = counter, column=0, padx=(10,1), pady=1, sticky='nsew')

            counter += 1 
        self.btn_add_category = ctk.CTkButton(self.inner_frame, text='Add new Category', width=30, image=self.add_category_image)
        self.btn_add_category.grid(row = counter, column=0, padx=(10,1), pady=1, sticky='nsew') 






            

