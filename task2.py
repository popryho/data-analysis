import pandas as pd

data = pd.read_json(r'output_task1.json')
# necessary columns
fields = ['title', 'link', 'summary', 'published']

# apply to_datetime function along published axis in data dataframe
data['published'] = pd.to_datetime(data['published'])
df = data[fields].dropna()

# output the result on all entries on necessary columns to output_task2.json file
with open("output_task2.json", 'w') as outfile:
    df.to_json(outfile, orient="records", date_format='iso')

print(df.info())
