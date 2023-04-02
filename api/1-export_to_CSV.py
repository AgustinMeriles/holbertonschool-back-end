#!/usr/bin/python3
"""Shebang"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user = requests.get(user_url).json()

    todos_url = ('https://jsonplaceholder.typicode.com/users/{}/todos'
                 .format(user_id))
    todos = requests.get(todos_url).json()

    filename = '{}.csv'.format(user_id)
    with open(filename, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, user['username'], task['completed'],
            task['title']])

    print("Employee {} is done with tasks({}/{}):".format(user.get('name'),
          len([t for t in todos if t['completed']]), len(todos)))
