print("sum:")
print("sub:")
print("mult:")
print("divide:")
x=int(input("enter your choice:"))
match x:
    case 1:
        a,b=int(input()),int(input())
        c=a+b
        print("sum of these number:",c)
    case 2:
        a,b=int(input()),int(input())
        c=a-b
        print("sub of these number:",c)
    case 3:
        a,b=int(input()),int(input())
        c=a*b
        print("mult of these number:",c)
    case 4:
        a,b=int(input()),int(input())
        c=a/b
        print("division of these number:",c)
