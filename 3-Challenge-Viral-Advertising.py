# ==================================================
# EXERCISE 1 : Viral Advertising
# ==================================================

import math
import os
import random
import re
import sys

def viralAdvertising(n):
    
    shared = 5
    cumulative_likes = 0

    for day in range(n):
        liked = shared // 2
        cumulative_likes += liked
        shared = liked * 3

    return cumulative_likes

def f_viralAdvertising():
    n = int(input().strip())
    result = viralAdvertising(n)
    print(result)

# ==================================================
# MAIN MENU
# ==================================================

def main():
    while True:
        print("\n================================")
        print("Viral Advertising")
        print("================================")
        print("1. Viral Advertising")
        print("0. Exit")
        print("================================")

        choice = input("Choose an exercise: ")

        if choice == "1":
            f_viralAdvertising()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()