text = input("Input: ")
print("Output: ",end="")
for char in text:
    if char in ['a','e','i','o','u','A','E','I','O','U']:
        continue
    else:
        print(char,sep="",end="")