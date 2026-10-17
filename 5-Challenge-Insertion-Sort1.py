# ==================================================
# EXERCISE 1 : Insertion Sort - Part 1
# ==================================================

import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    value = arr[-1]
    i = n - 2

    while i >= 0 and arr[i] > value:
        arr[i + 1] = arr[i]
        print(*arr)
        i -= 1

    arr[i + 1] = value
    print(*arr)

def f_insertionSort1():
    n = int(input("Enter integer n : ").strip())

    arr = list(map(int, input("Enter the n elements : ").rstrip().split()))

    insertionSort1(n, arr)

# ==================================================
# MAIN MENU
# ==================================================

def main():
    while True:
        print("\n================================")
        print("Insertion Sort - Part 1")
        print("================================")
        print("1. Insertion Sort - Part 1")
        print("0. Exit")
        print("================================")

        choice = input("Choose an exercise: ")

        if choice == "1":
            f_insertionSort1()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()