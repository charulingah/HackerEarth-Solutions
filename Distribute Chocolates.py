t = int(input())
for _ in range(t):
    c,n = map(int,input().split())
    minimumChocolates = (n*(n+1))//2
    if minimumChocolates >= c:
        print(c)
    else:
        c = c - minimumChocolates
        ans = c%n
        print(ans)
