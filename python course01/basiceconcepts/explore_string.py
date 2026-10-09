name = 'sakib khan'
name2 = "sakib khan"
name3 = """
    sakib khan
    namber one

"""
print(name)
# string is a sequence of charactors
for char in name2:
    print(char)
    
print(name2[3])


print(name2[1:6])
print(name[-3])
print(name[::-1])
# mutable neans changeable
# immutable means you can not change it
#name2[0] = 'R'
if 'khan' in name2:
    print('exists')
print(name2.upper())    