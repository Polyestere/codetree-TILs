n = int(input())
numbers = list(range(1,n+1))

for i in range(len(numbers)):
    if numbers[i] % 3 == 0: #3의 배수인가
        numbers[i] = 0

    num = list(str(numbers[i]))#정수를 자릿수별로 나누기 위해 문자열로 형변환
    if '3' in num or '6' in num or '9' in num:
            numbers[i] = 0
print(*numbers)