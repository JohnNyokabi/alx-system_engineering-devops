#!/usr/bin/python3
"""Script that returns information about a user TODO list"""
import sys
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(url, sys.argv[1])
    response = requests.get(user)
    json_obj = response.json()
    print("Employee {} is done with tasks".format(
        json_obj.get('name')), end="")

    todos = '{}todos?userID={}'.format(url, sys.argv[1])
    response = requests.get(todos)
    tasks = response.json()
    list_task = []
    for task in tasks:
        if task.get('completed') is True:
            list_task.append(task)

    print("({}/{}):".format(len(list_task), len(tasks)))
    for task in list_task:
        print("\t {}".format(task.get("title")))
