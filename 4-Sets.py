# ==================================================
# EXERCISE 1 : Introduction to Sets
# ==================================================

def average(array):
    unique = set(array)

    total = sum(unique)
    number_of_heights = len(unique)

    result = total / number_of_heights

    return result

def f_average():
    n = int(input("Enter an integer N : "))
    arr = list(map(int, input("Enter the N space-separated integers : ").split()))
    result = average(arr)
    print(result)

# ==================================================
# EXERCISE 2 : No Idea!
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
# EXERCISE 9 : 
# ==================================================


# ==================================================
# EXERCISE 10 : 
# ==================================================

# ==================================================
# EXERCISE 11 : 
# ==================================================


# ==================================================
# EXERCISE 12 : 
# ==================================================


# ==================================================
# EXERCISE 13 : 
# ==================================================


# ==================================================
# MAIN MENU
# ==================================================

def main():
    while True:
        print("\n================================")
        print("STRINGS")
        print("================================")
        print("1. Introduction to Sets")
        print("2. No Idea!")
        # print("3. ")
        # print("4. ")
        # print("5. ")
        # print("6. ")
        # print("7. ")
        # print("8. ")
        # print("9. ")
        # print("10. ")
        # print("11. ")
        # print("12. ")
        # print("13. ")
        print("0. Exit")
        print("================================")

        choice = input("Choose an exercise: ")

        if choice == "1":
            f_average()

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

        # elif choice == "9":
        #     tuples()

        # elif choice == "10":
        #     tuples()

        # elif choice == "11":
        #     tuples()

        # elif choice == "12":
        #     tuples()

        # elif choice == "13":
        #     tuples()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()