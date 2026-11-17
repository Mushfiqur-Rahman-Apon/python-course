
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ans = float('inf')

    for i in range(n):
        for j in range(i + 1, n):
            result = a[i] + a[j] + (j - i)

            if result < ans:
                ans = result

    print(ans)


# InputCopy
# 1
# 4
# 20 1 9 4
# OutputCopy
# 7