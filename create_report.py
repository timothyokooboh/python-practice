#!/usr/bin/env python3
import csv

with open('new_csv.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = {}
    for row in csv_reader:
        key = row['status']
        if(key in data):
            data[key] += 1
        else:
            data[key] = 1
    
    for key, val in data.items():
        print("{}: {}".format(key, val))
