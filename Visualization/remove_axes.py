import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

point_number = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c = point_number,
            cmap= plt.cm.Greens, edgecolors="none" ,s= 10) 
plt.scatter(0, 0, c = "red", s = 100)
plt.scatter(rw.x_values[-1], rw.y_values[-1],  c = "Blue", s = 100)

# Remove the axes.
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()