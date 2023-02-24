#!/usr/bin/python3
"""
    this python script returns progress list of todos for a given employee
    with a defined id.
"""
import json
from sys import argv
import requests


if __name__ == "__main__":

    request_employee = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{argv[1]}/', timeout=10)
    employee = json.loads(request_employee.text)
    employee_name = employee.get("name")

    request_todos = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{argv[1]}/todos', timeout=10)
    tasks = {}

    employee_todos = json.loads(request_todos.text)

    for dictionary in employee_todos:
        tasks.update({dictionary.get("title"): dictionary.get("completed")})

    EMPLOYEE_NAME = employee_name
    TOTAL_NUMBER_OF_TASKS = len(tasks)
    NUMBER_OF_DONE_TASKS = len([k for k, v in tasks.items() if v is True])
    print(f"Employee {EMPLOYEE_NAME} is done with tasks \
        ({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    for k, v in tasks.items():
        if v is True:
            print(f"\t {k}")
