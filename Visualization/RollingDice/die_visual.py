import pygal

from die import Die

die = Die()
die1 = Die(10)
# make some rolls , and store results in a list
results = []
for i in range(50000):
    side = die.roll() + die1.roll()
    results.append(side)

# analyze the results 
frequencies = []
max_result = die.number_sides + die1.number_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

sum = 0
for i in frequencies:
    sum += i
print("sum" + str(sum))
print(frequencies)

# visualize the results
# make a var chart by creating an instance of pygal.Bar()
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times"
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist._x_title = "Result"
hist._y_title = "Frequency of result"

# used to add a series of values to the chart
hist.add('D6 + D6', frequencies)
# render the chart to an svg file
hist.render_to_file("die_visual.svg")