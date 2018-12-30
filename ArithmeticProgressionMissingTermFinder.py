#This program finds the missing item in an arithmetic progression involving either
#addition or subtraction and returns the missing number in the sequence.

def find_missing(sequence):
    i=0
    old_difference=0
    #First we go through the sequence to find the progression function
    for item in sequence:
        if item==sequence[0]:
            continue
        else:
            new_difference=item-sequence[i]
            if new_difference==old_difference:
                difference=new_difference
                break
            old_difference=new_difference
            i=i+1
    i=0
    #Then we go through again to find out where the sequence skips an item
    for item in sequence:
        if item==sequence[0]:
            continue
        elif item-sequence[i]==difference:
            i=i+1
            pass
        else:
            return(sequence[i]+difference)


sequence=[1, 3, 5, 9, 11]
print('Missing number is ' + str(find_missing(sequence)))
