def remove_forward_slashes(text):
    new_text=''
    for c in text:
        if c!="\\":
            new_text=new_text+c
    print(new_text)
remove_forward_slashes('https:\/\/images.dog.ceo\/breeds\/brabancon\/n02112706_607.jpg')
