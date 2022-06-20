# # access the weather data file and store it in a list
#
# # with open("weather-data.csv") as data:
# #     weather_data = data.readlines()
# #
# # print(weather_data)
#
# # Access using csv module
# # import csv
#
# # with open("weather-data.csv") as data:
# #     weather_data = csv.reader(data)
# #     temperature = []
# #     for row in list(weather_data)[1:]:
# #         temperature.append(int(row[1]))
# #
# #     print(temperature)
#
# # more easy to analyse data using panda module
#
# import pandas
#
# data = pandas.read_csv("weather-data.csv")
#
# data_dict = data.to_dict()
# print(data_dict) # DataFrame object
#
# temp_list = data["temp"].to_list()
# average_temperature = sum(temp_list)/len(temp_list)
# print(f"{average_temperature:.2f}")
#
# # using pandas computational methods
#
# # print(data["temp"].mean())
#
# # find out maximum temperature using pandas series
#
# # print(data["temp"].max())
#
# # get data columns
# # print(data["condition"])
# # print(data.condition) # here we can use columns as an attribute to access the columns
#
# # Get data in row
# # print(data[data.day == "Monday"])
#
# # get the data that has maximum temperature
# # print(data[data.temp == data.temp.max()])
#
# # get the specific row data and manipulate the data
#
# # monday = data[data.day == "Monday"]
# # # get the monday temperature in fahrenheit
# # fahrenheit = (monday.temp * 9/5) + 32
# # print(fahrenheit)
#
# # create a dataframe from scratch
#
# data_dict = {
#     "students": ["Ashish", "Tazin", "Onkar", "Renu"],
#     "scores" : [56, 85, 86, 90]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


import pandas

squirrel_color = {"Colors": ["Gray", "Black", "Cinnamon"], "Count": []}

squirrel_data = pandas.read_csv("Central-Park-Squirrel-Census-Squirrel-Data.csv")
gray_count = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"].count()
black_count = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"].count()
cinnamon_count = squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"].count()
squirrel_color["Count"].append(gray_count["Primary Fur Color"])
squirrel_color["Count"].append(black_count["Primary Fur Color"])
squirrel_color["Count"].append(cinnamon_count["Primary Fur Color"])


data = pandas.DataFrame(squirrel_color)
data.to_csv("squirrel_data.csv")
