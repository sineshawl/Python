import json

my_projects = {}
with open('project_list.json', mode='r') as file:
    my_projects = json.load(file)

filtered_data = {}

print(my_projects['project_id'][2])

# print(filtered_data)

print(my_projects['project_id'][2])

