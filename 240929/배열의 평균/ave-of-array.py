numbers = [list(map(int,input().split())) for _ in range(2)]
row_mean = []
column_mean = [0 for _ in range(4)]
all_mean = 0
for i in numbers:
    row_mean.append(sum(i)/len(i))
    all_mean += sum(i)
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        column_mean[j] += numbers[i][j]

for i in row_mean:
    print('%.1f'% i,end = ' ')
print()
for i in column_mean:
    print('%.1f'% (i/2),end = ' ')
print()
print('%.1f'%(all_mean/8))