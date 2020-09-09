import requests
import os
import json


def getAPI(url):
    r = requests.get(url, auth=('joeysnclr', os.getenv("GITHUB_TOKEN")))
    return r.json()


def getReposCount():
    data = getAPI('https://api.github.com/users/joeysnclr')
    return data['public_repos']


def getStarCount():
    data = getAPI('https://api.github.com/users/joeysnclr/repos')
    stars = 0
    for repo in data:
        stars += repo['stargazers_count']
    return stars


def getContributionsCount():
    data = getAPI('https://api.github.com/users/joeysnclr/repos')
    contributions = 0
    for repo in data:
        if repo['fork']:
            contributions += 1
    return contributions
