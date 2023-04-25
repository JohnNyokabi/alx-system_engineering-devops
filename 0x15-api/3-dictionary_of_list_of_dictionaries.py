#!/usr/bin/python3
"""extends #0 script to export data in json format"""
import json
import sys
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user = '{}users'.format(url)
    result = requests.get(user)
    json_obj = result.json()
    task_dictionaries = {}
    for user in json_obj:
        name = user.get('username')
        userid = user.get('id')
        todo = '{}todo?userId={}'.format(url, userid)
        result = requests.get(todo)
        tasks = result.json()
        list_task = []
        for task in tasks:
            task_dict = {"username": name,
                         "task": task.get('title')
                         "completed": task.get('completed')}
            list_task.append(task_dict)

        task_dictionaries[str(userid)] = list_task
    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as f:
        json.dump(task_dictionaries, f)
