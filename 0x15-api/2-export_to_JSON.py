#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import sys
import json
import requests


def fetch_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        # Fetch user details
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()
        employee_name = user_data['name']

        # Fetch todos for the user
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        # Prepare JSON data structure
        tasks_data = {
            str(employee_id): [
                {
                    "task": todo['title'],
                    "completed": todo['completed'],
                    "username": employee_name
                }
                for todo in todos_data
                if 'title' in todo and 'completed' in todo
            ]
        }

        # Prepare JSON file name
        json_filename = f"{employee_id}.json"

        # Write tasks data to JSON file
        with open(json_filename, 'w') as jsonfile:
            json.dump(tasks_data, jsonfile, separators=(',', ':'))

        print(f"Tasks exported to {json_filename}")

    except requests.exceptions.RequestsException as e:
        print(f"Error: Failed to fetch data - {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_employee_todo_progress(employee_id)
