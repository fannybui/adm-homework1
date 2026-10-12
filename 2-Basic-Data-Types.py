
# ==================================================
# EXERCISE 1 : List Comprehensions
# ==================================================

def list_comprehensions():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    L = []

    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):

                if i + j + k != n:
                    coordonnee = [i, j, k]
                    L.append(coordonnee)

    print(L)

# ==================================================
# EXERCISE 2 : Find the Runner-Up Score!
# ==================================================

def runner_up():
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    arr = sorted(set(arr))
    print(arr[-2])


# ==================================================
# EXERCISE 3 : Nested Lists
# ==================================================

def nested_lists(): 
    L = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        L.append([name, score])

    notes = []
    for eleve in L:
        notes.append(eleve[1])
    notes = sorted(set(notes))
    deuxieme_note = notes[1]

    noms = []
    for eleve in L:
        if eleve[1] == deuxieme_note:
            noms.append(eleve[0])
    noms.sort()

    for nom in noms:
        print(nom)

# ==================================================
# EXERCISE 4 : Finding the percentage
# ==================================================

def percentage():
    n = int(input("Number of students between 2 and 10: "))
    student_marks = {}
    for _ in range(n):
        name, *line = input("Student name and marks separated by space (marks between 0 and 100, 3 marks per student): ").split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input("Student name for which we want to compute the mean : ")
    notes = student_marks[query_name]
    average = sum(notes) / len(notes)
    print(f"{average:.2f}")

# ==================================================
# EXERCISE 5 : Lists
# ==================================================

def lists():
    N = int(input("Number of commands: "))
    L = []
    for _ in range(N):
        command = input().split()
        if command[0] == "insert":
            L.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(L)
        elif command[0] == "remove":
            L.remove(int(command[1]))
        elif command[0] == "append":
            L.append(int(command[1]))
        elif command[0] == "sort":
            L.sort()
        elif command[0] == "pop":
            L.pop()
        elif command[0] == "reverse":
            L.reverse()

# ==================================================
# EXERCISE 6 : Tuples
# ==================================================

def tuples():
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))

# def tuples_python2():
#     n = int(raw_input())
#     integer_list = map(int, raw_input().split())
#     t = tuple(integer_list)
#     print(hash(t))

# ==================================================
# MAIN MENU
# ==================================================

def main():
    while True:
        print("\n================================")
        print("BASIC DATA TYPES")
        print("================================")
        print("1. List Comprehensions")
        print("2. Find the Runner-Up Score!")
        print("3. Nested Lists")
        print("4. Finding the percentage")
        print("5. Lists")
        print("6. Tuples")
        print("0. Exit")
        print("================================")

        choice = input("Choose an exercise: ")

        if choice == "1":
            list_comprehensions()

        elif choice == "2":
            runner_up()

        elif choice == "3":
            nested_lists()

        elif choice == "4":
            percentage()

        elif choice == "5":
            lists()

        elif choice == "6":
            tuples()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()