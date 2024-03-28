import pandas
# import csv
#
# # Watching CSV as a raw data
# # with open("weather_data.csv","r") as file:
# #     list_named_data = file.readlines()
# #     print(list_named_data)
#
# # Watching CSV using csv reader - and then print each line
# # with open("weather_data.csv", 'r') as file:
# #     data = csv.reader(file)
# #     # Task fish just the tempratures form the file
# #     temperature = []
# #     for line in data:
# #         if line[1] != "temp":
# #             temperature.append(int(line[1]))
# #     print(temperature)
# #
#
# Reading csvs file is easier and more clear with pandas
data = pandas.read_csv("weather_data.csv")
print(data['temp'])

# Converting data to dictionary
data_dict = data['temp'].to_dict()
print(data_dict)

# CSV can be converted to list using pandas
data_list = data['temp'].to_list()
print(data_list)

# Challenge - Calculate and print the average temperature
teta = len(data_list)
summ = 0
for t in data_list:
    summ += t
aver = summ / teta

print(aver)
# Can be possible without any calculation by my side with just using mean
mean = data['temp'].mean()
print(mean)

# Same as getting max
max = data['temp'].max()
print(max)

# Pulling data from monday raw
data_day = data[data.day == "Monday"]
print(data_day)


print(data[data.temp == data.temp.max()])