n=int(input("introduceti n : "))
s=0
x=(n-1)//2
if n%2==1 and n>0 :
    for i in range (x+1,x+n+1) :
       print (i)
       s=s+i
print("suma este ", s, "; patratul lui ",n," este ", n*n)    