yoon_cnt = 0
for i in range(1,int(input())+1):
    if i % 100 == 0 and i % 400 != 0:
        i += 1
        continue
    elif i % 4 == 0:
        yoon_cnt += 1
print(yoon_cnt)