def main ():
    x = input ("Input: ")
    output(x)

def output(x):
    print("Output: ", end="")
    for i in x:
        if i in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            i.replace(i , "")
        else:
            print(i, end="")
    print()

main()
