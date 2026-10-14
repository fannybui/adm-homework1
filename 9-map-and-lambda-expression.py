# ==================================================
# EXERCISE 1 : 
# ==================================================

def blabla():


# ==================================================
# MAIN MENU
# ==================================================

def main():
    while True:
        print("\n================================")
        print("STRINGS")
        print("================================")
        # print("1. ")
        # print("2. ")
        # print("3. ")
        # print("4. ")
        # print("5. ")
        # print("6. ")
        print("0. Exit")
        print("================================")

        choice = input("Choose an exercise: ")

        if choice == "1":
            # blabla()

        # elif choice == "2":
        #     runner_up()

        # elif choice == "3":
        #     nested_lists()

        # elif choice == "4":
        #     percentage()

        # elif choice == "5":
        #     lists()

        # elif choice == "6":
        #     tuples()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()