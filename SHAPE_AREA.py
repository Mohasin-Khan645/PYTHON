# Menu
# 1..square of number 
# 2..Rectangle
#  3..circle
#  4..triangle
#  5..Exit
# Enter any shapes 
#  use function for this program

# n = int(input("Enter a number 0)Square\n 1)Rectangle\n 2)Circle\n 3)Triangle\n 4)Exit:\n"))
# a = int(input("Enter any shapes:"))
# if n == 0:
#     print("Square of number is:", a * a)
# elif n == 1:
#     l = int(input("Enter length:"))
#     b = int(input("Enter breadth:"))
#     print("Area of Rectangle is:", l * b)
# elif n == 2:
#     r = int(input("Enter radius:"))
#     print("Area of Circle is:", 3.14 * r * r)
# elif n == 3:
#     h = int(input("Enter height:"))
#     b = int(input("Enter base:"))
#     print("Area of Triangle is:", 0.5 * b * h)
# elif n == 4:
#     print("Exit")


import math

def square():
    side = float(input("Enter side of square: "))
    area = side * side
    print(f"Area of Square = {area:.2f}")


def rectangle():
    length = float(input("Enter length of rectangle: "))
    breadth = float(input("Enter breadth of rectangle: "))
    area = length * breadth
    print(f"Area of Rectangle = {area:.2f}")

def circle():
    radius = float(input("Enter radius of circle: "))
    area = math.pi * radius * radius
    print(f"Area of Circle = {area:.2f}")


def triangle():
    base = float(input("Enter base of triangle: "))
    height = float(input("Enter height of triangle: "))
    area = 0.5 * base * height
    print(f"Area of Triangle = {area:.2f}")


def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Square")
        print("2. Rectangle")
        print("3. Circle")
        print("4. Triangle")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            square()
        elif choice == '2':
            rectangle()
        elif choice == '3':
            circle()
        elif choice == '4':
            triangle()
        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please enter between 1-5.")
menu()




