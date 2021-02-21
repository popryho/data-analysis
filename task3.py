# source https://medium.com/analytics-vidhya/quick-start-elasticsearch-with-python-a2578cd87339

# TODO:
#  1. Write a program for creating a batch file for upload to Elasticsearch based on the file
#  generated in the previous lesson in JSON format.
#  2. Install the curl utility on your computer (http://curl.se) and
#  learn the composition and values of its basic parameters.
#  3. Get acquainted with the composition and content of CRUD-operations in Elasticsearch.

import json

import requests
from elasticsearch import Elasticsearch

# Display page 'http://localhost:9200' content.
# Just unnecessary information, no longer used.
res = requests.get('http://localhost:9200')
print(res.json())

es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])

# open the file with outputs and read it
f = open("output_task2.json")
data = f.read()

i = 1
# Send the data into es
for body in json.loads(data):
    es.index(index='popryho',
             id=i, body=body, ignore=400)

    i = i + 1
