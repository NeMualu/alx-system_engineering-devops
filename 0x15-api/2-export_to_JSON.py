#!/usr/bin/python3
"""
Script that utilizes a REST API to retrieve progress information
for a given employee's TODO list and exports the data in JSON format.
"""
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

    totalTasks = []
    updateUser = {}

    for task in json_req:
        totalTasks.append(
            {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": usr,
            })
    updateUser[idEmp] = totalTasks

    file_Json = f'{idEmp}.json'
    with open(file_Json, 'w') as f:
        json.dump(updateUser, f)

