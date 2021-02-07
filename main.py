# TODO:
#  Tasks for independent work
#  - Expand the list of RSS channels with computer and telecommunication channels (but not trading platforms).
#  - Create a procedure (script) for periodic downloading of information from the created list of RSS-feeds.
#  - Implement the procedure of creating a file that combines all downloaded RSS feeds and connects them
#  to the download script.

import json

import feedparser

with open("config.json") as json_data_file:
    data = json.load(json_data_file)

for link in data['links']:
    d = feedparser.parse(link)
    print('Number of RSS posts :', len(d.entries))
    entry = d.entries[0]
    print('Post Title :', entry.title)
