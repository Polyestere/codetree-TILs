a, b = map(int,input().split())
ans = []
ans.append(a)
while True:
    
    if a % 2 == 0:
        a+=3
        if a > b:
            break
        ans.append(a)
    else:
        a*=2
        if a > b:
            break
        ans.append(a)
print(*ans)