# using individual  points with scatter()
import matplotlib.pyplot as plt

"""
# s = size of the dot
plt.scatter(1,3, s= 200)
plt.title("Scatter graphics")
plt.xlabel("Value ", fontsize=12)
plt.ylabel("Month", fontsize=12)
# set size of tick labels 
plt.tick_params(axis='both', which="major", labelsize = 14)
plt.show()
"""
# plotting a series of points with scatter()

x_values = [value for value in range(0, 2000, 2)]
y_values = [y**2 for y in x_values]
# edge color is a argument to show outlines from data points 
# removing outlines form data points
# plt.scatter(x_values, y_values, edgecolor="none", s = 10)

# use c parameter to change the color of the points , pass c to scatter()
# example: c = "red"
# you can also customize using the RGB color model, using decimal values between 0 to 1
# example: c = (0,0,0.8) 

# plt.scatter(x_values, y_values, c="red", edgecolors="none", s = 10)

# Using a colormap
# c= ...  is a list of values you want to assign , cmap is a color map used to 
plt.scatter(x_values, y_values, c=y_values, cmap = plt.cm.Reds ,edgecolors="none", s = 10)

plt.title("Scatter graphics")
plt.xlabel("Value ", fontsize=12, c= "red")
plt.ylabel("Month", fontsize=12)
# set size of tick labels 
plt.tick_params(axis='both', which="major", labelsize = 14)
# set the range for each axis 
plt.axis([0,1100, 0, 1100000])

# if  you wanna to save the plot to a file , you can replace the call show() with a call to 
# plt.savefig()
# the first argument is the filename , the second argument is the trims extra whitespace from the plot
plt.savefig("0_1000.png", bbox_inches="tight")
plt.show()