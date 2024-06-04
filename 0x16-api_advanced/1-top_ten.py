#!/usr/bin/python3
"""Function to print hot posts on a given subreddit."""

import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""

    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "0x16-api_advanced/task-1"},
        params={"limit": 10},
        allow_redirects=False
    )

    if response.status_code != 200:
        print("None")
        return

    try:
        data = response.json().get("data", {})
        for child in data.get("children", []):
            title = child.get("data", {}).get("title", "None")
            print(title)
    except ValueError:
        print("None")
