def main():
    smile=input()
    result=convert(smile)
    print(result)



def convert(smile):
    smile1=smile.replace(":)" ,"🙂" )
    smile2=smile1.replace( ":(" , "🙁" )
    return smile2
main()
