#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import sys
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

        # Calculate progress
        total_tasks = len(todos_data)
        completed_tasks = sum(1 for todo in todos_data if todo['completed'])
        # Print progress information
        print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
        for todo in todos_data:
            if todo['completed']:
                print(f"    {todo['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to fetch data - {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_todo_progress(employee_id)
