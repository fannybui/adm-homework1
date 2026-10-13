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
# EXERCISE 14 : 
# ==================================================


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
        print("7. Text Alignment")
        print("8. Text Wrap")
        # print("9. ")
        # print("10. ")
        # print("11. ")
        # print("12. ")
        # print("13. ")
        # print("14. ")
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

        # elif choice == "9":
            # tuples()

        # elif choice == "10":
            # tuples()

        # elif choice == "11":
            # tuples()

        # elif choice == "12":
            # tuples()

        # elif choice == "13":
            # tuples()

        # elif choice == "14":
            # tuples()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()