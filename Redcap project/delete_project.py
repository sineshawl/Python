import customtkinter as ctk
from redcap_project import project_name
import json
from PIL import Image
class delete_project(ctk.CTkToplevel):
    def __init__(self, master, project_id):
        super().__init__(master)
        self.title('Delete Project')
        self.geometry('300x200')



