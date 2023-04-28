from github import Github, GithubObject
import os

def get_github_instance(token):
    return Github(token)

def get_repository(github_instance, repo_name):
    return github_instance.get_repo(repo_name)

def get_contributors(repo):
    return repo.get_contributors()

def get_commits_by_author(repo, author, since=GithubObject.NotSet):
    return repo.get_commits(author=author, since=since)
