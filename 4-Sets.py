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

def no_idea():
    n, m = map(int, input("Enter integers n and m separated by a space : ").split())
    array = list(map(int, input("Enter the n numbers separated by a space that will allow you to grade your happiness : ").split()))
    A = set(map(int, input("Enter the m numbers that you like : ").split()))
    B = set(map(int, input("Enter the m numbers that you dislike : ").split()))

    happiness = 0

    for nb in array:
        if nb in A:
            happiness += 1
        elif nb in B:
            happiness -= 1

    print(happiness)

# ==================================================
# EXERCISE 3 : Symmetric Difference
# ==================================================

def sym_diff():
    m = int(input("Enter integer m : "))
    list_m = set(map(int, input("Enter list of m integers : ").split()))
    n = int(input("Enter integer n : "))
    list_n = set(map(int, input("Enter list of n integers : ").split()))

    result = set()

    for number in list_m:
        if number not in list_n:
            result.add(number)
            
    for number in list_n:
        if number not in list_m:
            result.add(number)

    result = sorted(result)

    for number in result:
        print(number)

# ==================================================
# EXERCISE 4 : Set .add()
# ==================================================

def country_stamps():
    n = int(input("Enter the total number of stamps : "))
    countries = set()
    for i in range(n):
        name = input("Enter the name of a country : ")
        countries.add(name)
    print(len(countries))

# ==================================================
# EXERCISE 5 : Set .discard(), .remove() & .pop()
# ==================================================

def commands():
    n = int(input("Enter the integer n : "))
    s = set(map(int, input("Enter the list of n integers between 0 and 9 : ").split()))
    N = int(input("Enter the number of commands : "))

    for i in range(N):
        command = input("Enter the command followed by a number : ").split()

        if command[0] == "pop":
            s.pop()
        elif command[0] == "remove":
            value = int(command[1]) 
            if value in s: 
                s.remove(value)
        elif command[0] == "discard":
            s.discard(int(command[1]))

    print(sum(s))

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
        print("SETS")
        print("================================")
        print("1. Introduction to Sets")
        print("2. No Idea!")
        print("3. Symmetric Difference")
        print("4. Set .add()")
        print("5. Set .discard(), .remove() & .pop()")
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

        elif choice == "2":
            no_idea()

        elif choice == "3":
            sym_diff()

        elif choice == "4":
            country_stamps()

        elif choice == "5":
            commands()

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