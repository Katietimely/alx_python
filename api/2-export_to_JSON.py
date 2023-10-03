import requests
import json
import sys

def get_employee_data(employee_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/uders/{employee_id}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    return user_data, todos_data

def display_todo_progress(user_data, todos_data):
    employee_name = user_data['name']
    total_tasks = len(todos_data)
    complete_tasks = [task for task in todos_data if task['completed']]

    print(f"Employee  {employee_name} is done with tasks({len(complete_task)}/{total_tasks}):")

    for task in complete_tasks:
        print(f"    {task['title']}")

    return user_data['id'], user_data['username'], complete_tasks


def export_to_json(user_id, username, complete_tasks):
    data = {user_id: [{"task": task['title'], "completed": task['completed'], "username": username} for task in complete_tasks]}
    filename = f"{user_id}.json"
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    user_data, todos_data = get_employee_data(employee_id)

    user_id, username, complete_tasks = display_todo_progress(user_data, todos_data)
    export_to_json(user_id, username, complete_tasks)

    
