n = int(input())
class_cnt = 0
corridor_cnt = 0
restroom_cnt = 0
for i in range(1,n+1):
    if i % 2 == 0:
        class_cnt += 1
    if i % 3 == 0:
        corridor_cnt += 1
        if i % 2 == 0:
            class_cnt -= 1
    if i % 12 == 0:
        restroom_cnt += 1
        corridor_cnt -= 1
print(class_cnt, corridor_cnt, restroom_cnt, sep=" ")
#elif으로 12,3,2, 순서로 조건문을 통과하는 방법도 있음