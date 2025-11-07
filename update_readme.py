import json

with open("output.json") as f:
    data = json.load(f)

repos_count = data['profile']['public_repos']
followers = data['profile']['followers']
following = data['profile']['following']

repos_table = ""
for repo in data['repos']:
    repos_table += f"| {repo['name']} | {repo['stars']} | {repo['forks']} | {repo['open_issues']} |\n"

with open("README.md") as f:
    readme = f.read()

readme = readme.replace("<!-- REPOS_COUNT -->", str(repos_count))
readme = readme.replace("<!-- FOLLOWERS -->", str(followers))
readme = readme.replace("<!-- FOLLOWING -->", str(following))
readme = readme.replace("<!-- REPOS_TABLE -->", repos_table)

with open("README.md", "w") as f:
    f.write(readme)

print("✅ README.md updated successfully!")
