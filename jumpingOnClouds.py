def jumpingOnClouds(c):
    position=0
    jumps=0
    while position<len(c)-1:
        if position==len(c)-2:
            position=position+1
            jumps=jumps+1
        elif c[position+2]==0:
            position=position+2
            jumps=jumps+1
        else:
            position=position+1
            jumps=jumps+1
        print('jump = ' + str(jumps))
        print('position = ' + str(position))
    return(jumps)

c=[0,0,0,1,0,0]
print(c)
print('Length of c = ' + str(len(c)))
print(jumpingOnClouds(c))
