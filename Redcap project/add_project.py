import customtkinter as ctk
import json

class add_project(ctk.CTkFrame):
    def __init__(self, key):
        super().__init__( key)

        self.key = key
        self.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=1.0)

        self.frame1 = ctk.CTkFrame(self)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.17)

       

        self.label1 = ctk.CTkLabel(self.frame1, text='Add Project', text_color='white')
        self.label1.place(relx=.4, rely=.4, relwidth=.2, relheight=.2)


        self.frame2 = ctk.CTkFrame(self)
        self.frame2.place(relx=0.02, rely=0.22, relwidth=0.96, relheight=0.76)


        self.frame2.columnconfigure((0,1), weight=1)
        self.frame2.rowconfigure((0, 1, 2, 3), weight=1)
        


        self.option_data_type = ctk.CTkOptionMenu(self.frame2, values=['Select Data Type','Layout', 'Raw Data(Machine Result)'], command=self.on_select_data_type) 
        self.option_data_type.grid(row = 0, column=0, columnspan=2)

        self.label2 = ctk.CTkLabel(self.frame2, text='Spreedsheet URL')

        self.entry_spreed_url = ctk.CTkEntry(self.frame2)

        self.label3 = ctk.CTkLabel(self.frame2, text='Folder ID')

        self.entry_folder_id = ctk.CTkEntry(self.frame2)

        self.label4 = ctk.CTkLabel(self.frame2, text='REDCap API')

        self.entry_redcap_api = ctk.CTkEntry(self.frame2)

        self.btn_save = ctk.CTkButton(self.frame2, text='Save', command=self.save_project)

    def on_select_data_type(self, choice):
        if choice == 'Layout':
            self.label2.grid(row=1, column=0, sticky='ew')
            self.entry_spreed_url.grid(row=1, column=1, sticky='ew')
            self.label4.grid(row=2, column=0, sticky='ew')
            self.entry_redcap_api.grid(row=2, column=1, sticky='ew')        
            self.btn_save.grid(row=3, column=1)

            self.entry_folder_id.grid_forget()
            self.label3.grid_forget()
        elif choice == 'Raw Data(Machine Result)':
            self.label3.grid(row=1, column=0, sticky='ew')
            self.entry_folder_id.grid(row=1, column=1, sticky='ew')
            self.label4.grid(row=2, column=0, sticky='ew')
            self.entry_redcap_api.grid(row=2, column=1, sticky='ew')        
            self.btn_save.grid(row=3, column=1)

            self.label2.grid_forget()
            self.entry_spreed_url.grid_forget()
    def save_project(self):
        
        # with open('project_list.json', mode='r') as file:
        #     project_list = json.load(file)

        if self.option_data_type.get() == 'Layout':
            if self.entry_spreed_url.get() == '':
                 self.entry_spreed_url.set('URL required')
            elif self.entry_redcap_api.get() == ' ':
                self.entry_redcap_api.set('API required')
            else:
                    print(self.key)

        elif self.option_data_type.get() == 'Raw Data(Machine Result)':
            if self.entry_folder_id.get() == '':
                 self.entry_folder_id.set('folder id required')
            elif self.entry_redcap_api.get() == '':
                self.entry_redcap_api.set('API required')



        



