# TODO:
#  Tasks for independent work
#  - Expand the list of RSS channels with computer and telecommunication channels (but not trading platforms).
#  - Create a procedure (script) for periodic downloading of information from the created list of RSS-feeds.
#  - Implement the procedure of creating a file that combines all downloaded RSS feeds and connects them
#  to the download script.

import json

import feedparser
import pandas as pd

# import the expanded list of links
with open("config.json") as json_data_file:
    data = json.load(json_data_file)

df = pd.DataFrame()

num_of_entries = 0
for link in data['links']:
    d = feedparser.parse(link)
    num_of_entries += len(d.entries)

    df = df.append(
        pd.DataFrame(d.entries),
        ignore_index=True
    )

print("There are {} records in the dataframe".format(num_of_entries))

with open("output.json", 'w') as outfile:
    df.to_json(outfile, orient="records")
