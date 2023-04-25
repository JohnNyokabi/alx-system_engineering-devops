#!/usr/bin/python3
"""Extends #0 script to export data in JSON format"""
import sys
import json
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'

    userid = sys.argv[1]
    user = '{}users/{}'.format(url, userid)
    result = requests.get(user)
    json_obj = result.json()
    name = json_obj.get('username')

    todo = '{}todo?userID={}'.format(url, userid)
    result = requests.get(todo)
    tasks = result.json()
    list_task = []
    for task in tasks:
        task_dict = {"task": task.get('title'),
                     "completed": task.get('completed'),
                     "username": name}
        list_task.append(task_dict)

    task_dictionaries = {str(userid): list_task}
    filename = '{}.json'.format(userid)
    with open(filename, mode='w') as f:
        json.dump(task_dictionaries, f)
