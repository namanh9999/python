import pygal
import matplotlib.pyplot as plt
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


def visual_chart(data):
    # create instance my_config
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
    hist._title = "The names and stars of several java projects"
    hist.x_labels = data[0]
    hist.y_title = "Starts"
    hist.add("Java Projects", data[1])
    hist.render_to_file("java_projects.svg")

def visual_plot(data):
    plt.xlabel("Project Name", c= "Green", fontsize=20)
    plt.xticks(rotation=45) 
    plt.ylabel("Start", c= "red", fontsize= 20)
    plt.title =("Java projects")
    plt.scatter(data[0], data[1],c=data[1] ,  cmap = plt.cm.Reds, edgecolors="none", s = 15)
    plt.tick_params(axis="both", which="major", labelsize = 14)
    plt.show()

