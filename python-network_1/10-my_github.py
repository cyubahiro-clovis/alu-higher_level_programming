#!/usr/bin/python3
"""Script that displays a GitHub user id using Basic Authentication."""
import requests
import sys


if __name__ == "__main__":
    auth = (sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
