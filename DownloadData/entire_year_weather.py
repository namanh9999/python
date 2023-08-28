import csv
import pygal
import matplotlib.pyplot as plt
from datetime import datetime


def draw_pyplot(data_high, data_low, dates):
    
    fig = plt.figure(dpi=128, figsize=(10, 16))
    plt.plot(dates, data_high, c= "Green")
    plt.plot(dates, data_low, c= "Red")
    plt.title(" Entire Year's 2021 Weather")
    plt.xlabel("Date Time", fontsize=10, c = "red")
    fig.autofmt_xdate()
    plt.ylabel("Temperature", fontsize=10, c= "orange")
    plt.tick_params(axis="both", which = "major", labelsize = 10)
    plt.show()
file_name = "Project/DataVisualization/DownloadData/weather_data/sitka_weather_2021_full.csv"
with open(file_name, 'r') as fobj:
        reader = csv.reader(fobj)
        header_row = next(reader)
        for index, value in enumerate(header_row):
            print(str(index) + " : " + str(value))
        data_high = []
        data_low = []
        dates = []
        for row in reader:
            dates.append(datetime.strptime(row[2], '%Y-%m-%d'))
            data_high.append(int(row[7]))
            data_low.append(int(row[8]))
        print(data_high)
draw_pyplot(data_high, data_low, dates)
