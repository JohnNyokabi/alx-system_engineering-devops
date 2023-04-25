"""Script that extends #0 script to export data in CSV format"""
import sys
import csv
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
        list_task.append([userid,
                          name,
                          task.get('completed'),
                          task.get('title')])

    filename = '{}.csv'.format(userid)
    with open(filename, mode='w') as employee_file:
        employee = csv.writer(employee_file,
                              delimiter=',',
                              quotechar='"',
                              quoting=csv.QUOTE_ALL)

        for task in list_task:
            employee.writerow(task)
