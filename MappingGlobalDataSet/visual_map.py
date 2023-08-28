import pygal
from pygal.maps.world import World
# used to choose color to the map
from pygal.style import RotateStyle as RS
# used to change color theme to printing
#changes the overall theme of the chart, including the background and labels as well
# as the individual country colors
from pygal.style import LightColorizedStyle as LCS

def draw_population(countries, populations):
    hist = pygal.Bar() 
    hist._title = "Population in the world"
    hist.x_labels = countries
    hist._x_title = "countries" 
    hist.y_labels = populations
    hist.add("Population", populations)
    hist.render_to_file("population.svg")

# build the world map 
def build_world_map(dict_data):
    # take an RGB color for map
    #  wm_style = RotateStyle('#996633')
    # set style and background color
    wm_style = RS('#996633',base_style=LCS )

    # set color for map

    wm = World(style=wm_style)
    wm.title  = "The population map"
    wm.add("Less than 10 millions people",dict_data["dict1"]) 
    wm.add("Less than 1 billions people",dict_data["dict2"]) 
    wm.add("More than 1 billions people",dict_data["dict3"]) 

    wm.render_to_file("world_population.svg")
# build the world map to showing the population of three countries
def build_american_map():
    wm = World()
    wm.title  = "North, Central , and South America"
    wm.add("North American", {"ca":32000000, "mx" : 309349000, "us":113423000, 'vn':90000000})
    wm.render_to_file("american_population.svg")
