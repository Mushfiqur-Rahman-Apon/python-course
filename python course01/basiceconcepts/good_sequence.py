
from collections import Counter

n = int(input())
a = list(map(int, input().split()))

freq = Counter(a)
ans = 0

for x, count in freq.items():
    if count < x:
        ans += count
    else:
        ans += count - x

print(ans)