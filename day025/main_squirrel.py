import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

fur_color_dict = {'fur color': [], 'count': []}
for d in data['Primary Fur Color']:
    if pd.notna(d):
        if d not in fur_color_dict['fur color']:
            fur_color_dict['fur color'].append(d)
        index = fur_color_dict['fur color'].index(d)
        if len(fur_color_dict['count']) == index:
            fur_color_dict['count'].append(1)
        else:
            fur_color_dict['count'][index] += 1

new_data = pd.DataFrame(fur_color_dict)
new_data.to_csv('color_data.csv')
