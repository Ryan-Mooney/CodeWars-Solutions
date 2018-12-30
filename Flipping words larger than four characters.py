##Takes a sentence in and flips all words greater than 4 characters around

sentence = "how do you do californication of the california"
new_sentence=""
running_word=""
flipped_word=""

##Goes through each character of the sentence
for i in range(len(sentence)):
    
    ##Runs only at the end of the last word
    if i==(len(sentence)-1):
        running_word=running_word+sentence[i]
        if len(running_word)>4:
            for k in range(len(running_word)):
                flipped_word=flipped_word+running_word[len(running_word)-1-k]
            if len(flipped_word)==len(sentence):
                new_sentence=new_sentence+flipped_word
            else:
                new_sentence=new_sentence+flipped_word
            
        else:
            new_sentence=new_sentence+running_word
            running_word=""

    ##Runs when there is a space, checking to see if word needs flipped
    elif sentence[i]==" ":
        if len(running_word)>4:
            for k in range(len(running_word)):
                flipped_word=flipped_word+running_word[len(running_word)-1-k]
            new_sentence=new_sentence+flipped_word+" "
            flipped_word=""
            running_word=""
        else:
            new_sentence=new_sentence+running_word+" "
            running_word=""
            
    ##Otherwise, adds current letter to the running word
    else:
        running_word=running_word+sentence[i]

print new_sentence
