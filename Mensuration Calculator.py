import math

# Define functions to calculate parameters and areas
def calculate_circle_parameter(radius):
    parameter = 2 * math.pi * radius
    print("Parameter of Circle:", parameter)

def calculate_rectangle_parameter(height, width):
    parameter = 2 * (height + width)
    print("Parameter of Rectangle:", parameter)

def calculate_square_parameter(side):
    parameter = 4 * side
    print("Parameter of Square:", parameter)

def calculate_circle_area(radius):
    area = math.pi * radius * radius
    print("Area of Circle:", area)

def calculate_rectangle_area(height, width):
    area = height * width
    print("Area of Rectangle:", area)

def calculate_square_area(side):
    area = side * side
    print("Area of Square:", area)

# Print welcome message
print("Welcome To My Mensuration Program")

# Main menu loop
while True:
    print("\nMAIN MENU")
    print("1. Calculate Parameter")
    print("2. Calculate Area")
    print("3. Exit")
    choice1 = input("Enter the Choice:")

    if choice1 == "1":
        print("\nCALCULATE PARAMETER")
        print("1. Circle")
        print("2. Rectangle")
        print("3. Square")
        print("4. Exit")
        choice2 = input("Enter the Choice:")

        if choice2 == "1":
            radius = float(input("Enter Radius of Circle:"))
            calculate_circle_parameter(radius)

        elif choice2 == "2":
            height = float(input("Enter Height of Rectangle:"))
            width = float(input("Enter Width of Rectangle:"))
            calculate_rectangle_parameter(height, width)

        elif choice2 == "3":
            side = float(input("Enter Side of Square:"))
            calculate_square_parameter(side)

        elif choice2 == "4":
            break

        else:
            print("Oops! Incorrect Choice.")

    elif choice1 == "2":
        print("\nCALCULATE AREA")
        print("1. Circle")
        print("2. Rectangle")
        print("3. Square")
        print("4. Exit")
        choice3 = input("Enter the Choice:")

        if choice3 == "1":
            radius = float(input("Enter Radius of Circle:"))
            calculate_circle_area(radius)

        elif choice3 == "2":
            height = float(input("Enter Height of Rectangle:"))
            width = float(input("Enter Width of Rectangle:"))
            calculate_rectangle_area(height, width)

        elif choice3 == "3":
            side = float(input("Enter Side of Square:"))
            calculate_square_area(side)

        elif choice3 == "4":
            break

        else:
            print("Incorrect Choice.")

    elif choice1 == "3":
        break

    else:
        print("Incorrect Choice.")
