while True:
    try:
        x,y =input("Fracrion: ").split("/")
        x = int(x)
        y = int(y)
        procenti = x / y
        result = procenti * 100
        if y < x :
             continue
        if y == 0:
            continue
        if result <= 1:
            print("E")
            break
        elif result >= 99:
            print("F")
            break
        else:
            print(str(round(result))+"%")
            break
    except(ValueError, ZeroDivisionError):
        continue






