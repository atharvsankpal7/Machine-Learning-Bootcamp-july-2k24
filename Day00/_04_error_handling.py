def fact(a):
    if a == 1 or a == 0:
        return 1
    else:
        return a * fact(a-1)
    
try:
    a = int(input("enter the value of a -->\n"))
    print(fact(a))
except:
    print("enter a valid value")
    