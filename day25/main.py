import pandas

# data = pandas.read_csv("weather_data.csv")

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)


# print((monday_temp*(9/5)) + 32)

data = pandas.read_csv("Squirrel_Data.csv")
primary_color = data["Primary Fur Color"]
red = 0
grey = 0
black = 0
for color in primary_color:
    if color == "Cinnamon":
        red += 1
    elif color == "Gray":
        grey += 1
    elif color == "Black":
        black += 1

color_data ={
    "Color": ["grey", "red", "black"],
    "Count" : [red, grey, black]
}

new_data = pandas.DataFrame(color_data)
new_data.to_csv("squirrel_count.csv")