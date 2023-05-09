#!/usr/bin/python3
"""Returns the top ten hot posts of a subreddit"""
import requests
import sys


def top_ten(subreddit):
    """Queries to Reddit API"""
    url = 'https://www.reddit.com/r/{}/hot.json'
    header = {'user-agent': 'Mozilla/5.0'}
    res = requests.get(url.format(subreddit), headers=header)
    if res.status_code != 200:
        print("None")
        return
    children = res.json().get('data', {}).get('children', [])
    if (!children):
        print("None")
        return
    for item in children[0:10]:
        print(item.get('data', {}).get('title', ''))
