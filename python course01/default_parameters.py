def sum(num1, num2, num3=0):
    result = num1 + num2 + num3
    return result

total = sum(99, 11, 5)
print('total: ', total)

total = all_sum(45, 46, 89, 11, 82, 5, 2, 77)
print('all sum: ', total)
def do_a_lot(*args):
    print(args)
    