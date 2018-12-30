##This is a function that emulates the Facebook Like Button
def likes(names):
    remaining = len(names)-2;
    if len(names)==0:
        return "no one likes this"
    elif len(names)==1:
        return str(names[0] + " likes this")
    elif len(names)==2:
        return str(names[0]+" and " + names[1] + " like this")
    elif len(names)==3:
        return str(names[0] + ", " + names[1] + " and " + names[2] + " like this")
    elif len(names)>3:
        return str(names[0] + ", " + names[1] + " and " + str(remaining) + " others like this")


names0 = []
names1 = ["Ryan"]
names2 = ["Ryan", "Mara"]
names3 = ["Ryan", "Mara", "Pebbles"]
names4 = ["Ryan", "Mara", "Pebbles", "Bojangles"]

print(likes(names0))
print(likes(names1))
print(likes(names2))
print(likes(names3))
print(likes(names4))
