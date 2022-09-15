a=input("enter your word:")
b=input("enter your word:")
match (a,b):
    case (a,b) if a==b:
        print("identical word:")
    case (a,b) if a>b:
        print("{} comes after {}".format(a,b))
    case (a,b) if a<b:
        print("{} comes after {}".format(b,a))
              
