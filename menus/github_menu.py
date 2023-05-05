from controller import list_contributors, display_commits_last_24h, display_commit_leaderboard, show_commit_graph, display_commits_last_h


def github_menu(repo):
    while True:
        print("\nGitHub menu:")
        print("1. List contributors")
        print("2. Display commits in the last 24 hours")
        print("3. Display commit leaderboard")
        print("4. Show commit graph")
        print("5. Display commits in the last 5 hours")
        print("6. Return to main menu")

        choice = input("Please enter the number of your choice: ")

        if choice == '1':
            list_contributors(repo)
        elif choice == '2':
            display_commits_last_24h(repo)
        elif choice == '3':
            display_commit_leaderboard(repo)
        elif choice == '4':
            show_commit_graph(repo)
        elif choice == '5':
            display_commits_last_h(repo, 5)
        elif choice == '6':
            print("Returning to main menu...")
            break
        else:
            print("Invalid input. Please try again.")
