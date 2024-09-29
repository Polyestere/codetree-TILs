alphabet = [input().split() for _ in range(5)]
ans = [ [] for i in range(5)]
for i in range(len(alphabet)):
    for a in alphabet[i]:
        ans[i].append(a.upper())
for i in ans:
    print(*i)