
n = int(input())
a = list(map(int, input().split()))

operations = 0

while all(x % 2 == 0 for x in a):
    a = [x // 2 for x in a]
    operations += 1

print(operations)