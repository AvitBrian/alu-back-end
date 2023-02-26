#!/usr/bin/python3
"""
    python script that returns TODO list progress for a given employee ID
    
    Args:
    ----------
        :param USER_ID: employee ID
        :param EMPLOYEE_NAME: employee name
        :param TOTAL_NUMBER_OF_TASKS: total number of tasks
        :param NUMBER_OF_DONE_TASKS: number of completed tasks
    
    Usage:
    -------------
    Simply run the script with the employee ID as the first argument:
    $ ./0-gather_data_from_an_API.py 2
   
    Output:
    -------------
    Employee Ervin Howell is done with tasks(8/8):
            distinctio vitae autem nihil ut molestias quo
            voluptas quo tenetur perspiciatis explicabo natus
            ...

"""

import requests
from sys import argv

# Parse command line arguments
USER_ID = argv[1]

# Send HTTP requests to get user and todo data
users_response = requests.get(
    f'https://jsonplaceholder.typicode.com/users/{USER_ID}', timeout=10)
todos_response = requests.get(
    f'https://jsonplaceholder.typicode.com/users/{USER_ID}/todos', timeout=10)

# Check if both requests were successful
if users_response.status_code == 200 and todos_response.status_code == 200:

    # Extract data from JSON responses
    user_data = users_response.json()
    todo_data = todos_response.json()

    # Extract employee name and number of completed tasks
    EMPLOYEE_NAME = user_data["name"]
    TOTAL_NUMBER_OF_TASKS = len(todo_data)
    NUMBER_OF_DONE_TASKS = 0
    for task in todo_data:
        if task["completed"] is True:
            NUMBER_OF_DONE_TASKS += 1

    # Print progress report
    print(
        f"Employee {EMPLOYEE_NAME} is done with"
        f" tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    for task in todo_data:
        if task["completed"] is True:
            print(f"\t {task['title']}")
