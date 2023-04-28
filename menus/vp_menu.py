from controller import display_revision_leaderboard, show_revision_graph


def vp_menu():
    while True:
        print("\nVisualParadigm menu:")
        print("1. Display revision leaderboard")
        print("2. Show revision graph")
        print("3. Return to main menu")

        choice = input("Please enter the number of your choice: ")

        if choice == '1':
            display_revision_leaderboard()
        elif choice == '2':
            show_revision_graph()
        elif choice == '3':
            print("Returning to main menu...")
            break
        else:
            print("Invalid input. Please try again.")
