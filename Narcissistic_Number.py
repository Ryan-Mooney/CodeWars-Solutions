#This method determines if the number is narcissistic
#A Narcissistic Number is a number which is the sum of its own digits,
#each raised to the power of the number of digits.

def narcissistic(number):
    power = len(str(number))
    new_number=str(number)
    digits = []
    solution=0
    for i in range(len(new_number)):
        print(i)
        solution+=int(new_number[i])**power
        print(solution)
    return(solution==number)
