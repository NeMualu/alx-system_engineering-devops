#!/usr/bin/python3
"""
Script that utilizes a REST API to retrieve progress information
for a given employee's TODO list and exports the data in CSV format.
"""

import csv
import json
import requests
from sys import argv

if __name__ == "__main__":
    sessionReq = requests.Session()

    idEmp = argv[1]
    idURL = f'https://jsonplaceholder.typicode.com/users/{idEmp}/todos'
    nameURL = f'https://jsonplaceholder.typicode.com/users/{idEmp}'

    employee = sessionReq.get(idURL)
    employeeName = sessionReq.get(nameURL)

    json_req = employee.json()
    usr = employeeName.json()['username']

    totalTasks = sum(1 for task in json_req if task['completed'])

    fileCSV = f'{idEmp}.csv'

    with open(fileCSV, "w", newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in json_req:
            csv_writer.writerow([idEmp, usr, task['completed'], task['title']])

