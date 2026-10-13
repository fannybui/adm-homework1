# ==================================================
# EXERCISE 1 : collections.Counter()
# ==================================================
from collections import Counter

def shoe_counter():

    X = int(input("Enter the total number of shoes : "))
    shoe_sizes = Counter(map(int, input("Enter the list of all the shoe sizes : ").split()))
    N = int(input("Enter the number of customers : "))

    total = 0

    for i in range(N):
        size, price = map(int, input("Enter the shoe size and the price : ").split())
        if shoe_sizes[size] > 0:
            total += price
            shoe_sizes[size] -= 1

    print(total)

# ==================================================
# EXERCISE 2 : DefaultDict Tutorial
# ==================================================


# ==================================================
# EXERCISE 3 : 
# ==================================================

# ==================================================
# EXERCISE 4 : 
# ==================================================

# ==================================================
# EXERCISE 5 : 
# ==================================================


# ==================================================
# EXERCISE 6 : 
# ==================================================


# ==================================================
# EXERCISE 7 : 
# ==================================================


# ==================================================
# EXERCISE 8 : 
# ==================================================


# ==================================================
# MAIN MENU
# ==================================================

def main():
    while True:
        print("\n================================")
        print("COLLECTIONS")
        print("================================")
        print("1. collections.Counter()")
        print("2. DefaultDict Tutorial")
        # print("3. ")
        # print("4. ")
        # print("5. ")
        # print("6. ")
        # print("7. ")
        # print("8. ")
        print("0. Exit")
        print("================================")

        choice = input("Choose an exercise: ")

        if choice == "1":
            shoe_counter()

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

        # elif choice == "7":
        #     tuples()

        # elif choice == "8":
        #     tuples()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()