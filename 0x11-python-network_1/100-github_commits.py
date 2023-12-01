#!/usr/bin/python3
""" Python script that takes your GitHub credentials and displays your id """
import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    user = sys.argv[2]
    url = f"https://api.github.com/repos/{user}/{repo}/commits"
    commits = requests.get(url)
    for ele in commits.json()[:10]:
        print(
            f"{ele.get('sha')}: \
{ele.get('commit').get('author').get('name')}"
        )
