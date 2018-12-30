##Takes array strarr and finds the longest string consisting of
##k number of consecutive strings

strarr=["first", "second", "third", "fourth", "3243524654", "sixth"]
k=4

##Initialize variables
longest_cons_string=""
comparison_str=""

##Goes through the array of strings and compares new concatenated string to previous one
for i in range(len(strarr)):
    ##This is used to skip the iterations until a string of length k strings can be made
    
    if i<k-1:
        pass
    
    ##Once a string of length k can be made, we start to compare
    else:
        
        ##Concatenates k number strings to compare
        print range(i-k+1, i+1, 1)
        for m in range(i-k+1, i+1, 1):
            comparison_str=comparison_str+strarr[m]

        ##If this is larger than the previous combination of strings we found, it replaces it as largest combination
        if len(comparison_str)>len(longest_cons_string):
            longest_cons_string=comparison_str

        ##Resets comparison string for next iteration
        comparison_str=""
        
print longest_cons_string
