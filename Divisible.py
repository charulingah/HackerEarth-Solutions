N=int(input())
c=0
b=0
a=list(map(int,input().split()))
for i in range(N//2):
    if(a[i]>=100000):
        a[i]=a[i]/100000
    elif(a[i]>=10000):
        a[i]=a[i]/10000
    elif(a[i]>=1000):
        a[i]=a[i]/1000
    elif(a[i]>=100):
        a[i]=a[i]/100
    elif(a[i]>=10):
        a[i]=a[i]/10
    else:
        a[i]=a[i]
    if(i%2==0):
        c+=int(a[i])
    else:
        b+=int(a[i])

for i in range(N//2,N):
    if(i%2==0):
        c+=(a[i]%10)
    else:
        b+=(a[i]%10)
if(abs(c-b)==0 or abs(c-b)==11):
    print("OUI")
else:
    print("NON")
