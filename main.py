from controller import init_github_repo
from menus.github_menu import github_menu
from menus.vp_menu import vp_menu

def main():
    g, repo = init_github_repo()

    while True:
        print("Welcome to the main menu:")
        print("1. GitHub")
        print("2. VisualParadigm")
        print("3. Quit")

        choice = input("Please enter the number of your choice: ")

        if choice == '1':
            github_menu(repo)
        elif choice == '2':
            vp_menu()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
