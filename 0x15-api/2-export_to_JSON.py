#!/usr/bin/python3
"""Export data from API to the JSON format."""


if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    url = "https://jsonplaceholder.typicode.com"
    userId = argv[1]
    employee = requests.get(f"{url}/users/{userId}").json().get("username")
    tasks = requests.get(f"{url}/todos?userId={userId}").json()
    my_list = [{
        "task": dict.get("title"),
        "completed": dict.get("completed"),
        "username": employee}
        for dict in tasks
    ]

    filename = f"{userId}.json"
    with open(filename, 'w') as json_file:
        json.dump({userId: my_list}, json_file)
