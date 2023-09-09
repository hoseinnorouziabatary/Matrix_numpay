from time import sleep
import numpy as np

A = []
B = []


def input_matrix(variable_name):
    global A, B

    R = int(input("Enter the number of rows:"))
    C = int(input("Enter the number of columns:"))

    print("Enter the entries in a single line (separated by space): ")

    entries = list(map(int, input().split()))

    # For printing the matrix
    if variable_name == 'A':
        A = np.array(entries).reshape(R, C)
    else:
        B = np.array(entries).reshape(R, C)


def print_matrix(variable_name):
    print(variable_name)
    return


def multiply_constant():
    global A
    constant = input("Enter constant value:")
    if not constant.isdigit():
        print("Please enter valid number")
        return
    if len(A) == 0:
        print("Can not multiply constant these matrixes!")
        return
    constant = int(constant)

    A = np.multiply(A, constant)


def add():
    global A, B
    if len(A) == 0 or len(B) == 0:
        print("Can not add these matrixes!")
        return

    A = np.add(A, B)


def minus():
    global A, B
    if len(A) == 0 or len(B) == 0:
        print("Can not minus these matrixes!")
        return

    A = np.subtract(A, B)


def multiply():
    global A, B
    if len(A) == 0 or len(B) == 0:
        print("Can not multiply these matrixes!")
        return

    A = np.multiply(A, B)


def divide():
    global A, B
    if len(A) == 0 or len(B) == 0:
        print("Can not divide these matrixes!")
        return

    A = np.divide


def determinant_matrix(variable_name):
    global A, B

    if len(A) == 0 or len(B) == 0:
        print("You cannot do determinants!")
        return
    determinant = np.linalg.det(variable_name)
    print(determinant)


option_mapping = {
    1:  input_matrix('A'),
    2:  input_matrix('B'),
    3:  globals().__setitem__('A', B),
    4:  globals().__setitem__('B', A),
    5: multiply,
    6: add,
    7: divide,
    8: minus,
    9: multiply_constant,
    10:  determinant_matrix(A),
    11:  determinant_matrix(B),
    12:  print_matrix(A),
    13:  print_matrix(B)
}


if __name__ == '__main__':
    while True:
        option: str = (
            input(
"""Select an option:
    1. Get Matrix A
    2. Get Matrix B
    3. Move B to A
    4. Move A to B
    5. Calculate A = A * B
    6. Calculate A = A + B
    7. Calculate A = A / B
    8. Calculate A = A - B
    9. Calculate A = a * A
    10. Determinant of A
    11. Determinant of B
    12. Print A
    13. Print B
    14. Close
= """))
        if not option.isdigit():
            print("Select a valid number")
            continue
        option = int(option)
        if option > 14 or option < 1:
            print("Select option between 1 and 14")
            continue

        if option == 14:
            print("See you soon. Bye :)")
            break

        option_mapping[option]()

        sleep(1)
