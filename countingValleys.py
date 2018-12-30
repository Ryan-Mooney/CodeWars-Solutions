def countingValleys(n, s):
    elevation=0
    valleys=0
    for step in s:
        if step=='U':
            elevation=elevation+1
        elif step=='D':
            elevation=elevation-1
        if elevation==0 and step=='U':
            valleys=valleys+1
        print(elevation)
    return(valleys)

steps='DDUUDDUUDD'
print(countingValleys(9,steps))
