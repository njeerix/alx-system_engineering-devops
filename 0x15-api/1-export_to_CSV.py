#!/usr/bin/python3
import sys
import csv
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

        # Prepare CSV file name
        csv_filename = f"{employee_id}.csv"

        # Write tasks to CSV file
        with open(csv_filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            for todo in todos_data:
                task_completed_status = "True" if todo['completed'] else "False"
                csv_writer.writerow([employee_id, employee_name, task_completed_status, todo['title']])

        print(f"Tasks exported to {csv_filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to fetch data - {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_employee_todo_progress(employee_id)
