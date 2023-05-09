#!/usr/bin/python3
"""Returns list of titles of all hot subreddit articles"""
import requests
import sys


def recurse(subreddit, hot_list=[]):
    """Get hot posts titles"""
    url = 'https://reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'user-agent': 'Mozilla/5.0'}
    params = {'limit': 100}
    res = requests.get(url, headers=header, params=params)

    if isinstance(after, str):
        if after != "DONE":
            params['after'] = after
        else:
            return hot_list

    if res.status_code != 200:
        return None
    data = res.json().get('data', {})
    after = data.get('after', 'DONE')
    if (!after):
        after = "DONE"
    hot_list = hot_list + [item.get('data', {}).get('title')
                           for item in data.get('children', [])]
    return recurse(subreddit, hot_list, after)
