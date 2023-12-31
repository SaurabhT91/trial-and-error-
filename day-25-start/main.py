# with open("weather_data.csv") as data_file:
#    data = data_file.readlines()
#    print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
#     print(temperatures)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data['temp'])

import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(data)
print(type(data["temp"]))
print(data["temp"])

data_dict = data.to_dict()
temp_list = data["temp"].to_list()

print(data_dict)
print(temp_list)

mean = data["temp"].mean()
average = sum(temp_list) / len(temp_list)
print(average)
print(mean)
print(data["temp"].max())
print(data["temp"].min())

print(data["condition"])
print(data.condition)
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
monday_temp = monday.temp[0]
monday_temp_f = monday_temp * 9/5 + 32

print(monday_temp_f)

#create a dataframe from scratch

data_dict = {
    "students": ["amy", "james", "angela"],
    "scores": [76,56,65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")














