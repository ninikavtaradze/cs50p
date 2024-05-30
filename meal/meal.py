def main():
    time = input ("What time is it ?")
    new_time= convert (time)
    if new_time >=7 and new_time <= 8:
        print ("breakfast time")
    elif new_time >=12 and new_time <=13:
        print("lunch time")
    elif new_time >=18 and new_time <=19:
        print ("dinner time")


def convert (new_time):
    hours, minutes = new_time.split(":")
    new_minutes = float(minutes)/60
    return float(hours) + new_minutes

if __name__ == "__main__":
    main()
