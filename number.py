
a, b = map(int, input().split())

found = False

for i in range(a, b + 1):
    s = str(i)

    if all(ch == '4' or ch == '7' for ch in s):
        print(i, end=" ")
        found = True

if not found:
    print(-1)