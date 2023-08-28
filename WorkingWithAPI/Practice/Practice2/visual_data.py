import pygal 
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS 

def visual_pygal(data):
    my_config = pygal.Config()
    # rotation and  show legend
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    # set font size for title, minor labels and major labels
    my_config.title_font_size = 24
    my_config.label_font_size = 18
    # the labels on the y_axis 
    my_config.major_label_font = 18
    # shorten the longer project names to 15 characters
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1000

    my_style = LS("#889900", base_style=LCS)
    hist = pygal.Bar(my_config, style=my_style)
    hist.x_labels = data[1]
    hist.add("", sorted(data[0]))
    
    hist.render_to_file("comment_visual.svg")

