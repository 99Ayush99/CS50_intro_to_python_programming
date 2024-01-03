import math
while True:
    try:
        fuel = input("Fraction: ")
        a, b, c = fuel.partition('/')
        a=float(a)
        c=float(c)
        if not(a.is_integer()) or not(c.is_integer()) or a/c>1.0:
            continue
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    else:
        if a/c<=0.01:
            print("E")
            break
        elif a/c>=0.99:
            print("F")
            break
        else:
            print(round(a/c*100),"%",sep="")
            break