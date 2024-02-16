import json, requests

js_data= None

with open('api_keys.json', mode='r') as file:
    js_data=json.load(file)


url = 'https://redcapsvr2.ahri.gov.et/api/'
def project_name(my_tokens):
    my_dic = dict()
    #! This code is from redcap Api: export project info
    with requests.Session() as session:
        for project in my_tokens.keys():
            project_list = []
            for token in my_tokens[project]: 
                data = {
                'token': token,
                'content': 'project',
                'format': 'json',
                'returnFormat': 'json'
                }
                r =session.post(url,data = data).json()
                project_list.append(r['project_title'])
                my_dic[project]=project_list
    return my_dic


project_list = {}

project_list = project_name(js_data)

with open('api_keys_label.json', mode='w') as file:
    json.dump(project_list, file)