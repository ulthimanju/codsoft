# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero!"
    else:
        return num1 / num2

# Main program
def main():
    print("Welcome to Simple Calculator!")

    # Input numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Select operation
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. All")

    choice = input("\nEnter choice (1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4', '5'):
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == '5':
            print(f"{num1} + {num2} = {add(num1, num2)}")
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input. Please choose a valid operation.")

if __name__ == "__main__":
    main()
