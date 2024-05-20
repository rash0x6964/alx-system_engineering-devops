#!/usr/bin/python3
"""Export data from API to the CSV format."""


if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    url = "https://jsonplaceholder.typicode.com"
    userId = argv[1]
    employee = requests.get(f"{url}/users/{userId}").json().get("username")
    tasks = requests.get(f"{url}/todos?userId={userId}").json()

    filename = f"{userId}.csv"
    with open(filename, 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        list = [
            [userId, employee, task.get("completed"), task.get("title")]
            for task in tasks
        ]

        taskwriter.writerows(list)
