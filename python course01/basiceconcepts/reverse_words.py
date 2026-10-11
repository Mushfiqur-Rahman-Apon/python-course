s = input()
words = s.split()

result = []
for word in words:
    result.append(word[::-1])

print(" ".join(result))
