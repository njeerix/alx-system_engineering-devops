#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import sys
import json
import requests


def export_employee_todo_list_to_json(user_id):
    url = "https://jsonplaceholder.typicode.com/"

    try:
        # Fetch user details
        user_response = requests.get(url + f"users/{user_id}")
        user_response.raise_for_status()
        user_data = user_response.json()
        username = user_data.get('username')

        # Fetch todos for the user
        todos_response = requests.get(url + "todos", params={"userId": user_id)
        todos_response.raise_for_status()
        todos = todos_response.json()

        # Check if todos is a list of dicts
        if not isinstance(todos, list) or \
           not all(isinstance(todo, dict) for todo in todos):
            raise ValueError("Todos data is not a list of dicts")

        # Prepare JSON data structure
        user_data = [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
        } for t in todos]

        # Write tasks data to JSON file
        filename = f"{user_id}.json"
        with open(filename, "w") as jsonfile:
             json.dump({user_id: user_tasks}, jsonfile, separators=(',', ':'))

        print(f"To-do list exported to {filename}")

    except requests.exceptions.RequestsException as e:
        print(f"Error: Failed to fetch data - {e}")
        sys.exit(1)
    except (json.JSONDecodeError, KeyError) as e:
        print(f"Error: Invalid JSON response - {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except IOError as e:
        print(f"Error: Failed to write JSON file - {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 export_to_JSON.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    export_employee_todo_list_to_json(user_id)
