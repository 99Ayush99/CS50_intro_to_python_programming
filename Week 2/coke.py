amount = 50
while True:
    print("Amount Due:",amount)
    coin_val = int(input("Insert Coin: "))
    if coin_val in [25,10,5]:
        amount = amount-coin_val
    else:
        continue
    if amount<=0:
        print("Change Owed:",amount.__abs__())
        break