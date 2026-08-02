def sum_of_digits(num):
    sum = 0
    while num>0:
        rem = num % 10
        sum = sum + rem
        num = int(num / 10)
    return sum

res = sum_of_digits(125)
print('result: ',res)