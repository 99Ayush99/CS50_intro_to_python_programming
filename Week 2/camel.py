str = input("camelCase: ")
for char in str:
    if char.islower():
        print(char,end="")
    else:
        print("_",char.lower(),sep="",end="")