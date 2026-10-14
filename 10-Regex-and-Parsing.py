# ==================================================
# EXERCISE 1 : Detect Floating Point Number
# ==================================================

def floating_number():
    T = int(input("Enter T the number of test cases : "))

    for _ in range(T):
        N = input("Enter a string : ")

        try:
            float(N)

            if '.' in N and N.count('.') == 1:
                if N.replace('.', '').replace('+', '').replace('-', '').isdigit():
                    print(True)
                else:
                    print(False)
            else:
                print(False)

        except ValueError:
            print(False)

# ==================================================
# EXERCISE 2 : Re.split()
# ==================================================

import re

def split(): 
    regex_pattern = r"[,.]"	# Do not delete 'r'.
    print("\n".join(re.split(regex_pattern, input("Enter a string only of digits 0-9, commas ,, and dots . : "))))

# ==================================================
# EXERCISE 3 : Group(), Groups() & Groupdict()
# ==================================================

import re

def first_occurrence():
    S = input("Enter a string : ")

    result = re.search(r'([a-zA-Z0-9])\1', S)

    if result:
        print(result.group(1))
    else:
        print(-1)


# ==================================================
# EXERCISE 4 : Re.findall() & Re.finditer()
# ==================================================

import re

def find_pattern():
    S = input("Enter a string : ")

    pattern = r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])[AEIOUaeiou]{2,}(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])'

    result = re.findall(pattern, S)

    if result:
        print(*result, sep='\n')
    else:
        print(-1)


# ==================================================
# EXERCISE 5 : Re.start() & Re.end()
# ==================================================

import re

def search_string():

    S = input("Enter a string : ")
    k = input("Enter the substring that you are looking for : ")

    matches = list(re.finditer(f'(?={k})', S))

    if matches:
        for match in matches:
            start = match.start()
            end = start + len(k) - 1
            print((start, end))
    else:
        print((-1, -1))

# ==================================================
# EXERCISE 6 : Regex Substitution
# ==================================================

import re

def regex_substitution():

    N = int(input("Enter the number of lines of your text : "))

    for _ in range(N):
        line = input()
        line = re.sub(r'(?<= )&&(?= )', 'and', line)
        line = re.sub(r'(?<= )\|\|(?= )', 'or', line)
        print(line)

# ==================================================
# EXERCISE 7 : Validating Roman Numerals
# ==================================================

import re

def roman_numeral():
    regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"  # Do not delete 'r'.
    print(str(bool(re.match(regex_pattern, input("Enter a string : ")))))

# ==================================================
# EXERCISE 8 : Validating phone numbers
# ==================================================

import re

def valid_phone_number():
    
    N = int(input("Enter N the number of phone numbers that you want to check : "))

    regex_pattern = r'^[789][0-9]{9}$'

    for _ in range(N):
        number = input("Enter a phone number : ")

        if re.match(regex_pattern, number):
            print("YES")
        else:
            print("NO")

# ==================================================
# EXERCISE 9 : Validating and Parsing Email Addresses
# ==================================================

import re
from email.utils import parseaddr, formataddr

def valid_email():

    n = int(input("Enter n the number of email addresses : "))

    pattern = r'^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'

    for _ in range(n):
        line = input("Enter the following format => name <user@email.com> :")
        name, email = parseaddr(line)

        if re.match(pattern, email):
            print(formataddr((name, email)))

# ==================================================
# EXERCISE 10 : Hex Color Code
# ==================================================

import re

def HEX_colorcode(): 

    n = int(input("Enter the number of code lines : "))
    inside = False

    for _ in range(n):
        line = input("Enter the CSS code: ")

        if '{' in line:
            inside = True
            continue

        if '}' in line:
            inside = False
            continue

        if inside:
            colors = re.findall(r'#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?\b', line)
            for color in colors:
                print(color)

# ==================================================
# EXERCISE 11 : HTML Parser - Part 1
# ==================================================

def html_parser_1():



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
# EXERCISE 15 : 
# ==================================================



# ==================================================
# MAIN MENU
# ==================================================

def main():
    while True:
        print("\n================================")
        print("REGEX AND PARSING")
        print("================================")
        print("1. Detect Floating Point Number")
        print("2. Re.split()")
        print("3. Group(), Groups() & Groupdict()")
        print("4. Re.findall() & Re.finditer()")
        print("5. Re.start() & Re.end()")
        print("6. Regex Substitution")
        print("7. Validating Roman Numerals")
        print("8. Validating phone numbers")
        print("9. Validating and Parsing Email Addresses")
        print("10. Hex Color Code")
        print("11. HTML Parser - Part 1")
        # print("12. ")
        # print("13. ")
        # print("14. ")
        # print("15. ")
        print("0. Exit")
        print("================================")

        choice = input("Choose an exercise: ")

        if choice == "1":
            floating_number()

        elif choice == "2":
            split()

        elif choice == "3":
            first_occurrence()

        elif choice == "4":
            find_pattern()

        elif choice == "5":
            search_string()

        elif choice == "6":
            regex_substitution()

        elif choice == "7":
            roman_numeral()

        elif choice == "8":
            valid_phone_number()

        elif choice == "9":
            valid_email()

        elif choice == "10":
            HEX_colorcode()

        elif choice == "11":
            html_parser_1()

        # elif choice == "12":
        #     tuples()

        # elif choice == "13":
        #     tuples()

        # elif choice == "14":
        #     tuples()

        # elif choice == "15":
        #     tuples()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()