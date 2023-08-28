import get_data
import file_process
from visual_map import build_world_map
data = file_process.get_file()
print(len(data))
countries = get_data.get_countries_name(data)
print(countries)
populations = get_data.get_2010_population(data,countries)
print(len(populations))
dict_data =  get_data.make_dict_from_data(countries, populations)
print(dict_data)
dict_data_code_population = get_data.make_dict_countryCode_populations(countries)

build_world_map(dict_data_code_population)