#!/usr/bin/python3
"""Script that sends a POST request with an email parameter."""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    data = urllib.parse.urlencode({"email": sys.argv[2]}).encode("ascii")
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode("utf-8"))
