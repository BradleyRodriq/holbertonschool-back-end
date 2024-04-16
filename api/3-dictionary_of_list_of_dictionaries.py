#!/usr/bin/python3
""" returns to-do list information about employee ID """
import json
import requests
from requests import get


if __name__ == '__main__':
    APIurl = 'https://jsonplaceholder.typicode.com'
    users = get(APIurl + "/users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            i.get("id"): [{
                "task": n.get("title"),
                "completed": n.get("completed"),
                "username": i.get("username")
            }for n in requests.get(APIurl + "/todos",
                                   params={"userId": i.get("id")}).json()]
            for i in users}, jsonfile)
