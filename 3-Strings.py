# ==================================================
# EXERCISE 1 : sWAP cASE
# ==================================================

def swap_case(s):
    string = ""
    for element in s:
        if element.islower():
            string += element.upper()
        elif element.isupper():
            string += element.lower()
        else:
            string += element
    return string

# def swap_case2(s):
#     return s.swapcase()

def f_swap_case():
    s = input("Enter a string :")
    result = swap_case(s)
    print(result)

# ==================================================
# EXERCISE 2 : String Split and Join
# ==================================================

def split_and_join(line):
    L = line.split(" ")
    result = "-".join(L)
    return result

def f_split_and_join():
    line = input("Enter a string :")
    result = split_and_join(line)
    print(result)

# ==================================================
# EXERCISE 3 : What's Your Name?
# ==================================================

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

def f_print_full_name():
    first_name = input("Enter the first name :")
    last_name = input("Enter the last name :")
    print_full_name(first_name, last_name)

# ==================================================
# EXERCISE 4 : Mutations
# ==================================================

def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]

def f_mutate_string():
    s = input("Enter a string :")
    i, c = input("Enter a position in the string and the new character :").split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# ==================================================
# EXERCISE 5 : Find a string
# ==================================================

def count_substring(string, sub_string):
    nb = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            nb += 1
    return nb

def f_count_substring():
    string = input("Enter a string :").strip()
    sub_string = input("Enter the substring :").strip()
    count = count_substring(string, sub_string)
    print(count)
 

# ==================================================
# EXERCISE 6 : String Validators
# ==================================================

# str.isalnum() : This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
# str.isalpha() : This method checks if all the characters of a string are alphabetical (a-z and A-Z).
# str.isdigit() : This method checks if all the characters of a string are digits (0-9).
# str.islower() : This method checks if all the characters of a string are lowercase characters (a-z).
# str.isupper() : This method checks if all the characters of a string are uppercase characters (A-Z).

def strings_validators():
    s = input("Enter a string :")
    
    alphanumeric = False
    alphabetical = False
    digits = False
    lowercase = False
    uppercase = False

    for c in s:
        if c.isalnum():
            alphanumeric = True
        if c.isalpha():
            alphabetical = True
        if c.isdigit():
            digits = True
        if c.islower():
            lowercase = True
        if c.isupper():
            uppercase = True

    print(alphanumeric)
    print(alphabetical)
    print(digits)
    print(lowercase)
    print(uppercase)


# ==================================================
# EXERCISE 7 : Text Alignment
# ==================================================

# .ljust(width) : This method returns a left aligned string of length width.
# .center(width) : This method returns a centered string of length width.
# .rjust(width) : This method returns a right aligned string of length width.



# ==================================================
# EXERCISE 8 : Text Wrap
# ==================================================

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

def f_wrap():
    string, max_width = input("Enter a string : "), int(input("Enter the width : "))
    result = wrap(string, max_width)
    print(result)

# ==================================================
# EXERCISE 9 : Designer Door Mat
# ==================================================

def door_mat():
    N, M = map(int, input("Enter N and M separated by space : ").split())

    for i in range(1, N, 2):
        pattern = ".|." * i
        print(pattern.center(M, "-"))

    print("WELCOME".center(M, "-"))

    for i in range(N - 2, 0, -2):
        pattern = ".|." * i
        print(pattern.center(M, "-"))

# ==================================================
# EXERCISE 10 : String Formatting
# ==================================================

def print_formatted(number):

    width = len(bin(number)[2:])

    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]

        print(decimal.rjust(width), 
              octal.rjust(width), 
              hexadecimal.rjust(width), 
              binary.rjust(width))

def f_print_formatted():
    n = int(input("Enter an integer between 1 and 99 :"))
    print_formatted(n)


# ==================================================
# EXERCISE 11 : Alphabet Rangoli
# ==================================================

def print_rangoli(size):
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    width = 4 * size - 3
    
    L=[]
    
    for i in range(size):
        right_part = alphabet[i:size]
        left_part = alphabet[size - 1:i:-1]
        letters = left_part + right_part
        line = "-".join(letters)
        line = line.center(width, "-")
        L.append(line)

    for i in range(size - 1, 0, -1):
        print(L[i])
    for line in L:
        print(line)

def f_print_rangoli():
    n = int(input())
    print_rangoli(n)

# ==================================================
# EXERCISE 12 : Capitalize!
# ==================================================


import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(name):

    L = name.split(" ")
    capitalized_names = []

    for word in L:
        capitalized = word.capitalize()
        capitalized_names.append(capitalized)

    result = " ".join(capitalized_names)

    return result

def f_solve():
    string = input("Enter a name :")
    result = solve(string)
    print(result)

# ==================================================
# EXERCISE 13 : The Minion Game
# ==================================================

def minion_game(string):
    
    kevin = 0
    stuart = 0
    vowels = "AEIOU"
    length = len(string)

    for i in range(length):
        points = length - i
        if string[i] in vowels:
            kevin += points
        else:
            stuart += points

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")

def f_minion_game():
    s = input("Enter a string in capital :")
    minion_game(s)

# ==================================================
# EXERCISE 14 : Merge the Tools!
# ==================================================

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i + k]

        result = ""

        for character in substring:
            if character not in result:
                result += character

        print(result)

def f_merge_the_tools():
    string, k = input("Enter a string (of length n) : "), int(input("Enter a integer k (where  k is a factor of n)"))
    merge_the_tools(string, k)

# ==================================================
# MAIN MENU
# ==================================================

def main():
    while True:
        print("\n================================")
        print("STRINGS")
        print("================================")
        print("1. sWAP cASE")
        print("2. String Split and Join")
        print("3. What's Your Name?")
        print("4. Mutations")
        print("5. Find a string")
        print("6. String Validators")
        # print("7. Text Alignment")
        print("8. Text Wrap")
        print("9. Designer Door Mat")
        print("10. String Formatting")
        print("11. Alphabet Rangoli")
        print("12. Capitalize!")
        print("13. The Minion Game")
        print("14. Merge the Tools!")
        print("0. Exit")
        print("================================")

        choice = input("Choose an exercise: ")

        if choice == "1":
            f_swap_case()

        elif choice == "2":
            f_split_and_join()

        elif choice == "3":
            f_print_full_name()

        elif choice == "4":
            f_mutate_string()

        elif choice == "5":
            f_count_substring()

        elif choice == "6":
            strings_validators()

        # elif choice == "7":
            # tuples()        

        elif choice == "8":
            f_wrap()

        elif choice == "9":
            door_mat()

        elif choice == "10":
            f_print_formatted()

        elif choice == "11":
            f_print_rangoli()

        elif choice == "12":
            f_solve()

        elif choice == "13":
            f_minion_game()

        elif choice == "14":
            f_merge_the_tools()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()