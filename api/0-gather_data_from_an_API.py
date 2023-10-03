#!/usr/bin/python3

import requests
import sys

def get_employee_data(employee_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    return user_data, todos_data


def display_todo_progress(user_data, todos_data):
    employee_name = user_data['name']
    total_tasks = len(todos_data)
    complete_tasks = [task for task in todos_data if task['completed']]

    print(f"Employee {employee_name} is done with tasks ({len(complete_tasks)}):")


    for task in complete_tasks:
        print(f"    {task['title' ]}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv)
    user_data, todos_data = get_employee_data(employee_id)

    display_todo_progress(user_data, todos_data)

