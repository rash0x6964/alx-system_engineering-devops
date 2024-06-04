#!/usr/bin/python3
"""How many subs"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""

    headers = {'User-Agent': '0x16-api_advanced-jmajetich'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0

    try:
        data = response.json()['data']
        return data['subscribers']
    except (KeyError, ValueError):
        return 0

    pass
