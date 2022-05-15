#!/usr/bin/env python3
import csv

with open('/Users/mac/downloads/generated.csv') as old_file:
    new_file = csv.DictReader(old_file)
    keys = ['status', 'user', 'email', 'phoneNumber', 'location', 'date']
    with open('new_csv.csv', 'w') as generated_csv_file:
        new_file_csv = csv.DictWriter(generated_csv_file, fieldnames=keys)
        new_file_csv.writeheader()
        for row in new_file:
            new_file_csv.writerow(row)
