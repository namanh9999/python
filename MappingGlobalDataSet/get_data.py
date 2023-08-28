from pygal.maps.world import COUNTRIES
from file_process import get_file

def get_country_code(country_name):
    print(country_name)
    
    for country_code in sorted(COUNTRIES.keys()):
        if country_name == COUNTRIES[country_code]:
            return country_code
        elif country_name == "Vietnam":
            country_code = 'vn'
            return country_code
        else:
            pass

def get_countries_name(data):
    countries_name = []
    # get country name 
    for value in data:
        if value["Year"] == '2010':
            country_name = value["Country Name"]
            countries_name.append(country_name)
    return countries_name

def get_2010_population(data, countries_name):
    populations = []
    for value in data:
        for country_name in countries_name:
            if country_name == value["Country Name"] and value['Year'] == "2010":
                populations.append(value["Value"])
                print(country_name, value['Value'])
    return populations

def get_population ( country_name):
    data = get_file()
    for value in data:
        if value["Year"] == "2010" and value["Country Name"] == country_name:
            population = value['Value']
            return population

def make_dict_from_data(countries_name, populations):
    dict_data = {}
    i = 0
    while True:
        if i < len(countries_name):
            dict_data[countries_name[i]] = populations[i]
            i += 1
        else: 
            break    
    return dict_data

def make_dict_countryCode_populations(countries_name):
    dict_data = {}
    dict1 = {}
    dict3 = {}
    dict2 = {}
    for country in countries_name:
        country_code = get_country_code(country)
        population = int(float(get_population(country)))
        if country_code:
            if(population < 10000000):
                dict1[country_code]  = population
                dict_data["dict1"] = dict1
            elif(population < 1000000000):
                dict2[country_code]  = population
                dict_data["dict2"] = dict2
            else:
                dict3[country_code]  = population
                dict_data["dict3"] = dict3
    return dict_data

