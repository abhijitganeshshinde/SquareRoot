import math

def calculate_square_root(number):
    if number < 0:
        return "Error: Cannot calculate square root of a negative number."
    else:
        return math.sqrt(number)

if __name__ == "__main__":
    try:
        num = float(input("Enter a number: "))
        result = calculate_square_root(num)
        print("Square root:", result)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
