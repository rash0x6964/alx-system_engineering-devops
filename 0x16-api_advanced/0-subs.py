#!/usr/bin/python3
"""How many subs"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""

    response = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "0x16-api_advanced/task-0"},
        allow_redirects=False
    )

    if response.status_code != 200:
        return 0

    try:
        data = response.json()["data"]
        return data["subscribers"]
    except (KeyError, ValueError):
        return 0
