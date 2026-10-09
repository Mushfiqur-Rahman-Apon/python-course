n = input()

rev = n[::-1]

rev = rev.lstrip('0')

if rev == '':
    rev = '0'

print(rev)

if n == n[::-1]:
    print("YES")
else:
    print("NO")