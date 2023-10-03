import requests
import csv
import sys

def get_employee_data(employee_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data =  user_response.json()
    todos_data = todos_response.json()

    return user_data, todos_data


def display_todo_progress(user_data, todos_data):
    employee_name = user_data['name']
    total_tasks = len(todos_data)
    complete_tasks = [task for task in todos_data if task['completed']]

    print(f"Employee {employee_name} is done with tasks({len(complete_tasks)}/{total_tasks}):")

    for task in complete_tasks:
        print(f"   {task['title']}")

    return user_data['id'], user_data['username'], complete_tasks

def export_to_csv(user_id, username, complete_tasks):
    filename = f"{user_id}.csv"
    with open(filename, mode='w', newline='') as  file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in complete_tasks:
            writer.writerow([user_id, username, True, task['title']])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    user_data, todos_data = get_employee_data(employee_id)

    user_id, username, complete_tasks = display_todo_progress(user_data, todos_data)
    export_to_csv(user_id, username, complete_tasks)
