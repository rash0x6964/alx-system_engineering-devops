#!/usr/bin/python3
"""Recursive function that queries the Reddit API
    and returns a list containing the titles of
    all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, title_list=[], count=0, after=None):
    """Returns all hot posts of the subreddit"""

    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        params={"count": count, "after": after},
        headers={"User-Agent": "0x16-api_advanced/task-2"},
        allow_redirects=False
    )

    if response.status_code != 200:
        return None

    try:
        data = response.json().get("data", {})
        children = data.get("children", [])
        after = data.get("after")

        title_list.extend([child.get("data", {}).get("title", "None")
                           for child in children])

        if not after:
            return title_list

        return recurse(
            subreddit,
            title_list,
            count + len(children),
            after
        )

    except ValueError:
        return None
