import customtkinter as ctk
from redcap_project import project_name
import json
from PIL import Image
class add_project(ctk.CTkFrame):
    def __init__(self, master, key):
        super().__init__(master)
        self.key = key
        self.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=1.0)

        self.frame1 = ctk.CTkFrame(self)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.17)

       

        self.label1 = ctk.CTkLabel(self.frame1, text='Add Project', text_color='white')
        self.label1.pack(padx=10, pady=10, expand=True)

        self.exit_icon = Image.open('Images/exit.png').resize((20, 20))
        self.exit_image = ctk.CTkImage(self.exit_icon)

        self.btn_exit = ctk.CTkButton(self.frame1, text=None,width=20, fg_color="transparent", image=self.exit_image, command=lambda:self.destroy())
        self.btn_exit.place(relx=.93, rely=.01, relwidth=.07, relheight=.5)

        self.frame2 = ctk.CTkFrame(self)
        self.frame2.place(relx=0.02, rely=0.22, relwidth=0.96, relheight=0.76)

        self.frame2.columnconfigure((0,1), weight=1)
        self.frame2.rowconfigure((0, 1, 2, 3, 4,5,6), weight=1)
       
        self.label_redcap_folder = ctk.CTkLabel(self.frame2, text='REDCap Folder Name')
        self.label_redcap_folder.grid(row=0, column=0, ipadx=10, sticky='we')

        self.entry_redcap_folder = ctk.CTkEntry(self.frame2, placeholder_text=key)
        self.entry_redcap_folder.grid(row=0, column=1, sticky='we')

        self.label_redcap_project = ctk.CTkLabel(self.frame2, text='REDCap Project Name')
        self.label_redcap_project.grid(row=1, column=0)

        self.entry_redcap_project = ctk.CTkEntry(self.frame2)
        self.entry_redcap_project.grid(row=1, column=1, sticky='we')

        self.label_redcap_api = ctk.CTkLabel(self.frame2, text='REDCap API')
        self.label_redcap_api.grid(row=2, column=0)

        self.entry_redcap_api = ctk.CTkEntry(self.frame2)
        self.entry_redcap_api.grid(row=2, column=1, sticky='we')

        self.option_data_type = ctk.CTkOptionMenu(self.frame2, values=['Select Data Structure','Layout', 'Antigen', 'Antibody', 'qPCR', 'Digital'], command=self.on_select_data_type) 
        self.option_data_type.grid(row = 3, column=0)

        self.label_spreadsheet_url = ctk.CTkLabel(self.frame2, text='Google Spreadsheet URL')

        self.entry_spreadsheet_url = ctk.CTkEntry(self.frame2)

        self.label_google_drive_id = ctk.CTkLabel(self.frame2, text='Google Drive ID')

        self.entry_google_drive_id = ctk.CTkEntry(self.frame2)

        self.btn_save = ctk.CTkButton(self.frame2, text='Save', command=self.save_project)

    def on_select_data_type(self, choice):
        if choice == 'Layout':
            self.label_spreadsheet_url.grid(row=4, column=0, sticky='ew')
            self.entry_spreadsheet_url.grid(row=4, column=1, sticky='ew')
            self.btn_save.grid(row=5, column=1)

            # self.entry_redcap_api.configure(placeholder_text='')
            self.label_google_drive_id.grid_forget()
            self.entry_google_drive_id.grid_forget()
        elif choice != 'Layout' and choice != 'Select Data Structure':
            self.label_google_drive_id.grid(row=4, column=0, sticky='ew')
            self.entry_google_drive_id.grid(row=4, column=1, sticky='ew')
            self.btn_save.grid(row=5, column=1)

            self.label_spreadsheet_url.grid_forget()
            self.entry_spreadsheet_url.grid_forget()
    def save_project(self):

        redcap_folder = self.entry_redcap_folder.get()
        redcap_project_name = self.entry_redcap_project.get()
        redcap_api = self.entry_redcap_api.get()
        spreadsheet_url = self.entry_spreadsheet_url.get()
        google_drive_id = self.entry_google_drive_id.get()
        structure_of_data =self.option_data_type.get() 

        project_list = {}  
        with open('project_list.json', mode='r') as file:
            project_list = json.load(file)
        
        # check if the form is blank
        if redcap_folder == '' or redcap_project_name == '' or redcap_api == '':
            if redcap_folder == '':
                self.entry_redcap_folder.configure(placeholder_text='REDCap folder name required', placeholder_text_color='red')
            if redcap_project_name == '':
                self.entry_redcap_project.configure(placeholder_text='REDCap project name required', placeholder_text_color='red')
            if redcap_api == '':
                self.entry_redcap_api.configure(placeholder_text='REDCap API name required', placeholder_text_color='red')
 
        elif self.option_data_type.get() == 'Layout':
            if spreadsheet_url == '' :
                self.entry_spreadsheet_url.configure(placeholder_text='Spreadsheet URL required', placeholder_text_color='red')
            # elif len(self.entry_redcap_api.get()) != 32:
            #     self.entry_redcap_api.delete(0, ctk.END)
            #     self.entry_redcap_api.insert(0, 'API length should be 32')
            #     self.entry_redcap_api.configure(text_color='red')
            else: 
                project_list['project_id'].append(len(project_list['project_id'])+1)           
                project_list['redcap_folder_name'].append(redcap_folder)
                project_list['redcap_project_name'].append(redcap_project_name)
                project_list['redcap_api'].append(redcap_api)
                project_list['structure_of_data'].append(structure_of_data)
                project_list['spreadsheet_url'].append(spreadsheet_url)
                project_list['google_drive_id'].append('None')

                with open('project_list.json', mode='w') as file:
                    json.dump(project_list, file)
                # project_name({self.key:redcap_api})

        elif structure_of_data != 'Layout':
            
            if google_drive_id == '':
                self.entry_folder_id.configure(placeholder_text='folder id required', placeholder_text_color='red')
            else:
                project_list['project_id'].append(len(project_list['project_id'])+1)           
                project_list['redcap_folder_name'].append(redcap_folder)
                project_list['redcap_project_name'].append(redcap_project_name)
                project_list['redcap_api'].append(redcap_api)
                project_list['structure_of_data'].append(structure_of_data)
                project_list['spreadsheet_url'].append('None')
                project_list['google_drive_id'].append(google_drive_id)
         
                with open('project_list.json', mode='w') as file:
                    json.dump(project_list, file)
                    # project_name({self.key:redcap_api})
 


   



