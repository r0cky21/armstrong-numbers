#arsmstrongg number-
n=153
n1=n
n2=n

tot=0
c=0

while(n!=0):
    n=n//10
    c=c+1

while (n1!=0):
    rem=n1%10
    tot=tot+(rem**c)
    n1=n1//10

if(tot == n2):
    print("armstrong")

else:
    print("not armstrong")
