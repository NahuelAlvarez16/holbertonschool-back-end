#!/usr/bin/python3
"""
    Using what you did in the task #0, extend your Python
    script to export data in the JSON format.
"""


if __name__ == "__main__":
    import json
    import sys
    from urllib import request

    users = None
    tasks = None
    users_json = {}

    users_url = request.urlopen("https://jsonplaceholder.typicode.com/users")
    users = json.loads(users_url.read().decode("utf-8"))

    tasks_url = request.urlopen("https://jsonplaceholder.typicode.com/todos")
    tasks = json.loads(tasks_url.read().decode("utf-8"))

    tasks_file = open("todo_all_employees.json.json", "w")

    for user in users:
        idx = "{}".format(user["id"])
        filtered_task = list(filter(lambda task: task["userId"] == user["id"],
                                    tasks))
        users_json[idx] = []
        for task in filtered_task:
            users_json[idx].append({
                "username": user["username"],
                "task": task["title"],
                "completed": task["completed"]
            })

    tasks_file.write(json.dumps(users_json))
    tasks_file.close()
