import matplotlib.pyplot as plt

import dice1
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()
point_number = list(range(rw.number_points))
plt.scatter(rw.x_value, rw.y_value, c = point_number, cmap = plt.cm.Blues, s = 12, edgecolors="none")
plt.scatter(0,0 , c = "Red", s = 17)
plt.scatter(rw.x_value[-1], rw.y_value[-1], c = "Yellow", s = 17)
plt.savefig("randomwalk.png", bbox_inches = "tight")
plt.axis("off")

dice = dice1.get_value()
dice1.draw(dice)
plt.show()
