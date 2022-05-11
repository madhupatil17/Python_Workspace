import common_functions

def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def division(n1, n2):
    return n1 / n2

def multiplication(n1, n2):
    return n1 * n2

operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}
def calculator():
    num1 = float(input("Enter first number: "))
    end = False
    while not end:
        operation = input("Choose +, -, /, * : ")
        num2 = float(input("Enter next number: "))
        function = operations[operation]
        output = function(num1, num2)
        print(output)
        if input("Do you wish to continue? ").lower() == 'no':
            if input("Do you wish to start new calculation? ").lower() == 'yes':
                calculator()
            else:
                end = True
                common_functions.cls()
        else:
            num1 = output

calculator()