#!/usr/bin/python3
"""
    Using what you did in the task #0, extend your Python
    script to export data in the JSON format.
"""


if __name__ == "__main__":
    import json
    import sys
    from urllib import request

    user_id = sys.argv[1]
    user = None
    tasks = None
    user_json = None

    user_url = request.urlopen("https://jsonplaceholder.typicode.com"
                               "/users/{}".format(user_id))
    user = json.loads(user_url.read().decode("utf-8"))

    tasks_url = request.urlopen("https://jsonplaceholder.typicode.com"
                                "/todos?userId={}".format(user_id))
    tasks = json.loads(tasks_url.read().decode("utf-8"))

    tasks_file = open("{}.json".format(user["id"]), "w")

    idx = "{}".format(user["id"])
    user_json = {
        idx: []
    }
    for task in tasks:
        user_json[idx].append({
            "task": task["title"],
            "completed": task["completed"],
            "username": user["username"]
        })

    tasks_file.write(json.dumps(user_json))
    tasks_file.close()
