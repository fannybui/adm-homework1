# ==================================================
# EXERCISE 1 : Zipped!
# ==================================================

def average_marks():

    N, X = map(int, input("Enter the number of students N and the number of subjects X : ").split())

    subjects = []

    for _ in range(X):
        subjects.append(list(map(float, input("Enter the contains the space separated marks obtained by each of the N student : ").split())))

    for student_scores in zip(*subjects):
        print(sum(student_scores) / X)

# ==================================================
# EXERCISE 2 : Athlete Sort
# ==================================================

import math
import os
import random
import re
import sys

def athlete_sort():
    first_multiple_input = input("Enter the integers N and M separated by space : ").rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input("Enter the M elements separated by space over N lines : ").rstrip().split())))

    k = int(input("Enter integer K : ").strip())

    arr.sort(key=lambda x: x[k])

    for row in arr:
        print(*row)

# ==================================================
# EXERCISE 3 : ginortS
# ==================================================

def cle_tri(c):
    return (
        c.isdigit(),
        c.isdigit() and int(c) % 2 == 0,
        c.isupper(),
        c
    )

def sorting():
    s = input("Enter the string S : ")
    resultat = ''.join(sorted(s, key=cle_tri))
    print(resultat)

# ==================================================
# MAIN MENU
# ==================================================

def main():
    while True:
        print("\n================================")
        print("BUILT-INS")
        print("================================")
        print("1. Zipped!")
        print("2. Athlete Sort")
        print("3. ginortS")
        print("0. Exit")
        print("================================")

        choice = input("Choose an exercise: ")

        if choice == "1":
            average_marks()

        elif choice == "2":
            athlete_sort()

        elif choice == "3":
            sorting()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()