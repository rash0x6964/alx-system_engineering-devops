#!/usr/bin/python3
"""
    Extend Python script in 0-gather_data_from_an_API.py file to export data
    in the JSON format.

    Requirement:
    ============
    Records all tasks from all employees.
"""


if __name__ == "__main__":
    import json
    import requests

    url = "https://jsonplaceholder.typicode.com"
    employees = requests.get(f"{url}/users").json()
    tasks = requests.get(f"{url}/todos").json()

    my_dict = {}
    for employee in employees:
        my_list = [{
            "task": obj.get("title"),
            "completed": obj.get("completed"),
            "username": employee.get("username")}
            for obj in tasks if obj.get("userId") == employee.get("id")
        ]
        my_dict[employee.get("id")] = my_list

    filename = "todo_all_employees.json"
    with open(filename, 'w') as json_file:
        json.dump(my_dict, json_file)
