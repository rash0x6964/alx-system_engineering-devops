#!/usr/bin/python3
"""Using REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    url = "https://jsonplaceholder.typicode.com"
    userId = argv[1]
    employee = requests.get(f"{url}/users/{userId}").json().get("name")
    tasks = requests.get(f"{url}/todos?userId={userId}").json()
    completed = [dict.get("title") for dict in tasks if dict.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        employee, len(completed), len(tasks)))
    for task in completed:
        print("\t {}".format(task))
