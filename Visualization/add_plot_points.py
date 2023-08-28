import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk(50000)
rw.fill_walk()

# set size of figure to fit screen
plt.figure(figsize=(10,6))

# Get the current figure
fig = plt.gcf()
# Set the background color
fig.set_facecolor('lightgray')

point_numbers = list(range(rw.num_points))
number = len(point_numbers)
plt.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap= plt.cm.Reds, edgecolors="none", s = 11)

# dpi is the system's resolution
# plt.figure(dpi=128, figsize=(10, 6))
# remove axis from plot
plt.axis("off")

plt.show()
