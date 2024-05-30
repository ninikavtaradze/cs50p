def main():
    amount_due=50
    print("Change Owed:" , abs( get_coins(amount_due)))

def get_coins(amount_due):
   while True:
    if amount_due <= 0:
        return amount_due
    print ("Amount Due:" , amount_due)
    n =int(input ("Insert Coin:"))
    if n == 5:
        amount_due -= n
    elif n == 10:
        amount_due -= n
    elif n ==25 :
        amount_due -= n
    else :
        continue



main()
