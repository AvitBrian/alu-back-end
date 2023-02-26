#!/usr/bin/python3
"""
Python script that retrieves and saves a TODO list for a given employee ID.

Usage:
------
Run the script with the employee ID as the first argument:
    $ ./gather_data_from_api.py 2

Args:
-----
    employee_id: int, the ID of the employee whose TODO list should be retrieved.

Output:
-------
A CSV file named "<employee_id>.csv" with the following columns:
    - Employee ID
    - Employee Name
    - Task Completion Status
    - Task Description
"""

import csv
import json
import requests
from sys import argv

if __name__ == "__main__":
    # Retrieve user data
    user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}', timeout=10)
    user_data = user_response.json()
    employee_name = user_data["name"]

    # Retrieve TODO list
    todo_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}/todos', timeout=10)
    todo_data = todo_response.json()

    # Process TODO list data
    tasks = {}
    for task in todo_data:
        task_description = task["title"]
        task_completion_status = task["completed"]
        tasks[task_description] = task_completion_status

    # Write data to CSV file
    with open(f'{argv[1]}.csv', mode='w', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL)
        for task_description, task_completion_status in tasks.items():
            csv_writer.writerow([argv[1], employee_name, task_completion_status, task_description])
