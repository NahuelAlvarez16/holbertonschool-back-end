#!/usr/bin/python3
"""
    Write a Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""


if __name__ == "__main__":
    import sys
    import json
    from urllib import request

    user_id = sys.argv[1]
    user = None
    tasks = None
    completed_tasks = None

    user_url = request.urlopen("https://jsonplaceholder.typicode.com/users/{}".format(user_id))
    user = json.loads(user_url.read().decode("utf-8"))

    tasks_url = request.urlopen("https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id))
    tasks = json.loads(tasks_url.read().decode("utf-8"))
    completed_tasks = list(filter(lambda task: task["completed"], tasks))

    print("Employee {} is done with tasks({}/{}):".format(user["name"], len(completed_tasks), len(tasks)))
    for task in completed_tasks:
        print("\t {}".format(task['title']))
