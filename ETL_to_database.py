import pymongo
from pymongo import MongoClient
import csv
from csv import reader

try:
	client = MongoClient("mongodb+srv://bibartan:bibpass@cluster0.1epb4.mongodb.net/BatchRecords?retryWrites=true&w=majority")
except:
	print("Could not connect")


db = client['BatchRecords']
collection = db['BatchRecords']


batch_number = 1
with open('example_batch_records.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        dict_record = {"batch_number": batch_number, "submitted_at": row[1],"nodes_used": row[2]}
        #record_submitted = collection.insert_one(dict_record)
        #commented out the line above so that accidentally running this file again dosen't populate the mongodb anymore
        batch_number += 1


