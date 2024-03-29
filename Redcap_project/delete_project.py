import customtkinter as ctk
from redcap_project import project_name
import json
from PIL import Image
class delete_project(ctk.CTkToplevel):
    def __init__(self, master, project_id):
        super().__init__(master)
        self.title('Delete Project')
        self.focus()
        print(master)
        self.resizable(width=False, height=False)

        self.project_id = project_id - 1

        self.question_mark_icon = Image.open('Images/question-mark.png').resize((100,100))
        self.question_mark_image= ctk.CTkImage(self.question_mark_icon)

        self.btn = ctk.CTkButton(self, text=None, fg_color='transparent', hover=None, image=self.question_mark_image )
        self.btn.pack(pady=(20, 10))

         
        self.label = ctk.CTkLabel(self, text='Are you sure, you want to delete this project?')
        self.label.pack(pady=(5, 5))
        self.btn_ok = ctk.CTkButton(self, text='Delete', width=100, command=self.delete_project)
        self.btn_ok.pack(side='left', padx=(30, 1))
        self.btn_cancel = ctk.CTkButton(self, text='Cancel',fg_color='red', width=100, command=lambda:self.destroy())
        self.btn_cancel.pack(side='right', padx=(1, 30))
    def delete_project(self):
        project_list = {}

        with open('project_list.json', mode='r') as file:
            project_list = json.load(file)

        project_list['project_id'] = [id for id in range(1, len(project_list['project_id']))]     
        del project_list['redcap_folder_name'][self.project_id] 
        del project_list['redcap_project_name'][self.project_id] 
        del project_list['redcap_api'][self.project_id] 
        del project_list['structure_of_data'][self.project_id]
        del project_list['spreadsheet_url'][self.project_id] 
        del project_list['google_drive_id'][self.project_id] 

        with open('project_list.json', mode='w') as file:
            json.dump(project_list, file)

        self.destroy()



