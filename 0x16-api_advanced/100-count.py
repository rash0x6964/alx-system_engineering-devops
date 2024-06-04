#!/usr/bin/python3
"""Function to count words in all hot posts of a given subreddit."""

import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """Parses the title of all hot articles,
        and prints a sorted count of given keywords
    """
    if not word_list or word_list == [] or not subreddit:
        return

    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "0x16-api_advanced/task-3"},
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        return

    try:
        data = response.json().get("data", {})
        children = data.get("children", [])

        for post in children:
            title = post["data"]["title"].lower()
            for word in word_list:
                word_lower = word.lower()
                if word_lower in title:
                    counts[word_lower] = (
                        counts.get(word_lower, 0) + title.count(word_lower)
                    )

        after = data.get("after")
        if after:
            count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print("{}: {}".format(word, count))

    except ValueError:
        return
