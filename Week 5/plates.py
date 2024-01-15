def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not(2<=len(s)<=6):
        return False
    elif not(s[:2].isalpha()):
        return False
    is_num = False
    for ch in s:
        if ch.isdigit() and is_num==False and ch=='0':
            return False
        if ch.isdigit():
            is_num=True
        if ch.isalpha() and is_num==False:
            continue
        elif ch.isalpha() and is_num==True:
            return False
    for ch2 in s:
        if ch2.isalpha() or ch2.isdigit():
            continue
        else:
            return False
    return True









main()