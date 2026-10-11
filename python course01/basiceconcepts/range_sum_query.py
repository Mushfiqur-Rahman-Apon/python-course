N, Q = map(int, input().split())
A = list(map(int, input().split()))

for i in range(Q):
    L, R = map(int, input().split())
    print(sum(A[L-1:R]))
    
    
# 6 3
# 6 4 2 7 2 7
# 1 3
# 3 6
# 1 6
    
# 12
# 18
# 28
    