import os
from github import Github, Auth
import json

token = os.getenv("MY_GITHUB_PAT")

if not token:
    raise ValueError("MY_GITHUB_PAT environment variable not set!")

USERNAME = "SevenKhan"
g = Github(auth=Auth.Token(TOKEN))
user = g.get_user(USERNAME)

profile_info = {
    "login": user.login,
    "name": user.name,
    "bio": user.bio,
    "public_repos": user.public_repos,
    "followers": user.followers,
    "following": user.following
}

repos_list = []
for repo in user.get_repos():
    repos_list.append({
        "name": repo.name,
        "stars": repo.stargazers_count,
        "forks": repo.forks_count,
        "open_issues": repo.open_issues_count,
        "private": repo.private
    })

output = {
    "profile": profile_info,
    "repos": repos_list
}

with open("output.json", "w") as f:
    json.dump(output, f, indent=4)

print("✅ Data saved to output.json")
