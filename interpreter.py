##################################################
## Takes data from source_file_2.json and returns all the projects
## associeted with a watcher
##################################################
## Author: {Marcos Pachêco}
## Credits: [{Marcos Pachêco}]
## Version: {1.0}
## Email: {marcos.hr.pacheco@gmail.com}
## Status: {non initiated}
##################################################

# Libs
import json

# Code

# Opens de file and dumps its contents into a well formatted string
with open("source_file_2.json") as f:
    json_data = json.load(f)

# Function for geting every project that a watcher is in
def watchers():
    # Makes a list with just the watchers
    watchers_list = list()
    for i in range(len(json_data)):

        watcher = json_data[i]['watchers']
        for j in range(len(watcher)):
            watchers_list.append(watcher[j])

    dic_geral = {}
    # Tests i wacther for every project
    for i in range(len(watchers_list)):
        projects_list = list()
        for j in range(len(json_data)):
            data_watcher = json_data[j]['watchers']

            # If finds will add to list based on priority value
            if watchers_list[i] in data_watcher:
                item = list()
                item.append(json_data[j]['name'])
                item.append(json_data[j]['priority'])
                projects_list.append(item)
        projects_list.sort(key=lambda item: item[1])

        # Deletes priority value as it is useless now
        for k in range(len(projects_list)):
            del projects_list[k][1]
            projects_list[k] = projects_list[k][0]

        # Appends watcher i with list of projects hes in
        dic_geral.update({
            watchers_list[i]:  projects_list
        })
    return dic_geral

def managers():
    # Makes a list with just the managers
    managers_list = list()
    for i in range(len(json_data)):

        manager = json_data[i]['managers']
        for j in range(len(manager)):
            managers_list.append(manager[j])

    dic_geral = {}
    # Tests i manager for every project
    for i in range(len(managers_list)):
        projects_list = list()
        for j in range(len(json_data)):
            data_manager = json_data[j]['managers']

            # If finds will add to list based on priority value
            if managers_list[i] in data_manager:
                item = list()
                item.append(json_data[j]['name'])
                item.append(json_data[j]['priority'])
                projects_list.append(item)
        projects_list.sort(key=lambda item: item[1])

        # Deletes priority value as it is useless now
        for k in range(len(projects_list)):
            del projects_list[k][1]
            projects_list[k] = projects_list[k][0]

        # Appends watcher i with list of projects hes in
        dic_geral.update({
            managers_list[i]:  projects_list
        })
    return dic_geral

# Writes file watchers.json
result = watchers()
with open('watchers.json', 'w') as file:
    json.dump(result, file, indent=2)

# Writes file watchers.json
result = managers()
with open('managers.json', 'w') as file:
    json.dump(result, file, indent=2)