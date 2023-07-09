import csv
import pandas

# method 1: without using csv library
with open('weather_data.csv') as weather_data:
    data = weather_data.readlines()

separated = []
for row in data:
    separated.append(row.strip().split(','))

print(separated)


# method 2: using csv library
with open('weather_data.csv') as weather_data:
    data = list(csv.reader(weather_data))

print(data)


# method 3: using pandas library
data = pandas.read_csv('weather_data.csv')
# print(data)
# print(type(data.iloc[1]))

# get a particular column
# print(data['temp'])
# print(data.temp)

# get average
average = sum(data['temp']) / data['temp'].size
print(average)
print(data['temp'].mean())

# get a particular row meeting the criteria
print(data[data.day == 'Monday'])
print(data[data['temp'] == data['temp'].max()])

# create a dataframe from dict
data_dict = {'student': ['Tom', 'Amy', 'Alice'], 'score': [90, 80, 88]}
data = pandas.DataFrame(data_dict)
print(data)