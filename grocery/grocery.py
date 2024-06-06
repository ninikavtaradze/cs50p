emptydict = {}

while True:
    try:
        grocery = input().upper()
        if grocery not in emptydict:
           emptydict[grocery]= 1
        else:
            emptydict[grocery] += 1
    except  EOFError:
        for key,value in sorted(emptydict.items()):
            print(value,key)
        break
