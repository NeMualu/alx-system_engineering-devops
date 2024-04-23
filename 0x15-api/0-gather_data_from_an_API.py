#!/usr/bin/python3
"""
Script that fetches information about a given employee's TODO list progress
from a REST API
"""

import json
import requests
import sys


if __name__ == "__main__":

    sessionReq = requests.Session()

    idEmp = sys.argv[1]
    idURL = f'https://jsonplaceholder.typicode.com/users/{idEmp}/todos'
    nameURL = f'https://jsonplaceholder.typicode.com/users/{idEmp}'

    employee = sessionReq.get(idURL)
    employeeName = sessionReq.get(nameURL)

    json_req = employee.json()
    name = employeeName.json()['name']

    totalTasks = sum(1 for task in json_req if task['completed'])

    print(f"Employee {name} is done with tasks ({totalTasks}/{len(json_req)}):")

    for done_tasks in json_req:
        if done_tasks['completed']:
            print(f"\t {done_tasks.get('title')}")

