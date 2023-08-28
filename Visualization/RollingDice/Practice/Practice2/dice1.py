import pygal

from random import randint


class Dice():
    def __init__(self, number_side=6):
        self.number_side = number_side

    def roll(self):
        return randint(1, self.number_side)


def get_value(time=100000):
    die = Dice()
    die1 = Dice()
    die2 = Dice()

    result = []
    for i in range(time):
        value = die.roll() + die1.roll() + die2.roll()
        result.append(value)

    max_amount = die.number_side + die1.number_side + die2.number_side
    frequencies = []
    for value in range(3, max_amount + 1):
        frequency = result.count(value)
        frequencies.append(frequency)
    return frequencies


def draw(frequencies):

    hist = pygal.Bar()
    hist.title = "Result rolling three dices D6"
    hist.x_labels = ['3', '4', '5', '6', '7', '8', '9',
                     '10', '11', '12', '13', '14', '15', '16', '17', '18']
    hist.x_title = "Result"
    hist.y_title = "Frequency of each result"

    hist.add("D6* D6 * D6", frequencies)
    hist.render_to_file("D6x3.svg")