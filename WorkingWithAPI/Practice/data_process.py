def get_infor(data):
    starts, names = [],[]
    values = []
    repo_dicts = data["items"]
    print(type(repo_dicts))
    for value in repo_dicts:
        print("type of repo_dicts, ", type(value))
        name = value["name"]
        names.append(name)
        start = value["stargazers_count"]
        starts.append(start)
    values.append(names) 
    values.append(starts) 
    return values
def get_data_description(data):
    names, plot_dicts = [],[]
    values = []
    repo_dicts = data["items"]
    print(type(repo_dicts))
    for value in repo_dicts:
        print("type of repo_dicts, ", type(value))
        name = value["name"]
        names.append(name)
        plot_dict = {
            'value' :value["stargazers_count"],
            'label' :value["description"],
            # adding clickable links to our graph
            'xlink' : value["html_url"]

        }
        plot_dicts.append(plot_dict)
    values.append(names) 
    values.append(plot_dicts) 
    return values