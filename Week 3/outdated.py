months =[
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
]
while True:
    try:
        outdated_date = input("Date: ")
        if '/' in outdated_date:
            mm, dd, yyyy = outdated_date.split('/')
        elif ',' in outdated_date:
            first, yyyy = outdated_date.split(',')
            month, dd = first.split(' ')
            mm=(months.index(month))+1
        if int(mm)>12 or int(dd)>31:
                raise ValueError
    except ValueError:
        pass
    except KeyError:
        pass
    except EOFError:
        pass
    except NameError:
        pass
    else:
        print(f"{int(yyyy)}-{int(mm):02}-{int(dd):02}")
        break