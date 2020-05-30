import json
import os

p = os.path.dirname(os.path.abspath(__file__))
print(p)

schema = {}



for i in range(10):
    temp_schema = {'url':'','description':''}
    schema[i]=temp_schema
    schema[i]['url'] = input('URL -> ')
    schema[i]['description'] = input('Description -> ')

with open('config.json', "w", encoding='utf8') as out_file:
    data = json.dump(schema, out_file, indent=4)
