from github import Github
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import os
import dotenv

# Load the environment variables from the .env file
dotenv.load_dotenv()

g = Github(os.environ.get("PAT"))

repo = g.get_repo(os.environ.get("REPO"))

for contributor in repo.get_contributors():
    print(contributor.login)

since_time = datetime.utcnow() - timedelta(hours=24)

for contributor in repo.get_contributors():
    print(f"Commits by {contributor.login}:")
    # Iterate over all the commits made by the contributor in the last 24 hours.
    for commit in repo.get_commits(author=contributor.login, since=since_time):
        print(commit.sha[:7], ", ", end="", sep='')
    print()

# Create a dictionary to store the number of commits for each contributor.
commits_by_contributor = {}

# Iterate over all the contributors in the repository.
for contributor in repo.get_contributors():
    # Initialize the number of commits for this contributor to 0.
    commits_by_contributor[contributor.login] = 0
    # Iterate over all the commits made by the contributor in the repository.
    for commit in repo.get_commits(author=contributor.login):
        commits_by_contributor[contributor.login] += 1

# Sort the contributors by their total number of commits in descending order.
contributors_sorted = sorted(commits_by_contributor.items(), key=lambda x: x[1], reverse=True)

print("Commits by contributor:\n")

for i, (contributor, commits) in enumerate(contributors_sorted):
    if i == 0:
        print("👑", end="")
    elif commits == 0:
        continue
    else:
        print(f"{i + 1}.", end="")
    print(f" {contributor} ({commits} commits)")

# Get the top 4 contributors
top_contributors = contributors_sorted[:4]

# Initialize a dictionary to store the commits for each of the top 4 contributors
commits_by_top_contributor = {}

for contributor, _ in top_contributors:
    # Initialize an empty list for this contributor
    commits_by_top_contributor[contributor] = []

    # Iterate over all the commits made by the contributor in the repository
    for commit in repo.get_commits(author=contributor):
        # Append the commit's author date to the list
        commits_by_top_contributor[contributor].append(commit.commit.author.date)

# Create a plot for each of the top 4 contributors
for contributor, commit_dates in commits_by_top_contributor.items():
    # Sort the commit dates in ascending order
    commit_dates.sort()

    # Create the X and Y values for the plot
    x_values = commit_dates
    y_values = range(1, len(commit_dates) + 1)

    # Plot the data
    plt.plot(x_values, y_values, label=contributor)

# Customize the plot
plt.xlabel("Date")
plt.ylabel("Number of Commits")
plt.title("Commits Over Time for Top 4 Contributors")
plt.legend()
plt.grid()

# Display the plot
plt.show()
