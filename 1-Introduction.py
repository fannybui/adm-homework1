
# ==================================================
# EXERCISE 1 : Say Hello, World! With Python
# ==================================================

def hello_world():
    print("Hello, World!")


# ==================================================
# EXERCISE 2 : Python If-Else
# ==================================================

import math
import os
import random
import re
import sys

def weird_or_not():
    n = int(input("Enter an integer between 1 and 100 : "))

    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")


# ==================================================
# EXERCISE 3 : Arithmetic Operators
# ==================================================

def arithmetic_operations():
    a = int(input("Enter the first positive integer: "))
    b = int(input("Enter the second positive integer: "))

    print(a + b)
    print(a - b)
    print(a * b)


# ==================================================
# EXERCISE 4 : Python: Division
# ==================================================

def division():
    a = int(input("Enter the first integer: "))
    b = int(input("Enter the second non-null integer: "))

    if b != 0:
        print(a // b)
        print(a / b)
    else:
        print("Division by zero is not allowed.")


# ==================================================
# EXERCISE 5 : Loops
# ==================================================

def print_squares():
    n = int(input("Enter a integer between 1 and 20 : "))

    for i in range(n):
        print(i ** 2)


# ==================================================
# EXERCISE 6 : Write a function
# ==================================================

def is_leap(year):
    leap = False
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    else:
        leap = False
    return leap


def check_leap_year():
    year = int(input("Enter a year above 1900: "))
    print(is_leap(year))


# ==================================================
# EXERCISE 7 : Print Function
# ==================================================

def print_consecutive_numbers():
    n = int(input("Enter a integer between 1 and 150 : "))

    for i in range(1, n + 1):
        print(i, end="")

    print()

# ==================================================
# MAIN MENU
# ==================================================

def main():
    while True:
        print("\n================================")
        print("INTRODUCTION")
        print("================================")
        print("1. Say Hello, World! With Python")
        print("2. Python If-Else")
        print("3. Arithmetic Operators")
        print("4. Python: Division")
        print("5. Loops")
        print("6. Write a function")
        print("7. Print Function")
        print("0. Exit")
        print("================================")

        choice = input("Choose an exercise: ")

        if choice == "1":
            hello_world()

        elif choice == "2":
            weird_or_not()

        elif choice == "3":
            arithmetic_operations()

        elif choice == "4":
            division()

        elif choice == "5":
            print_squares()

        elif choice == "6":
            check_leap_year()

        elif choice == "7":
            print_consecutive_numbers()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()