# ==================================================
# EXERCISE 1 : Standardize Mobile Number Using Decorators
# ==================================================

def wrapper(f):
    def fun(l):
        l = ['+91 ' + number[-10:-5] + ' ' + number[-5:] for number in l]
        f(l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

def mobile_phone():
    n = int(input("Enter n the number of phone numbers: "))
    l = [input("Enter a phone number : ") for _ in range(n)]
    sort_phone(l) 

# ==================================================
# EXERCISE 2 : Decorators 2 - Name Directory
# ==================================================

import operator

def person_lister(f):
    def inner(people):
        people.sort(key=lambda person: int(person[2]))
        return map(f, people)
    return inner
    
@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

def age_ordering():
    n = int(input("Enter n the number of people : "))
    people = [input("Enter the first name, last name, age and sex (separated by space) for each person : ").split() for i in range(n)]
    print(*name_format(people), sep='\n')

# ==================================================
# MAIN MENU
# ==================================================

def main():
    while True:
        print("\n================================")
        print("CLOSURES AND DECORATORS")
        print("================================")
        print("1. Standardize Mobile Number Using Decorators")
        print("2. Decorators 2 - Name Directory")
        print("0. Exit")
        print("================================")

        choice = input("Choose an exercise: ")

        if choice == "1":
            mobile_phone()

        elif choice == "2":
            age_ordering()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()