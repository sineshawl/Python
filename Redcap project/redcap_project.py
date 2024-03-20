import json, requests


url = 'https://redcapsvr2.ahri.gov.et/api/'
def project_name(my_tokens):
    my_dic = {}

    with open('api_keys_label.json', mode='r') as file:
        my_dic = json.load(file)
    #! This code is from redcap Api: export project info
    with requests.Session() as session:
        for project in my_tokens.keys():
            print(project)
            token = my_tokens[project]
            data = {
            'token': token,
            'content': 'project',
            'format': 'json',
            'returnFormat': 'json'
            }
            r =session.post(url,data = data).json()
            project_title = r['project_title']
            print(token)
            if my_dic[project] != None:
                 if project_title not in my_dic[project]: 
                    my_dic[project].append(project_title)
            else:
                my_dic[project] = [project_title]
    with open('api_keys_label.json', mode='w') as file:
        json.dump(my_dic, file)




