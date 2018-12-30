n=int(raw_input("Enter a number to be turned into binary: "))
binaryN=[0]
##For each digit, 1 is added to the binary number
for i in range(n):
    ##This adds 1 to the furthest most place in the binary number
    binaryN[len(binaryN)-1]+=1
    
    ##This loop looks at each place and determines if any digits need to be carried over
    for k in range(len(binaryN)):
        ##When adding 1 requires a digit to be carried over into a new binary place
        ##this adds to the list and carries it over
        if len(binaryN)-1-k==0 and binaryN[len(binaryN)-1-k]==2:
            binaryN=[1]+binaryN
            binaryN[len(binaryN)-1-k]=0

        ##This carries over into a preexisting placeholder
        elif binaryN[len(binaryN)-1-k]==2:
            binaryN[len(binaryN)-1-k]=0
            binaryN[len(binaryN)-2-k]+=1

        ##If no carrying over needs to be done, then no other placeholders need to be looked at
        ##in this iteration
        else:
            break
binarySum=0
binaryAnswer=''
for m in range(len(binaryN)):
    binarySum+=binaryN[m]
    binaryAnswer+=str(binaryN[m])
print 'The user supplied number ' + str(n) + ' is ' + binaryAnswer + ' in binary and its sum is ' + str(binarySum)
