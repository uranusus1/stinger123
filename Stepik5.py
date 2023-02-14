n = int(input())
list = list(map(int, input().split()))

for i in range(1, n):
    for j in range(i, 0, -1):
        if list[j] < list[j-1]:
            list[j], list[j-1] = list[j-1], list[j]
        else:
            break

print(*list)