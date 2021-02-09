import pandas as pd

data = pd.read_json(r'output.json')
# necessary columns
fields = ['title', 'link', 'summary', 'published']

# apply to_datetime function along published axis in data dataframe
data['published'] = pd.to_datetime(data['published'])

# output the result on all entries on necessary columns to output_task2.json file
with open("output_task2.json", 'w') as outfile:
    data[fields].to_json(outfile, orient="records")

print(data[fields])
