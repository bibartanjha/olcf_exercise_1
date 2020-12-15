import pymongo
from pymongo import MongoClient
import pandas as pd

import csv
from csv import reader
import requests
import time
from datetime import date
import http.client
import json
import random
import pyrebase
import string
import math

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
        batch_number += 1
        record_submitted = collection.insert_one(dict_record) 


