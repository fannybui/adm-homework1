# ==================================================
# EXERCISE 1 : Birthday Cake Candles
# ==================================================

import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    tallest = max(candles)
    return candles.count(tallest)

def f_birthdayCakeCandles():
    candles_count = int(input("Enter the integer N : ").strip())

    candles = list(map(int, input("Enter the N elements space-separated : ").rstrip().split()))

    result = birthdayCakeCandles(candles)

    print (result)

# ==================================================
# MAIN MENU
# ==================================================

def main():
    while True:
        print("\n================================")
        print("Birthday Cake Candles")
        print("================================")
        print("1. Birthday Cake Candles")
        print("0. Exit")
        print("================================")

        choice = input("Choose an exercise: ")

        if choice == "1":
            f_birthdayCakeCandles()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()