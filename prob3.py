n= int (input())
c=0
n1=n
while n>0 :
  if n%10==2 :
     c+=1
     n=n//10
  else :
     n=n//10
print ("numarul",str(n1),"are" ,str(c), "cifre 2")     