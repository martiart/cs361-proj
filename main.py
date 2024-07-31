from book_tracker import *
"""
UI of book tracker
"""


def main():
    """Main body of Book Tracker UI"""
    try:
        book_tracker = BookTracker()
        print("------------------------------")
        print("Welcome to Book Tracker by Art!")
        print("------------------------------")

        print("Let's verify your account:")

        valid = False
        # Enter while loop to validate name
        while not valid:
            if not valid:
                user_name = book_tracker.validate_user()
                if user_name == -1:  # user decided to not create account
                    break
                else:
                    valid = True

        # if user already had an account or decided to create an account
        if valid:
            print()
            print(f'What can I do for you today {user_name}?')
            print("------------------------------")
            while True:  # Go through while loop until user decides to exit
                # Menu option of Book Tracker functionalities
                print("1. Add Book")
                # print("2. Edit Book Status")
                # print("3. Get Read Books")
                # print("4. Get Unread Books")
                # print("5. Delete Book")
                print("2. Account Management")
                print("7. Exit Application (or type x)")
                print("0. Enter 0 to learn more about Book Tracker by Art")
                menu_choice = input("Enter menu option: ")

                # Cases for the 7 menu options
                if menu_choice == '1':  # Add Book
                    book_tracker.add_book(user_name)

                # elif menu_choice == '2':  # Edit Book Status
                #     pass
                #
                # elif menu_choice == '3':  # Get Read Books
                #     pass
                #
                # elif menu_choice == '4':  # Get Unread Books
                #     pass
                #
                # elif menu_choice == '5':  # Delete Book
                #     pass

                elif menu_choice == '2':  # Account Management
                    user_name = book_tracker.account_management(user_name)
                    if user_name == -1:
                        break
                elif menu_choice == 'x' or menu_choice == 'x'.upper() or menu_choice == '7':
                    break

                elif menu_choice == '0':
                    print("About: \n Book Tracker is an easy and simple way to manage your reading habits! ")
                    print("Many apps claim to be Book Trackers but are very complicated.\n")
                    print("Here with Book Tracker by Art we keep things simple.")
                    print("You can modify your accounts and modify your books because what else do you really need?!")
                    print("Application was inspired by my wife! I hope this tracker can help you too!")

                else:
                    print("Invalid Option!")
                print()

    except KeyboardInterrupt as e:  # Handles case of manually exiting application from IDE
        print()
        print("You force exited the application!")

    print("Thank you for using Art's Book Tracker!")


if __name__ == "__main__":
    main()
