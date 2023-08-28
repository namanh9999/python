import pygal

from die import Die

die1 = Die(8)
die2 = Die(8)

result = []
for i in range(50000):  
    value = die1.roll() + die2.roll()
    result.append(value)

frequencies = []
max_value = die1.number_sides + die2.number_sides
for value in range(2,max_value + 1):
    frequency = result.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Result of rolling two D8 dice 1000 "
hist.x_title = "Result"
hist.x_labels =['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.y_title= "Frequency of Result"

hist.add("D8 + D8" , frequencies)
hist.render_to_file("d8.svg")

