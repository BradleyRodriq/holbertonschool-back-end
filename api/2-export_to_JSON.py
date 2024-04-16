#!/usr/bin/python3
""" returns to-do list information about employee ID """
import json
from requests import get
from sys import argv

if __name__ == '__main__':
    APIurl = "https://jsonplaceholder.typicode.com"
    employee = get(APIurl + "/users/{}".format(argv[1])).json()
    to_do_list = get(APIurl + "/todos", params={
        "userId": argv[1]}).json()
    username = employee.get("username")

    with open("{}.json".format(argv[1]), "w") as jsonfile:
        json.dump({argv[1]: [{
            "task": i.get("title"),
            "completed": i.get("completed"),
            "username": username
                }for i in to_do_list]}, jsonfile)
