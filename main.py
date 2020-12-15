from flask import Flask, render_template, url_for, request, redirect
import pymongo
from pymongo import MongoClient
import csv
import requests
import http.client
import json
import random
import string
import math
import re

app = Flask(__name__)

client = MongoClient("mongodb+srv://bibartan:bibpass@cluster0.1epb4.mongodb.net/BatchRecords?retryWrites=true&w=majority")


@app.route('/')
def root(method=['GET']):
	db = client["BatchRecords"]
	col = db["BatchRecords"]
	batch_jobs = []
	for doc in col.find():
		batch_jobs.append(doc)
	return render_template('index.html', data=batch_jobs)


@app.route('/batch_jobs', methods=['GET', 'POST'])
def batch_jobs():
	db = client["BatchRecords"]
	col = db["BatchRecords"]
	if request.method == 'GET':
		#filtering:		
		after_input = request.args.get('after')
		before_input = request.args.get('before')
		min_nodes = request.args.get('min_nodes')
		max_nodes = request.args.get('max_nodes')

		filtered_batch_jobs = []
		for doc in col.find():
			passes_after = True
			passes_before = True
			passes_min = True
			passes_max = True

			if doc['submitted_at'] != "":
				if after_input != '':
					if doc['submitted_at'] < after_input:
						passes_after = False
				if before_input != '':
					if doc['submitted_at'] > before_input:
						passes_before = False
			else:
				passes_after = False
				passes_before = False

			if doc['nodes_used'] != "":
				if min_nodes != '':
					if int(doc['nodes_used']) < int(min_nodes):
						passes_min = False
				if max_nodes != '':
					if int(doc['nodes_used']) > int(max_nodes):
						passes_max = False
			else:
				passes_min = False
				passes_max = False

			if passes_after and passes_before and passes_min and passes_max:
				filtered_batch_jobs.append(doc)
		return render_template('index.html', data=filtered_batch_jobs)

	batch_jobs = []
	for doc in col.find():
		batch_jobs.append(doc)
	return render_template('index.html', data=batch_jobs)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)


