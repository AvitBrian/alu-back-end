#!/usr/bin/python3
"""
Python script that exports data in the JSON format.

Usage:
    Simply run the script to generate a JSON file containing data for all employees:
    $ ./1-export_to_JSON.py

Output:
    A file named 'todo_all_employees.json' containing data for all employees in JSON format.
"""

import json
import requests

if __name__ == "__main__":
    # URL of the API
    url = "https://jsonplaceholder.typicode.com/"

    # Retrieve all users
    users_data = requests.get(url + "users").json()

    # Export data to a JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        # Use a dictionary comprehension to format data for each user
        users_dict = {
            user.get("id"): [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user.get("username")
            } for task in requests.get(url + "todos", params={"userId": user.get("id")}).json()]
            for user in users_data
        }

        # Write data to JSON file
        json.dump(users_dict, jsonfile)
