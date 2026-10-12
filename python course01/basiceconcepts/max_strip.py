s = input()

balance = 0
start = 0
count = 0
result = []

for i in range(len(s)):
    if s[i] == 'L':
        balance += 1
    else:
        balance -= 1

    if balance == 0:
        result.append(s[start:i + 1])
        count += 1
        start = i + 1

print(count)
for sub in result:
    print(sub)