def duplicate_encode(word):
    ##Initializing variables
    encoder=[]
    result=""

    ##For each character, compare it to every other character in the string
    for i in range(len(word)):
        encoder.append(0)
        for m in range(len(word)):
            ##Ensures it doesn't compare it to itself
            if m==i:
                pass
            elif word[i].lower()==word[m].lower():
                encoder[i]=1

    ##Using the encoder, makes a new string based on duplicity
    for n in range(len(word)):
        if encoder[n]==0:
            result=result+"("
        else:
            result=result+")"
    return result


print duplicate_encode("Success")
