from datetime import datetime, timedelta
import xml.etree.ElementTree as ET

def get_recent_commits(repo, get_commits_by_author_func, hours=24):
    since_time = datetime.utcnow() - timedelta(hours=hours)
    recent_commits = {}

    for contributor in repo.get_contributors():
        recent_commits[contributor.login] = get_commits_by_author_func(repo, contributor.login, since=since_time)

    return recent_commits

def count_commits_by_contributor(repo, get_commits_by_author_func):
    commits_by_contributor = {}

    for contributor in repo.get_contributors():
        commits_by_contributor[contributor.login] = len(list(get_commits_by_author_func(repo, contributor.login)))

    return commits_by_contributor


def sort_contributors_by_commits(commits_by_contributor):
    return sorted(commits_by_contributor.items(), key=lambda x: x[1], reverse=True)


def parse_revision_xml(file_path):
    mytree = ET.parse(file_path)
    myroot = mytree.getroot()

    revisions = {}

    for tag in myroot:
        user = tag.attrib.get("user")
        if user in revisions:
            revisions[user] += 1
        else:
            revisions[user] = 1

    return revisions

def sort_revisions(revisions):
    return sorted(revisions.items(), key=lambda x: x[1], reverse=True)
