##Function used to complete a two number mathematical operation in the form
##first_operand(operator(second_operand()));

first_operand = None
second_operand = None
operation = None

def final_answer(number1, number2, operator):
    result = 0
    global first_operand
    global second_operand
    global operation
    if operation == "+":
        result = (int(first_operand) + int(second_operand))
    elif operation == "-":
        result = (int(first_operand) - int(second_operand))
    elif operation == "/":
        result = (int(first_operand) / int(second_operand))
    elif operation == "*":
        result = (int(first_operand) * int(second_operand))
    first_operand = None
    second_operand = None
    operation = None
    return int(result)

def zero(*operator, **second_number):
    global first_operand
    global second_operand
    global operation
    if second_operand == None:
        second_operand=0
    elif first_operand == None:
        first_operand=0
    if operation == None:
        pass
    else:
        return final_answer(first_operand, second_operand, operation)
def one(*operator, **second_number):
    global first_operand
    global second_operand
    global operation
    if second_operand == None:
        second_operand=1
    elif first_operand == None:
        first_operand=1
    if operation == None:
        pass
    else:
        return final_answer(first_operand, second_operand, operation)
def two(*operator, **second_number):
    global first_operand
    global second_operand
    global operation
    if second_operand == None:
        second_operand=2
    elif first_operand == None:
        first_operand=2
    if operation == None:
        pass
    else:
        return final_answer(first_operand, second_operand, operation)
def three(*operator, **second_number):
    global first_operand
    global second_operand
    global operation
    if second_operand == None:
        second_operand=3
    elif first_operand == None:
        first_operand=3
    if operation == None:
        pass
    else:
        return final_answer(first_operand, second_operand, operation)
def four(*operator, **second_number):
    global first_operand
    global second_operand
    global operation
    if second_operand == None:
        second_operand=4
    elif first_operand == None:
        first_operand=4
    if operation == None:
        pass
    else:
        return final_answer(first_operand, second_operand, operation)
def five(*operator, **second_number):
    global first_operand
    global second_operand
    global operation
    if second_operand == None:
        second_operand=5
    elif first_operand == None:
        first_operand=5
    if operation == None:
        pass
    else:
        return final_answer(first_operand, second_operand, operation)
def six(*operator, **second_number):
    global first_operand
    global second_operand
    global operation
    if second_operand == None:
        second_operand=6
    elif first_operand == None:
        first_operand=6
    if operation == None:
        pass
    else:
        return final_answer(first_operand, second_operand, operation)
def seven(*operator, **second_number):
    global first_operand
    global second_operand
    global operation
    if second_operand == None:
        second_operand=7
    elif first_operand == None:
        first_operand=7
    if operation == None:
        pass
    else:
        return final_answer(first_operand, second_operand, operation)
def eight(*operator, **second_number):
    global first_operand
    global second_operand
    global operation
    if second_operand == None:
        second_operand=8
    elif first_operand == None:
        first_operand=8
    if operation == None:
        pass
    else:
        return final_answer(first_operand, second_operand, operation)
def nine(*operator, **second_number):
    global first_operand
    global second_operand
    global operation
    if second_operand == None:
        second_operand=9
    elif first_operand == None:
        first_operand=9
    if operation == None:
        pass
    else:
        return final_answer(first_operand, second_operand, operation)

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

print seven(times(five())); ##must return 35
print four(plus(nine())); ##must return 13
print eight(minus(three())); ## must return 5
print six(divided_by(two())); ## must return 3
