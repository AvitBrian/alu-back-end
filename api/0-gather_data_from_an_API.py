#!/usr/bin/python3
"""
    this python script returns progress list of TODO for a given employee
    with a defined id.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """
        send get request for user info
    """
    request_employee = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{argv[1]}/', timeout=10)

    """
        converts the json string to a python dictionary
    """
    employee = json.loads(request_employee.text)

    """
        extracts the name of the employee
    """
    employee_name = employee.get("name")

    """
        request list
    """
    request_todos = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{argv[1]}/todos', timeout=10)
   
    tasks = {}
    """
        converts the json string to a python dictionary
    """
    employee_todos = json.loads(request_todos.text)
    """ loops through the list of dictionaries """
    # adds the title of the task and the status of the task to the dictionary
    for dictionary in employee_todos:
        tasks.update({dictionary.get("title"): dictionary.get("completed")})

    """printing out the tasks that are completed"""
    # loops through the dictionary and prints out the title of the task
    EMPLOYEE_NAME = employee_name
    TOTAL_NUMBER_OF_TASKS = len(tasks)
    NUMBER_OF_DONE_TASKS = len([k for k, v in tasks.items() if v is True])
    print(f"Employee {EMPLOYEE_NAME} is done with tasks \
        ({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    for k, v in tasks.items():
        if v is True:
            print(f"\t {k}")
