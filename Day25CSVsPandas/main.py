# with open("Day25CSVsPandas\weather_data.csv") as file:
#     data = file.readlines()

# import csv

# with open("Day25CSVsPandas\weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = [int(x[1]) for x in data if x[1] != 'temp']
#     print(temperatures)

import pandas as pd
data = pd.read_csv("Day25CSVsPandas/weather_data.csv")
list = data["temp"].tolist()
avg = sum(list)/len(list)
avg = data["temp"].mean()
maximum = data["temp"].max()
maximum = data.temp.max()

# Get Row Data: filter column by condition
data[data.temp == maximum]
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)

# Dataframe from stratch
data_dict = {
    "students": ["Amy", "James","Angela"],
    "scores":[76, 56, 65]
}
data = pd.DataFrame(data_dict)
data.to_csv("Day25CSVsPandas/new_data.csv")

grey_count, red_count, black_count = 0,0,0
squirrel_data = pd.read_csv("Day25CSVsPandas/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colors = squirrel_data["Primary Fur Color"]#.tolist()
# grey_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
# red_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
# black_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

squirrel_color_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count":[grey_count, red_count, black_count]
}

def count(color):
    # global squirrel_color_dict
    match color:
        case "Gray":
            squirrel_color_dict["Count"][0] += 1
        case "Cinnamon":
            squirrel_color_dict["Count"][1] += 1
        case "Black":
            squirrel_color_dict["Count"][2] += 1
        case _:
            pass

# map(lambda x: count(x), colors)
for color in colors:
    count(color)

squirrel_count = pd.DataFrame(squirrel_color_dict)
squirrel_count.to_csv("Day25CSVsPandas/squirrel_count.csv")


