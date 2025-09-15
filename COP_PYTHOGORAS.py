import math


def check_coprime(a, b):
    if math.gcd(a, b) == 1:
        print(f"{a} and {b} are Co-Prime numbers")
    else:
        print(f"{a} and {b} are NOT Co-Prime numbers")


def check_pythagoras(a, b, c):
    if a**2 + b**2 == c**2:
        print(f"{a}, {b}, {c} satisfy Pythagoras theorem")
    else:
        print(f"{a}, {b}, {c} do NOT satisfy Pythagoras theorem")


def main():
    print("=== Co-prime Check ===")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    check_coprime(a, b)

    print("\n=== Pythagoras Theorem Check ===")
    x = int(input("Enter first number (a): "))
    y = int(input("Enter second number (b): "))
    z = int(input("Enter third number (c): "))
    check_pythagoras(x, y, z)
main()
