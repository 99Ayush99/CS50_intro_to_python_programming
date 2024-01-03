from collections import defaultdict

grocery_list = defaultdict(int)
while True:
    try:
        item = input()
    except ValueError:
        pass
    except EOFError:
        break
    else:
        grocery_list[item.lower()]+=1

list_item=[]
for a in grocery_list:
    list_item.append(a)
list_item.sort()
for items in list_item:
    print(grocery_list[items],items.upper())
