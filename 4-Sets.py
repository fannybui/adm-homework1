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
# EXERCISE 6 : Set .union() Operation
# ==================================================

def union_op():
    n = int(input("Enter an integer n : "))
    english = set(map(int, input("Enter a list of n integers separated by a space : ").split()))
    b = int(input("Enter an integer b : "))
    french = set(map(int, input("Enter a list of b integers separated by a space : ").split()))

    students = english.union(french)
    print(len(students))

# ==================================================
# EXERCISE 7 : Set .intersection() Operation
# ==================================================

def intersection_op():
    n = int(input("Enter an integer n : "))
    english = set(map(int, input("Enter a list of n integers separated by a space : ").split()))
    b = int(input("Enter an integer b : "))
    french = set(map(int, input("Enter a list of b integers separated by a space : ").split()))

    students = english.intersection(french)
    print(len(students))

# ==================================================
# EXERCISE 8 : Set .difference() Operation
# ==================================================

def difference_op():
    n = int(input("Enter an integer n : "))
    english = set(map(int, input("Enter a list of n integers separated by a space : ").split()))
    b = int(input("Enter an integer b : "))
    french = set(map(int, input("Enter a list of b integers separated by a space : ").split()))

    students = english.difference(french)
    print(len(students))

# ==================================================
# EXERCISE 9 : Set .symmetric_difference() Operation
# ==================================================

def symmetric_difference_op():
    n = int(input("Enter an integer n : "))
    english = set(map(int, input("Enter a list of n integers separated by a space : ").split()))
    b = int(input("Enter an integer b : "))
    french = set(map(int, input("Enter a list of b integers separated by a space : ").split()))

    students = english.symmetric_difference(french)
    print(len(students))


# ==================================================
# EXERCISE 10 : Set Mutations
# ==================================================

def mut():
    n = int(input("Enter the number n of elements in the set A : "))
    A = set(map(int, input("Enter the n elements of the set A : ").split()))
    N = int(input("Enter the number N of operations : "))

    for i in range(N):
        command = input("Enter the operation followed the length of the other set : ").split()
        operation = command[0]

        B = set(map(int, input("Enter the elements of the other set : ").split()))

        if operation == "update":
            A.update(B)

        elif operation == "intersection_update":
            A.intersection_update(B)

        elif operation == "difference_update":
            A.difference_update(B)

        elif operation == "symmetric_difference_update":
            A.symmetric_difference_update(B)

    print(sum(A))

# ==================================================
# EXERCISE 11 : The Captain's Room
# ==================================================

def captain_room():
    K = int(input("Enter integer K : "))
    rooms = list(map(int, input("Enter room numbers : ").split()))
    unique_rooms = set(rooms)
    captain_room = (sum(unique_rooms) * K - sum(rooms)) // (K - 1)
    print(captain_room)

# ==================================================
# EXERCISE 12 : Check Subset
# ==================================================

def check_subset():
    T = int(input("Enter the number T of test cases : "))

    for i in range(T):
        n = int(input("Enter the number n of elements in set A : "))
        A = set(map(int, input("Enter the n elements of set A : ").split()))
        m = int(input("Enter the number m of elements in set B : "))
        B = set(map(int, input("Enter the m elements of set B : ").split()))
        result = True
        for element in A: 
            if element not in B: 
                result = False 
                break
        print(result)


# ==================================================
# EXERCISE 13 : Check Strict Superset
# ==================================================

def strict_superset():
    A = set(map(int, input("Enter the elements of set A : ").split()))
    n = int(input("Enter the number n of other sets : "))
    result = True
    for i in range(n):
        B = set(map(int, input("Enter the elements of the other set : ").split()))
        for element in B:
            if element not in A:
                result = False
                break
        if len(A) <= len(B):
            result = False
        if result == False:
            break
    print(result)


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
        print("6. Set .union() Operation")
        print("7. Set .intersection() Operation")
        print("8. Set .difference() Operation")
        print("9. Set .symmetric_difference() Operation")
        print("10. Set Mutations")
        print("11. The Captain's Room")
        print("12. Check Subset")
        print("13. Check Strict Superset")
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

        elif choice == "6":
            union_op()

        elif choice == "7":
            intersection_op()

        elif choice == "8":
            difference_op()

        elif choice == "9":
            symmetric_difference_op()

        elif choice == "10":
            mut()

        elif choice == "11":
            captain_room()

        elif choice == "12":
            check_subset()

        elif choice == "13":
            strict_superset()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()