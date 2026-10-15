# ==================================================
# EXERCISE 1 : Map and Lambda Function
# ==================================================

def fibonacci(n):
    fib = []
    a, b = 0, 1

    for _ in range(n):
        fib.append(a)
        a, b = b, a + b

    return fib

def fibo():
    cube = lambda x: x**3
    n = int(input("Enter an integer N : "))
    print(list(map(cube, fibonacci(n))))

# ==================================================
# MAIN MENU
# ==================================================

def main():
    while True:
        print("\n================================")
        print("MAP AND LAMBDA EXPRESSION")
        print("================================")
        print("1. Map and Lambda Function")
        print("0. Exit")
        print("================================")

        choice = input("Choose an exercise: ")

        if choice == "1":
            fibo()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()