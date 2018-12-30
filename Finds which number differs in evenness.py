def iq_test(numbers):
    new_numbers=numbers.split(' ')
    print(new_numbers)
    for i in range(len(new_numbers)):
        new_numbers[i]=int(new_numbers[i])
    evenness = []
    for i in range(len(new_numbers)):
        if new_numbers[i]%2==0:
            evenness.append(1)
        else:
            evenness.append(0)
    if sum(evenness)==1:
        for i in range(len(new_numbers)):
            if evenness[i]==1:
                answer=i+1
    else:
        for i in range(len(new_numbers)):
            if evenness[i]==0:
                answer=i+1
    return answer

numbers1=("1 2 3")
numbers2=("2 2 2 2 2 2 2 2 3")

print(iq_test(numbers1))
print(iq_test(numbers2))
