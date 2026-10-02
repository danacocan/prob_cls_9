def aduna(a, b):
    return a+b

def scade(a,b):
    return a-b


def putere(x, y):
    # return pow(x,y)
    p=1
    for i in range(1,y+1):
       p = p * x
    return p


x = int(input("x="))
y = int(input("y="))

print("x+y=", aduna(x,y))
c = scade(x,y)
print("x-y=", c)

print("x^y=", putere(x,y))



