#!/usr/bin/python3
"""Returns number of subscribers"""
import requests
import sys

url = 'https://www.reddit.com/r/{}/about.json'


def number_of_subscribers(subreddit):
    """subscribers"""
    header = {'user-agent': 'Mozilla/5.0'}
    res = requests.get(url.format(subreddit), headers=header)
    if res.status_code != 200:
        return 0
    return res.json().get("data", {}).get("subscribers", 0)
