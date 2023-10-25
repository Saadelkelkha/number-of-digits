def count(x) :
    p=1
    while (x/10)>1 :
            p=p+1
            x=x/10
    return p
n=int(input("type number :"))
print("number of chiffer is :",count(n))