#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, print None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Custom"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        for post in response.json().get("data", {}).get("children", []):
            title = post.get("data", {}).get("title")
            print(title)
    else:
        print(None)

