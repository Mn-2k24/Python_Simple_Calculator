# built simple calculator using if else and while loop in python

# function for Additional
def Add(num1, num2):
    return num1 + num2

# function for subtract


def Sub(num1, num2):
    return num1 - num2

# function for multiply


def Mult(num1, num2):
    return num1 * num2

# function for divide


def Div(num1, num2):
    if num2 == 0:
        print("Error! Division by zero is not allowed.")
    else:
        return num1 / num2

# function for Modulus


def Mod(num1, num2):
    return num1 % num2

# function for power


def Power(num1, num2):
    return num1 ** num2


# while loop for to continue progaram
while True:
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Exit")
# user input to select operation
    choice = input("Enter Operator-(1/2/3/4/5/6/7): ")

    # checking if user input is valid
    if choice not in ("1", "2", "3", "4", "5", "6", "7"):
        print("Invalid operator! Please select between 1 to 7.")
        continue
    # checking if user wants to exit program
    if choice == "7":
        print("\nExiting...")
        break
    # if conditions to calculate operation
    if choice in ("1", "2", "3", "4", "5", "6"):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        # if elif conditions to calculate
        if choice == "1":
            print(f"Addition: {Add(num1, num2)}")
        elif choice == "2":
            print(f"Subtraction: {Sub(num1, num2)}")
        elif choice == "3":
            print(f"Multiplication: {Mult(num1, num2)}")
        elif choice == "4":
            print(f"Division: {Div(num1, num2)}")
        elif choice == "5":
            print(f"Modulus: {Mod(num1, num2)}")
        elif choice == "6":
            print(f"Power: {Power(num1, num2)}")
        else:
            print("Invalid input! Please try again.")
