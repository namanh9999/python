import pygal

from dice import Dice

die = Dice()
die2 = Dice()
die3 = Dice()

result = []
for i in range(1000):
    value = die.roll() + die2.roll() + die3.roll()
    result.append(value)

frequencies = []
max_amount = die.number_sides  + die2.number_sides + die3.number_sides
for i in range(3, max_amount+ 1):
    frequency = result.count(i)
    frequencies.append(frequency)
print(frequencies)

sum = 0
for i in frequencies:
    sum += i
print("sum :" + str(sum))

hist = pygal.Bar()
hist.title = "Result of rolling three dices"
hist.x_title = "Result"
hist.x_labels = ['3', '4', '5', '6','7', '8','9','10','11','12','13','14','15','16','17','18']
hist.y_title = "Frequency of result"

hist.add('D6+D6+D6', frequencies)
hist.render_to_file("practice.svg")