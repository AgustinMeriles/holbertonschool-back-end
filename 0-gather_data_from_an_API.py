#!/usr/bin/python3
"""Shebang"""
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user = requests.get(url).json()

    url = ('https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(user_id))
    todos = requests.get(url).json()

    completed_tasks = [task.get('title') for task in todos
                       if task.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):".format(user.get('name'),
          len(completed_tasks), len(todos)))
    for task in completed_tasks:
        print("\t {}".format(task))
