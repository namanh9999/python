import pygal
import csv 

from matplotlib import pyplot as plt
from datetime import datetime

def  draw_pyplot(highs, date):
    fig = plt.figure(dpi= 128, figsize=(10,6))
    plt.plot(date, highs, c="red")
    plt.title("Daily high temperatures, July 2014", fontsize= 14)
    plt.xlabel('', fontsize=10)
    # draw the date labels diagonally 
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize=10)
    plt.tick_params(axis="both", which="major", labelsize = 16)
    plt.show()

def  draw_chart(highs, dates):
    print(highs)
    frequencies = []
    for i in range(100):
        frequency = highs.count(i)
        if frequency != 0:
            frequencies.append(frequency)
        frequencies.sort()
    print("Frequency :")
    print(frequencies)
    hist = pygal.Bar()
    hist._title = "max temperature in January 5 2014"
    label = set(highs)
    print("label : ")
    print(label)
    hist.x_labels = dates
    hist.x_title = "Values"
    hist.y_title = "Frequency"
    hist.y_labels = label
    hist.add("Temperature", highs)
    hist.render_to_file("temperature.svg")

file_name = "Project/DataVisualization/DownloadData/sitka_weather_07-2021_simple.csv"

try:
    dates = []
    highs = []
    with open(file_name, mode="r") as fobj:
        reader = csv.reader(fobj)
        header_row = next(reader)

        # use enumerate to get the index of each item , as well as the value
        for index, column_header in enumerate(header_row):
            print(index, column_header)

        for row in reader:
            # convert string to datetime format
            date= datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(date)
            highs.append(int(row[4]))
        print(highs)
        print(dates)
    draw_chart(highs, dates)
    draw_pyplot(highs, dates)
except:
    print("Error")
