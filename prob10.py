def max (x,y) :
    if x>y :
        return x
    else :
        return y

n= int(input("introdu primul nr : "))
m= int(input("introdu al doilea nr : "))
# a = n
# if n>m :
#     a=n
# else :
#     a=m
# print(a)

a = max(m,n)
print(a)