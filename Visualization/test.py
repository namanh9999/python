import matplotlib.pyplot as plt
from random_walk import RandomWalk
"""
# create a list contain values want to plot
x_values = list(range(1, 1000))
y_values = [value+2 for value in x_values ]

# set title , label and font 
plt.title("Plot Testing", c = "green",fontsize=10)
plt.xlabel("Discount", fontsize=10)
plt.ylabel("Valued", c = "red",fontsize=10)
plt.scatter(x_values, y_values, c = y_values,cmap=plt.cm.Reds, edgecolors= "none", s =10)
plt.tick_params(axis="both", labelsize=14)
# save the plot as a file 
plt.savefig("testGraph.png", bbox_inches='tight')
"""

rw = RandomWalk()
rw.fill_walk()
point_number = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c= point_number,cmap = plt.cm.Greens , s= 15)

# emphasize the last and first 
plt.scatter(0,0, c = "red", edgecolors="none",s = 100)
plt.scatter(rw.x_values[-1],rw.y_values[-1], c = "blue", edgecolors="none",s = 100)

plt.savefig("testGraph.png", bbox_inches='tight')
plt.show()