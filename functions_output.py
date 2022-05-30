# Functions with output (return)




def format_name(f_name,l_name): 
    # Adding docstrings.
    """Takes the first and last name 
    and format it to return the title case version of the name""" 
    formated_f_name=f_name.title()
    formated_l_name = l_name.title()
    return (f"{formated_f_name},{formated_l_name}")
# formatted_string = format_name("rAcHAel" ,"minage")
print(format_name("rAcHAel" ,"minage"))


# CALCULATOR
def add(n1,n2):
    """Returns the sum of the numbers"""
    return n1+n2

def subtract(n1,n2):
    """Returns the difference of the numbers"""
    return n1-n2

def multiply(n1,n2):
    """Returns the product of the numbers"""
    return n1*n2

def divide(n1,n2):
    """Returns the quotient of a given value"""
    return n1//n2
operations = {
    "+":add,
"-":subtract,
"*":multiply,
"//":divide
}

def calculator():
    number_one = float(input("Enter the first number"))
    for key in operations:
        print(key)
    should_continue = True
    while should_continue:
        operation_key = input("Pick an operation from the above line:\n")
        number_two  = float(input("Enter the next number"))
        calculations = operations[operation_key]
        ans = calculations(number_one,number_two)
        print(f"{number_one} {operation_key} {number_two} = {ans}")

        choice= input(f"Type 'y' to continue calculating with previous {ans} or 'n' to exit:\n")
        if choice =="y":
            number_one=ans
            #    should_continue
        else:
            should_continue = False 
            # print("End of operation")
            calculator()
calculator()























# if operation_symbol == +:
#     print(add(num1,num2))
# elif operation_symbol == "-":
#     print(subtract(num1,num2))
# elif operation_symbol == "*":
#     print(multiplication(num1,num2))
# elif operation_symbol == "//":
#     print(divide(num1,num2))


