#!/usr/bin/python3
"""Shebang"""
import json
import requests


if __name__ == "__main__":
    users_url = 'https://jsonplaceholder.typicode.com/users'
    users = requests.get(users_url).json()

    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    todos = requests.get(todos_url).json()

    data = {}
    for user in users:
        user_id = str(user.get('id'))
        username = user.get('username')
        user_todos = [task for task in todos if task.get('userId') == user_id]
        user_tasks = []
        for task in user_todos:
            user_tasks.append({
                "username": username,
                "task": task.get('title'),
                "completed": task.get('completed')
            })
        data[user_id] = user_tasks

    with open('todo_all_employees.json', 'w') as f:
        json.dump(data, f)
