# ==================================================
# EXERCISE 1 : Recursive Digit Sum
# ==================================================

import math
import os
import random
import re
import sys

def superDigit(n, k):
    total = sum(int(digit) for digit in n) * k

    while total >= 10:
        total = sum(int(digit) for digit in str(total))

    return total

def f_superDigit():
    first_multiple_input = input("Enter integer n and k : ").rstrip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])
    result = superDigit(n, k)
    print(result)

# ==================================================
# MAIN MENU
# ==================================================

def main():
    while True:
        print("\n================================")
        print("Recursive Digit Sum")
        print("================================")
        print("1. Recursive Digit Sum")
        print("0. Exit")
        print("================================")

        choice = input("Choose an exercise: ")

        if choice == "1":
            f_superDigit()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()