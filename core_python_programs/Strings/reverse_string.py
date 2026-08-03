str = input("Enter string: ")

# Option-1
revStr1 = str[::-1]
print('Reverse: ',revStr1)

# Option-2
charArr = list(str)
charArr.reverse()
print('Reverse: ',"".join(charArr))
