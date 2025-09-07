def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def main():
    print("Simple Calculator")
    while True:
        print("\nSelect operation: 1.Add 2.Subtract 3.Multiply 4.Divide 5.Exit")
        choice = input("Enter choice: ")
        if choice == '5':
            print("Goodbye!")
            break
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(a, b))
        elif choice == '2':
            print("Result:", subtract(a, b))
        elif choice == '3':
            print("Result:", multiply(a, b))
        elif choice == '4':
            print("Result:", divide(a, b))
        else:
            print("Invalid input!")

if __name__ == "__main__":
    main()
