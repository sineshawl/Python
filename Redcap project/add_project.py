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
        self.label1.place(relx=.4, rely=.4, relwidth=.2, relheight=.2)

        self.exit_icon = Image.open('Images/exit.png').resize((20, 20))
        self.exit_image = ctk.CTkImage(self.exit_icon)

        self.btn_exit = ctk.CTkButton(self.frame1, text=None,width=20, fg_color="transparent", image=self.exit_image, command=lambda:self.destroy())
        self.btn_exit.place(relx=.93, rely=.01, relwidth=.07, relheight=.5)


        self.frame2 = ctk.CTkFrame(self)
        self.frame2.place(relx=0.02, rely=0.22, relwidth=0.96, relheight=0.76)


        self.frame2.columnconfigure((0,1), weight=1)
        self.frame2.rowconfigure((0, 1, 2, 3), weight=1)
        


        self.option_data_type = ctk.CTkOptionMenu(self.frame2, values=['Select Data Type','Layout', 'Raw Data(Machine Result)'], command=self.on_select_data_type) 
        self.option_data_type.grid(row = 0, column=0, columnspan=2)

        self.label2 = ctk.CTkLabel(self.frame2, text='Spreadsheet URL')

        self.entry_spread_url = ctk.CTkEntry(self.frame2)

        self.label3 = ctk.CTkLabel(self.frame2, text='Folder ID')

        self.entry_folder_id = ctk.CTkEntry(self.frame2)

        self.label4 = ctk.CTkLabel(self.frame2, text='REDCap API')

        self.entry_redcap_api = ctk.CTkEntry(self.frame2)

        self.btn_save = ctk.CTkButton(self.frame2, text='Save', command=self.save_project)

    def on_select_data_type(self, choice):
        if choice == 'Layout':
            self.label2.grid(row=1, column=0, sticky='ew')
            self.entry_spread_url.grid(row=1, column=1, sticky='ew')
            self.label4.grid(row=2, column=0, sticky='ew')
            self.entry_redcap_api.grid(row=2, column=1, sticky='ew')        
            self.btn_save.grid(row=3, column=1)

            self.entry_redcap_api.configure(placeholder_text='')

            self.entry_folder_id.grid_forget()
            self.label3.grid_forget()
        elif choice == 'Raw Data(Machine Result)':
            self.label3.grid(row=1, column=0, sticky='ew')
            self.entry_folder_id.grid(row=1, column=1, sticky='ew')
            self.label4.grid(row=2, column=0, sticky='ew')
            self.entry_redcap_api.grid(row=2, column=1, sticky='ew')        
            self.btn_save.grid(row=3, column=1)
            self.entry_redcap_api.configure(placeholder_text='')


            self.label2.grid_forget()
            self.entry_spread_url.grid_forget()
    def save_project(self):
        my_dic = {}  
        my_api_token = {}      
        with open('project_list.json', mode='r') as file:
            my_dic = json.load(file)
        with open('api_keys.json' , mode='r') as file:
            my_api_token = json.load(file)
        

        if self.option_data_type.get() == 'Layout':
            if self.entry_spread_url.get() == '' or self.entry_spread_url.get() =='URL required' or self.entry_redcap_api.get() == '' or self.entry_folder_id.get() == 'API required':
                if self.entry_spread_url.get() == '':
                    self.entry_spread_url.configure(placeholder_text='URL required', placeholder_text_color='red')
                if self.entry_redcap_api.get() == '':
                    self.entry_redcap_api.configure(placeholder_text='API required', placeholder_text_color='red')
            elif len(self.entry_redcap_api.get()) != 32:
                self.entry_redcap_api.delete(0, ctk.END)
                self.entry_redcap_api.insert(0, 'API length should be 32')
                self.entry_redcap_api.configure(text_color='red')

            else:
                print(len(self.entry_redcap_api.get()))
                spreadsheet_url =self.entry_spread_url.get()
                redcap_api = self.entry_redcap_api.get()

                dic1 = {}
                dic2 = {}

                dic1['spreadsheet url'] = [spreadsheet_url]
                dic2['redcap api layout'] = [redcap_api]
                if self.key in my_dic and my_dic[self.key] != None:
                     if 'spreadsheet url' in my_dic[self.key][0]:
                        my_dic[self.key][0]['spreadsheet url'].append(spreadsheet_url)
                     if 'redcap api layout' in my_dic[self.key][1]:
                         my_dic[self.key][1]['redcap api layout'].append(redcap_api)

                     if self.key in my_api_token:
                         my_api_token[self.key].append(redcap_api)
                     else:
                         my_api_token[self.key] = [redcap_api]
                else:
                    my_dic[self.key] = [dic1, dic2]
                    my_api_token[self.key] = [redcap_api]

                with open('project_list.json', mode='w') as file:
                    json.dump(my_dic, file)
                with open('api_keys.json', mode='w') as file:
                    json.dump(my_api_token, file)
                    project_name({self.key:redcap_api})

        elif self.option_data_type.get() == 'Raw Data(Machine Result)':
            
            if self.entry_folder_id.get() == '' or self.entry_folder_id.get() == 'folder id required' or self.entry_redcap_api.get() == '' or self.entry_folder_id.get() == 'API required':
                if self.entry_folder_id.get() == '':
                    self.entry_folder_id.configure(placeholder_text='folder id required', placeholder_text_color='red')
                if self.entry_redcap_api.get() == '':
                    self.entry_redcap_api.configure(placeholder_text='API required', placeholder_text_color='red')
            elif len(self.entry_redcap_api.get()) != 32:
                self.entry_redcap_api.delete(0, ctk.END)
                self.entry_redcap_api.insert(0, 'API length should be 32')
                self.entry_redcap_api.configure(text_color='red')
            else:
                folder_id =self.entry_folder_id.get()
                redcap_api = self.entry_redcap_api.get()
                dic1 = {}
                dic2 = {}

                dic1['folder id'] = [folder_id]
                dic2['redcap api raw'] = [redcap_api]
                if self.key in my_dic and my_dic[self.key] != None:
                     if 'folder id' in my_dic[self.key][2]:
                        my_dic[self.key][2]['folder id'].append(folder_id)
                     if 'redcap api raw' in my_dic[self.key][3]:
                         my_dic[self.key][3]['redcap api raw'].append(redcap_api)
                     
                     if self.key in my_api_token:   # creating api dictionary to write into api_keys.json
                         my_api_token[self.key].append(redcap_api)                      
                     else:
                         my_api_token[self.key] = redcap_api
                else:
                    my_dic[self.key] = [dic1, dic2]   
                    my_api_token[self.key]=redcap_api   
         
                with open('project_list.json', mode='w') as file:
                    json.dump(my_dic, file)
                with open('api_keys.json', mode='w') as file:
                    json.dump(my_api_token, file)
                    project_name({self.key:redcap_api})
 


   



