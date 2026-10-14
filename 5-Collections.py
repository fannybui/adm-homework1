# ==================================================
# EXERCISE 1 : collections.Counter()
# ==================================================
from collections import Counter

def shoe_counter():

    X = int(input("Enter the total number of shoes : "))
    shoe_sizes = Counter(map(int, input("Enter the list of all the shoe sizes : ").split()))
    N = int(input("Enter the number of customers : "))

    total = 0

    for i in range(N):
        size, price = map(int, input("Enter the shoe size and the price : ").split())
        if shoe_sizes[size] > 0:
            total += price
            shoe_sizes[size] -= 1

    print(total)

# ==================================================
# EXERCISE 2 : DefaultDict Tutorial
# ==================================================

from collections import defaultdict

def default_dict():

    n, m = map(int, input("Enter integers n and m separated by a space : ").split())
    d = defaultdict(list)

    for i in range(1, n + 1):
        word = input("Enter n words belonging to A : ")
        d[word].append(i)

    for _ in range(m):
        word = input("Enter m words belonging to B : ")
        if d[word]:
            print(*d[word])
        else:
            print(-1)


# ==================================================
# EXERCISE 3 : Collections.namedtuple()
# ==================================================

from collections import namedtuple

def collections_named():
    N = int(input("Enter N the number of students : "))
    columns = input("Enter the names of the columns : ").split()
    Student = namedtuple('Student', columns)

    total = 0

    for _ in range(N):
        student = Student(*input("Enter the student's information : ").split())
        total += int(student.MARKS)

    print(f"{total / N:.2f}")

# ==================================================
# EXERCISE 4 : Collections.OrderedDict()
# ==================================================

from collections import OrderedDict

def collections_ordered():
    N = int(input("Enter N the number of items : "))
    items = OrderedDict()

    for _ in range(N):
        name, price = input("Enter the name of the article and its price separated by space : ").rsplit(" ", 1)
        price = int(price)

        if name in items:
            items[name] += price
        else:
            items[name] = price

    for name, price in items.items():
        print(name, price)

# ==================================================
# EXERCISE 5 : Word Order
# ==================================================

from collections import OrderedDict

def word_order():
    n = int(input("Enter n the number of words : "))
    words = OrderedDict()

    for _ in range(n):
        word = input("Enter a word : ")
        if word in words:
            words[word] += 1
        else:
            words[word] = 1


    print(f"There are {len(words)} distinct words.")
    print(f"Occurrences for each distinct word: {' '.join(map(str, words.values()))}")


# ==================================================
# EXERCISE 6 : Collections.deque()
# ==================================================


from collections import deque

def collections_deque():
    d = deque()
    N = int(input("Enter N the number of operations : "))

    for _ in range(N):
        operation = input("Enter the space separated name of method and its value : ").split()

        if operation[0] == "append":
            d.append(int(operation[1]))

        elif operation[0] == "appendleft":
            d.appendleft(int(operation[1]))

        elif operation[0] == "pop":
            d.pop()

        elif operation[0] == "popleft":
            d.popleft()

    print(*d)


# ==================================================
# EXERCISE 7 : Company Logo
# ==================================================

from collections import Counter

def company_logo():
    s = input("Enter the name of a comany : ")

    counts = Counter(s)
    result = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    for char, count in result[:3]:
        print(char, count)

# ==================================================
# EXERCISE 8 : Piling Up!
# ==================================================


from collections import deque

def piling_up():
    T = int(input("Enter T the number of test cases : "))

    for _ in range(T):
        n = int(input("Enter n the number of cubes for the test case : "))
        cubes = deque(map(int, input("Enter the n separated-space integers denoting the sideLengths of each cube : ").split()))

        pile = float('inf')
        possible = True

        while cubes:
            gauche = cubes[0]
            droite = cubes[-1]

            if gauche >= droite and gauche <= pile:
                pile = cubes.popleft()
            elif droite <= pile:
                pile = cubes.pop()
            else:
                possible = False
                break

        print("Yes" if possible else "No")


# ==================================================
# MAIN MENU
# ==================================================

def main():
    while True:
        print("\n================================")
        print("COLLECTIONS")
        print("================================")
        print("1. collections.Counter()")
        print("2. DefaultDict Tutorial")
        print("3. Collections.namedtuple()")
        print("4. Collections.OrderedDict()")
        print("5. Word Order")
        print("6. Collections.deque()")
        print("7. Company Logo")
        print("8. Piling Up!")
        print("0. Exit")
        print("================================")

        choice = input("Choose an exercise: ")

        if choice == "1":
            shoe_counter()

        elif choice == "2":
            default_dict()

        elif choice == "3":
            collections_named()

        elif choice == "4":
            collections_ordered()

        elif choice == "5":
            word_order()

        elif choice == "6":
            collections_deque()

        elif choice == "7":
            company_logo()

        elif choice == "8":
            piling_up()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()