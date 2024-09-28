ans = [list(map(int,input().split())) for _ in range(4)]
output = []
for i in range(4):
    hap = 0
    for j in range(4):
        hap += ans[i][j]
        if j == 3:
            output.append(hap)

for i in output:
    print(i)