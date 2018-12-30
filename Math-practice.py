first_operand = None
second_operand = None
operation = None
print first_operand
print second_operand
print operation

def four(*operator, **second_number):
    global first_operand
    global second_operand
    global operation
    print first_operand
    print second_operand
    print operation
    if second_operand == None:
        second_operand=4
    elif first_operand == None:
        first_operand=4
    if operation == None:
        pass
    elif operation == "+":
        return (first_operand + second_operand)
    elif operation == "-":
        return (first_operand - second_operand)
    elif operation == "/":
        return (first_operand / second_operand)
    elif operation == "*":
        return (first_operand * second_operand)

def nine(*operator, **second_number):
    global first_operand
    global second_operand
    global operation
    print first_operand
    print second_operand
    print operation
    if second_operand == None:
        second_operand=9
    elif first_operand == None:
        first_operand=9
    if operation == None:
        pass
    elif operation == "+":
        return (first_operand + second_operand)
    elif operation == "-":
        return (first_operand - second_operand)
    elif operation == "/":
        return (first_operand / second_operand)
    elif operation == "*":
        return (first_operand * second_operand)


def plus(*second_number):
    global operation
    operation = "+"
def minus(*second_number):
    global operation
    operation = "-"
def times(*second_number):
    global operation
    operation = "*"
def divided_by(*second_number):
    global operation
    operation = "/"

print four(plus(nine()))
