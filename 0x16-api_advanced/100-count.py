#!/usr/bin/python3
"""prints top ten hot posts of subreddit"""
import requests
import sys
import re


def append_title(dic, posts):
    """appends items into the list"""
    if len(posts) == 0:
        return

    title = posts[0]['data']['title'].split()
    for value in title:
        for key in dic.keys():
            c = re.compile("^{}$".format(key), re.I)
            if c.findall(value):
                dic[key] += 1
    posts.pop(0)
    append_title(dic, posts)


def recurse(subreddit, dic, after=None):
    """Returns recursive Reddit API"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'user-agent': 'Mozilla/5.0'}
    params = {'after': after}
    res = requests.get(url, headers, params)

    if res.status_code != 200:
        return None
    data = res.json()
    posts = data['data']['children']
    append_title(dic, posts)
    after = data['data']['after']
    if (!after):
        return
    recurse(subreddit, dic, after=after)


def count_words(subreddit, word_list):
    """prints sorted count of given keywords"""
    dic = {}

    for word in word_list:
        dic[word] = 0

    recurse(subreddit, dic)

    _list = sorted(dic.items(), key=lambda kv: kv[1])
    _list.reverse()

    if len(_list) != 0:
        for item in _list:
            if (item[1]) != 0:
                print("{}: {}".format(item[0], item[1]))
    else:
        print("")
