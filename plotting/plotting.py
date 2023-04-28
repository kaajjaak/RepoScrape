import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def plot_commits_over_time(commits_by_top_contributor):
    for contributor, commit_dates in commits_by_top_contributor.items():
        commit_dates.sort()
        x_values = commit_dates
        y_values = range(1, len(commit_dates) + 1)
        plt.plot(x_values, y_values, label=contributor)

    plt.xlabel("Date")
    plt.ylabel("Number of Commits")
    plt.title("Commits Over Time for Top 4 Contributors")
    plt.legend()
    plt.grid()
    plt.show()



def parse_revision_dates(file_path):
    mytree = ET.parse(file_path)
    myroot = mytree.getroot()

    revisions = {}

    for tag in myroot:
        user = tag.attrib.get("user")
        timestamp = int(tag.attrib.get("datetime")) // 1000
        date = datetime.fromtimestamp(timestamp, tz=timezone.utc).strftime('%d/%m/%Y')

        if user not in revisions:
            revisions[user] = {}
        if date not in revisions[user]:
            revisions[user][date] = 0
        revisions[user][date] += 1

    return revisions

def plot_revision_dates(revisions):
    for user, data in revisions.items():
        sorted_dates = sorted(data.keys(), key=lambda d: datetime.strptime(d, '%d/%m/%Y'))
        x = [datetime.strptime(date, '%d/%m/%Y') for date in sorted_dates]
        y = []
        cumulative_revisions = 0
        for date in sorted_dates:
            cumulative_revisions += data[date]
            y.append(cumulative_revisions)
        name = user.split('@')[0].split('.')[0].capitalize()
        plt.plot(x, y, label=name)

    plt.xlabel('Date')
    plt.ylabel('Cumulative Number of Revisions')
    plt.legend()

    ax = plt.gca()
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=7))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
    plt.xticks(rotation=65)
    plt.tight_layout()
    plt.show()

