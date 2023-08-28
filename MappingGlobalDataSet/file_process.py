import json
# used to get two-letter  of the country 
relative_path = "DataVisualization/MappingGlobalDataSet/population_data.json"
def get_file():
    try:
        with open(relative_path, 'r') as fobj:
            data = json.load(fobj)
            return data
    except FileNotFoundError:
        print("File not found")
