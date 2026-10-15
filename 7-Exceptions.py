# ==================================================
# EXERCISE 1 : Exceptions
# ==================================================

def exceptions():

    T = int(input("Enter integer T : "))

    for _ in range(T):
        a, b = input("Enter the space separated values a and b over T lines : ").split()
        try:
            print(int(a) // int(b))
        except Exception as e:
            print("Error Code:", e)

# ==================================================
# MAIN MENU
# ==================================================

def main():
    while True:
        print("\n================================")
        print("EXCEPTIONS")
        print("================================")
        # print("1. ")
        print("0. Exit")
        print("================================")

        choice = input("Choose an exercise: ")

        if choice == "1":
            exceptions()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()