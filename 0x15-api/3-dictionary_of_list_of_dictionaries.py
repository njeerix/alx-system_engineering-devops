#!/usr/bin/python3
"""
Exports to-do list information of all employees to JSON format.
"""

import json
import requests

def export_todo_all_employees_to_json():
    base_url = "https://jsonplaceholder.typicode.com"

    try:
        # Fetch all users
        users_response = requests.get(f"{base_url}/users")
        users_response.raise_for_status()
        users = users_response.json()

        # Prepare dictionary to hold user tasks
        user_tasks = {}

        # Iterate over each user to fetch their tasks
        for user in users:
            user_id = user["id"]
            username = user["username"]

            # Fetch tasks for current user
            tasks_response = requests.get(f"{base_url}/todos", params={"userId": user_id})
            tasks_response.raise_for_status()
            tasks = tasks_response.json()

            # Prepare task list for current user
            user_task_list = [{"task": task["title"], "completed": task["completed"], "username": username} for task in tasks]

            # Add user task list to dictionary
            user_tasks[user_id] = user_task_list

        # Write user tasks list to dictionsry
        with open ("todo_all_employees.json", "w") as jsonfile:
            json.dump(user_tasks, jsonfile, separators=(',', ':'))

        print("Export successful: todo_all_employees.json created.")

    except requests.exceptions.RequestsException as e:
        print(f"Error occurred during API request: {e}")

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")

    except IOError as e:
        print(f"Error writing to JSON file: {e}")


if __name__ == "__main__":
    export_todo_all_employees_to_json()
