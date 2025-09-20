import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    resume_with_result = True
    print(art.logo)
    first_number = float(input("What's the first number?:    "))
    while resume_with_result:
        operation = input("+\n-\n*\n/\nPick an operation:    ")
        second_number = float(input("What's the next number?:    "))
        calculated_number =  operations[operation](first_number, second_number)
        print(f"{first_number} {operation} {second_number} = {round(calculated_number, 2)}")
        first_number = calculated_number
        resume = input(f"Type 'y' to continue calculating with {round(calculated_number, 2)}, or type 'n' to start a new calculation:    ").lower()
        if resume == "n" :
            print("\n" * 100)
            calculator()

calculator()