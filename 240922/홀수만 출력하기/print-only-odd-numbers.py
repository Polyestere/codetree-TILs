numbers = []
for i in range(int(input())):
        numbers.append(int(input()))
for num in numbers:
    if num % 3 == 0 and num % 2 == 1:
        print(num)