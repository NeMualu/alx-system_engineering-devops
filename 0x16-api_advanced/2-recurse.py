#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
"""

import requests

def recurse(subreddit, hot_list=[], after=""):
    """
    Queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit.

    - If not a valid subreddit, return None.
    """
    headers = {"User-Agent": "Custom"}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"after": after}
    req = requests.get(url, headers=headers, params=params)

    if req.status_code == 200:
        for get_data in req.json().get("data", {}).get("children", []):
            title = get_data.get("data", {}).get("title")
            if title:
                hot_list.append(title)

        after = req.json().get("data", {}).get("after")

        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
