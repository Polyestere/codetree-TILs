n = int(input())
numbers = list(range(1,n+1))
for i in range(len(numbers)):
    if numbers[i] % 3 == 0: #3의 배수인가
        numbers[i] = 0
    num = list(str(numbers[i]))
    for case in num:
        if int(case) == 3 or int(case) == 6 or int(case) == 9:
            numbers[i] = 0
print(*numbers)