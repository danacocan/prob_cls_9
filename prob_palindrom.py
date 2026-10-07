def e_palindrom(x):
    m=0
    i=x
    while i>0 :
        m=m*10+i%10
        i=i//10
    if m==x :
        return True
    else :
        return False

    
n=int(input("intrduceti n "))
a=e_palindrom (n)
if a:
    print ("numarul este palindrom")
else :
    print("numarul nu este palindrom")


