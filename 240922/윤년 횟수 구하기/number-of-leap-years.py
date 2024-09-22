n = int(input())
yoon_cnt = 0
for i in range(1,n):
    if i % 100 == 0 and i % 400 == 1:
        continue
    elif i % 4 == 0:
        yoon_cnt += 1
print(yoon_cnt)