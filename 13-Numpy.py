# ==================================================
# EXERCISE 1 : Arrays
# ==================================================

import numpy

def arrays(arr):
    return numpy.array(arr, dtype=float)[::-1]

def f_arrays():
    arr = input("Enter the space separated numbers : ").strip().split(' ')
    result = arrays(arr)
    print(result)

# ==================================================
# EXERCISE 2 : Shape and Reshape
# ==================================================

import numpy

def convert_array():
    arr = numpy.array(input("Enter the 9 space separated integers : ").split(), dtype=int)
    print(numpy.reshape(arr, (3, 3)))

# ==================================================
# EXERCISE 3 : Transpose and Flatten
# ==================================================

import numpy

def transpose_flatten():

    n, m = map(int, input("Enter the integer N and M separated by space : ").split())

    arr = numpy.array([input("Enter the N x M space separated values : ").split() for _ in range(n)], dtype=int)

    print(numpy.transpose(arr))
    print(arr.flatten())

# ==================================================
# EXERCISE 4 : Concatenate
# ==================================================


import numpy

def concatenate():

    n, m, p = map(int, input("Enter the integers N, M and P : ").split())

    array_1 = numpy.array([input("Enter the N lines of P elements : ").split() for _ in range(n)], dtype=int)
    array_2 = numpy.array([input("Enter the M lines of P elements : ").split() for _ in range(m)], dtype=int)

    print(numpy.concatenate((array_1, array_2), axis=0))


# ==================================================
# EXERCISE 5 : Zeros and Ones
# ==================================================

import numpy

def zero_one_matrix(): 
    shape = tuple(map(int, input("Enter the 3 space-separated integers : ").split()))

    print(numpy.zeros(shape, dtype=int))
    print(numpy.ones(shape, dtype=int))

# ==================================================
# EXERCISE 6 : Eye and Identity
# ==================================================

import numpy

def eye_identity():

    numpy.set_printoptions(legacy='1.13')

    n, m = map(int, input("Enter integers N and M : ").split())

    print(numpy.eye(n, m))



# ==================================================
# EXERCISE 7 : Array Mathematics
# ==================================================


import numpy

def operations():

    n, m = map(int, input("Enter integers N and M : ").split())

    A = numpy.array([input("Enter the N integers space separated integers of array A : ").split() for _ in range(n)], dtype=int)
    B = numpy.array([input("Enter the N integers space separated integers of array B : ").split() for _ in range(n)], dtype=int)

    print(A + B)
    print(A - B)
    print(A * B)
    print(numpy.floor_divide(A, B))
    print(A % B)
    print(A ** B)


# ==================================================
# EXERCISE 8 : Floor, Ceil and Rint
# ==================================================


import numpy

def floor_ceil_rint():

    numpy.set_printoptions(legacy='1.13')

    A = numpy.array(input("Enter the space separated elements of array A : ").split(), dtype=float)

    print(numpy.floor(A))
    print(numpy.ceil(A))
    print(numpy.rint(A))


# ==================================================
# EXERCISE 9 : Sum and Prod
# ==================================================

import numpy

def sum_prod(): 

    n, m = map(int, input("Enter the N and M integers space separated : ").split())

    arr = numpy.array([input("Enter M space separated integers over N lines : ").split() for _ in range(n)], dtype=int)

    sum_axis = numpy.sum(arr, axis=0)

    print(numpy.prod(sum_axis))


# ==================================================
# EXERCISE 10 : Min and Max
# ==================================================


import numpy

def min_max():
    n, m = map(int, input("Enter the N and M integers space separated : ").split())

    arr = numpy.array([input("Enter M space separated integers over N lines : ").split() for _ in range(n)], dtype=int)

    min_axis = numpy.min(arr, axis=1)

    print(numpy.max(min_axis))


# ==================================================
# EXERCISE 11 : Mean, Var, and Std
# ==================================================


import numpy

def mean_var_std():

    n, m = map(int, input("Enter the N and M integers space separated : ").split())

    arr = numpy.array([input("Enter M space separated integers over N lines : ").split() for _ in range(n)], dtype=int)

    print(numpy.mean(arr, axis=1))
    print(numpy.var(arr, axis=0))
    print(round(numpy.std(arr), 11))


# ==================================================
# EXERCISE 12 : Dot and Cross
# ==================================================

import numpy

def dot_cross():

    n = int(input("Enter integer N : "))

    A = numpy.array([input("Enter N space separated integers over N lines for matrix A : ").split() for _ in range(n)], dtype=int)
    B = numpy.array([input("Enter N space separated integers over N lines for matrix A : ").split() for _ in range(n)], dtype=int)

    print(numpy.dot(A, B))


# ==================================================
# EXERCISE 13 : Inner and Outer
# ==================================================

import numpy

def inner_outer():

    A = numpy.array(input("Enter the space separated elements of array A : ").split(), dtype=int)
    B = numpy.array(input("Enter the space separated elements of array B : ").split(), dtype=int)

    print(numpy.inner(A, B))
    print(numpy.outer(A, B))


# ==================================================
# EXERCISE 14 : Polynomials
# ==================================================

import numpy

def polynomials():

    P = list(map(float, input("Enter the space separated value of the coefficients in P : ").split()))
    x = float(input("Enter the value of x : "))

    print(numpy.polyval(P, x))


# ==================================================
# EXERCISE 15 : Linear Algebra
# ==================================================

import numpy

def linear_algebra():

    n = int(input("Enter integer N : "))

    A = numpy.array([input("Enter the N space separated elements of array A : ").split() for _ in range(n)], dtype=float)

    print(round(numpy.linalg.det(A), 2))

# ==================================================
# MAIN MENU
# ==================================================

def main():
    while True:
        print("\n================================")
        print("NUMPY")
        print("================================")
        print("1. Arrays")
        print("2. Shape and Reshape")
        print("3. Transpose and Flatten")
        print("4. Concatenate")
        print("5. Zeros and Ones")
        print("6. Eye and Identity")
        print("7. Array Mathematics")
        print("8. Floor, Ceil and Rint")
        print("9. Sum and Prod")
        print("10. Min and Max")
        print("11. Mean, Var, and Std")
        print("12. Dot and Cross")
        print("13. Inner and Outer")
        print("14. Polynomials")
        print("15. Linear Algebra")
        print("0. Exit")
        print("================================")

        choice = input("Choose an exercise: ")

        if choice == "1":
            f_arrays()

        elif choice == "2":
            convert_array()

        elif choice == "3":
            transpose_flatten()

        elif choice == "4":
            concatenate()

        elif choice == "5":
            zero_one_matrix()

        elif choice == "6":
            eye_identity()

        elif choice == "7":
            operations()

        elif choice == "8":
            floor_ceil_rint()

        elif choice == "9":
            sum_prod()

        elif choice == "10":
            min_max()

        elif choice == "11":
            mean_var_std()

        elif choice == "12":
            dot_cross()

        elif choice == "13":
            inner_outer()

        elif choice == "14":
            polynomials()

        elif choice == "15":
            linear_algebra()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()