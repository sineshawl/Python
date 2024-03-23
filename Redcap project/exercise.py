import json

my_projects = {}
with open('project_list.json', mode='r') as file:
    my_projects = json.load(file)

grouped_data = {}

for i in range(len(my_projects['redcap_folder_name'])):
    folder_name = my_projects['redcap_folder_name'][i]
    if folder_name not in grouped_data:
        grouped_data[folder_name] = {}
    for key, value in my_projects.items():
        grouped_data[folder_name][key] = grouped_data[folder_name].get(key, []) + [value[i]]
# print(grouped_data['ACHIDES'])

for outer_key in grouped_data.keys():
        for values in grouped_data[outer_key]['redcap_project_name']:
             print(values, 'end')
        print()



