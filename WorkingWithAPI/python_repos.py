import requests
import json
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# make an API call and store the response

def visual_data(names, starts):
    my_style = LS("#996633", base_style= LCS)
    chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
    chart._title = "Top Repositories"
    chart.x_labels = names
    chart.add("", starts )
    chart.render_to_file("top_repositories.svg")

relative_path = "DataVisualization/WorkingWithAPI/ProApiResponse/response_api.json"
url = 'http://api.github.com/search/repositories?q=language:python&sort=stars'
# make the call  and  store the response object in the variable r

# r = requests.get(url)

# The response object has an attribute called status_code
# if status_code is 200 the call is successful

#print("Status code:" , r.status_code)

# store api response in a  variable 
# convert the information to a python dictionary

# response_dict = r.json()
with open(relative_path, 'r') as fobj:
    response_dict = json.load( fobj)
print(type(response_dict))
# print the total number of projects
print("Total count : " ,response_dict['total_count'])
print("incomplete : " , response_dict['incomplete_results'])
# explore information about the repositories 
print("Repositories returns : " ,len(response_dict['items']))
# examine the first repository
repo_dicts = response_dict['items']
repo_dict = repo_dicts[0]
for key in repo_dict.keys():
    print(key)
print(type(repo_dicts))
print("Name : ",repo_dict['name'])
# name of owner's project
print("Owner : ",repo_dict['owner']['login'])
print("Stars : ",repo_dict['stargazers_count'])
print("Repository : ",repo_dict['html_url'])
print("Created : ",repo_dict['created_at'])
print("Updated : ",repo_dict['updated_at'])
print("Description",repo_dict['description'])
print("==================================")

# Show the top repositories
print("---===The top repositories ==========")
for repo in repo_dicts:
    print("Name : ",repo_dict['name'])
    # name of owner's project
    print("Owner : ",repo['owner']['login'])
    print("Stars : ",repo['stargazers_count'])
    print("Repository : ",repo['html_url'])
    print("Created : ",repo['created_at'])
    print("Updated : ",repo['updated_at'])
    print("Description",repo['description'])
names, starts = [], []
for repo in repo_dicts:
    names.append(repo['name'])
    starts.append(repo['stargazers_count'])

visual_data(names, starts)