# This program converts a csv record to a predetermined hierchical JSON format 
# To make sense of the program, look at "json.example.py.comments - it's the same program but commented

import csv
import json

f = open("json.example.04.input.data","r")
reader = csv.DictReader(f)


for r in reader: 
    print r


    doc_string  =  '{ "parents": {"name": "'+r["name"]+'","spouse": "'+r["spouse"]+'"'

    if int(r['children']) == 0:
       doc_string = doc_string + '}}'


    print doc_string

    doc = json.loads(doc_string)

    print doc['parents']

    print json.dumps(doc)

