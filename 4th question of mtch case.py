age=int(input("enter your age :"))
match age:
        case age if age in(1,2,3,4,5,6,7,8,9,10):
             print("you are kid:")
        case age if age in(11,12,13,14,15,16,17,18,19,20):
             print("you are teen:")
        case age if age in(21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40):
             print("you are young:")
        case age if age in(41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60):
             print("you are experianced:")
        case age if age in range(60,150):
             print("you are senior citizen:")
        case age if age in range(150,5000):
             print("you are special one:")
