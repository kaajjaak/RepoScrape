import os
import dotenv
from github_utils.github_utils import get_github_instance, get_repository, get_contributors, get_commits_by_author
from data_processing.data_processing import get_recent_commits, count_commits_by_contributor, \
    sort_contributors_by_commits, parse_revision_xml, sort_revisions
from plotting.plotting import plot_commits_over_time, parse_revision_dates, plot_revision_dates

dotenv.load_dotenv()


def init_github_repo():
    g = get_github_instance(os.environ.get("PAT"))
    repo = get_repository(g, os.environ.get("REPO"))
    return g, repo


def list_contributors(repo):
    contributors = get_contributors(repo)
    for contributor in contributors:
        print(contributor.login)
    print()


def display_commits_last_24h(repo):
    recent_commits = get_recent_commits(repo, get_commits_by_author)
    for contributor, commits in recent_commits.items():
        print(f"Commits by {contributor}: {', '.join(commit.sha[:7] for commit in commits)}")
    print()


def display_commit_leaderboard(repo):
    commits_by_contributor = count_commits_by_contributor(repo, get_commits_by_author)
    contributors_sorted = sort_contributors_by_commits(commits_by_contributor)

    print("Commits by contributor:\n")
    for i, (contributor, commits) in enumerate(contributors_sorted):
        if i == 0:
            print("👑", end="")
        elif commits == 0:
            continue
        else:
            print(f"{i + 1}.", end="")
        print(f" {contributor} ({commits} commits)")
    print()


def display_revision_leaderboard():
    revision_file_path = "revision.xml"
    revisions = parse_revision_xml(revision_file_path)
    revisions_sorted = sort_revisions(revisions)

    print("\nRevisions by contributor:\n")
    for i, (contributor, revisions) in enumerate(revisions_sorted):
        if i == 0:
            print("👑", end="")
        elif revisions == 0:
            continue
        else:
            print(f"{i + 1}.", end="")
        print(f" {contributor} ({revisions} revisions)")
    print()


def show_commit_graph(repo):
    top_contributors = sort_contributors_by_commits(count_commits_by_contributor(repo, get_commits_by_author))[:4]
    commits_by_top_contributor = {}

    for contributor, _ in top_contributors:
        commits_by_top_contributor[contributor] = [commit.commit.author.date for commit in
                                                   get_commits_by_author(repo, contributor)]

    plot_commits_over_time(commits_by_top_contributor)


def show_revision_graph():
    revision_file_path = "revision.xml"
    revision_dates = parse_revision_dates(revision_file_path)
    plot_revision_dates(revision_dates)
