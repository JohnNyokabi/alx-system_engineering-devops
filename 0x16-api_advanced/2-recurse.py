#!/usr/bin/python3
"""Returns list of titles of all hot subreddit articles"""
import requests
import sys


def append_list(hot_list, posts):
    """adds item to the list"""
    if len(posts) == 0:
        return
    hot_list.append(posts[0]['data']['title'])
    posts.pop(0)
    append_list(hot_list, posts)


def recurse(subreddit, hot_list=[], after=None):
    """Get hot posts titles"""
    url = 'https://reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'user-agent': 'Mozilla/5.0'}
    params = {'after': after}
    res = requests.get(url, headers=header, params=params)

    if res.status_code != 200:
        return None
    dictionary = res.json()
    posts = dictionary['data']['children']
    append_list(hot_list, posts)
    after = dictionary['data']['after']
    if not after:
        return hot_list
    return recurse(subreddit, hot_list=hot_list, after=after)
