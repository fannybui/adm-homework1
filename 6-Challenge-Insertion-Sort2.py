# ==================================================
# EXERCISE 1 : Insertion Sort - Part 2
# ==================================================

import math
import os
import random
import re
import sys

def insertionSort2(n, arr):
    for i in range(1, n):
        value = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > value:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = value
        print(*arr)

def f_insertionSort2():
    n = int(input("Enter the integer n : ").strip())
    arr = list(map(int, input("Enter the n elements : ").rstrip().split()))
    insertionSort2(n, arr)


# ==================================================
# MAIN MENU
# ==================================================

def main():
    while True:
        print("\n================================")
        print("Insertion Sort - Part 2")
        print("================================")
        print("1. Insertion Sort - Part 2")
        print("0. Exit")
        print("================================")

        choice = input("Choose an exercise: ")

        if choice == "1":
            f_insertionSort2()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()