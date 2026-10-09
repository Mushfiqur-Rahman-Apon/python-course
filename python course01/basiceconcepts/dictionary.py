numbers = [12, 56, 98, 56, 12, 6, 98 ]
petson1 = ['kala Chan', 'kalipur',23, 'student']
# key value pair
# diction
# object
# hash table
# overlap with set
person = {'name': 'kala Pakhi', 'address': 'kaliapur', 'age' : 23, 'job': 'bekar'}
print(person)
print(person['job'])
print(person.keys())
print(person.values())
person['language'] = 'python'
person['name'] = 'sada pakhi'
print(person)

# special dictionary looping
for key, value in person.item():
    print(key, value)