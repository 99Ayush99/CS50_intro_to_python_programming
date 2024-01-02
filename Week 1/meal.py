def main():
    samay = input("What Time is it? ")
    samay = convert(samay)
    if 7<=samay<=8:
        print("breakfast time")
    elif 12<=samay<=13:
        print("lunch time")
    elif 18<=samay<=19:
        print("dinner time")
def convert(samay):
    a,b = samay.split(':')
    samay=float(a)+float(b)/60
    return samay
if __name__ == "__main__":
    main()