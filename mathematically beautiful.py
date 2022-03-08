t = int(input())
for _ in range(t):
    x,k = map(int,input().split())
    options = [1]
    val = k
    count = 1
    while val<=x:
        count+=1
        options.append(val)
        val = k**count
        
    total = options.pop()

    while total <= x:
        dif = x - total
        options = [i for i in options if i<= dif]
        try:
            total += options.pop()
        except:
            break

            
    if total == x:
        print("YES")
    else:
        print("NO")
