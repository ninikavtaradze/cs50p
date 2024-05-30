def main():
    name = input("camelCase: ")
    print( "snake_case: ", end= "")
    snake_case(name)

def snake_case (name):
    for letter in name:
        if letter.isupper():
            print ("_" + letter.lower(), end="")
        else :
            print ( letter, end="")
    print ()

main ()
