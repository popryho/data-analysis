from datetime import datetime

import pandas as pd

data = pd.read_json(r'output.json')
fields = ['title', 'link', 'summary', 'published']


def string_to_date(x):
    if x is None:
        return None
    if len(x) == 31:
        return datetime.strptime(x, '%a, %d %b %Y %H:%M:%S %z')
    if len(x) == 20:
        return datetime.strptime(x, '%Y-%m-%dT%H:%M:%SZ')
    if len(x) == 25:
        return datetime.strptime(x, '%Y-%m-%dT%H:%M:%S%z')


data['published'] = data['published'].apply(string_to_date)

print(data['published'])
with open("output_task2.json", 'w') as outfile:
    data[fields].to_json(outfile, orient="records")

print(data[fields])
