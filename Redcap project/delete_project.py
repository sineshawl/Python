import customtkinter as ctk
from redcap_project import project_name
import json
from PIL import Image
class delete_project(ctk.CTkToplevel):
    def __init__(self, master, project_id):
        super().__init__(master)
        self.title('Delete Project')
        self.geometry('300x200')
        self.resizable(width=False, height=False)

        self.btn_ok = ctk.CTkButton(self, text='Delete', fg_color='red')
        self.btn_ok.pack(side='left', padx=10)
        self.btn_cancel = ctk.CTkButton(self, text='Cancel')
        self.btn_cancel.pack(side='right', pady=10)



