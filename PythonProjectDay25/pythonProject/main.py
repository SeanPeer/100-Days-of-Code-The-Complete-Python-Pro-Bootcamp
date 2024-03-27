import pandas
import csv

# Watching CSV as a raw data
# with open("weather_data.csv","r") as file:
#     list_named_data = file.readlines()
#     print(list_named_data)

# Watching CSV using csv reader - and then print each line
# with open("weather_data.csv", 'r') as file:
#     data = csv.reader(file)
#     # Task fish just the tempratures form the file
#     temperature = []
#     for line in data:
#         if line[1] != "temp":
#             temperature.append(int(line[1]))
#     print(temperature)
#

data = pandas.read_csv("weather_data.csv")
print(data['temp'])
