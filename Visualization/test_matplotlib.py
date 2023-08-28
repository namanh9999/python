
import matplotlib.pyplot as plt
# use line to represent for data
input_value = [1,2,3,4,5,6]
squares = [1, 2, 5, 9, 3, 25]

plt.plot(input_value,squares, linewidth= 5)
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize= 14)
plt.ylabel("Square of values", fontsize= 14)

# set size of tick labels 
plt.tick_params(axis='both', labelsize=14)
plt.show()


