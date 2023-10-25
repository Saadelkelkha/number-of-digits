def count(x) :
    a=x
    p=1
    while True :
        if (a/10)>1 :
            p=p+1
            a=a/10
        if (a/10)<1 :
            break
    return p
n=int(input("type number :"))
print("number of chiffer is :",count(n))