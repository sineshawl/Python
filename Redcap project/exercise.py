import json
import customtkinter as ctk

project_list = {}

with open('project_list.json', mode='r') as file:
    project_list = json.load(file)

for category in project_list.keys():
    for inner_dict in project_list[category]:        
        for key in inner_dict.keys():
            for values in inner_dict[key]:
                print(f'{key}: {values}')

add_popup = ctk.CTkInputDialog(text='Enter Category Name', title='Add new Category')
