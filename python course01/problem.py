# i = 1
# while i <= 5:
#     print(i)
#     # i = 1
# # while i <= 5:
# #     print(i)
# #     i=i+1
# for i in range(1, 6):
#     print(i)
    
    
# num = int(input())
# i =1
# while i <= num


#     print(i)
#     sum=sum+4    
    
# num = int(input())
# # Solution as follows
# n = 1
# while n <= num:
#     print(n * n, end=" ")
#     n += 1
# num = int(input())
# factorial = 1

# while num > 0:
#     factorial *= num
#     num -= 1

# print(factorial)

str = input()
ans = 0
i = 0
while i < len(str):
    c = str[i]
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        ans += 1
    i += 1

print(ans)