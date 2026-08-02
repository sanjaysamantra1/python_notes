str = 'This is Python Class'

print(str.upper())
print(str.lower())
print(str.capitalize())
print(str.title())

print(str.swapcase())

print(str.find('Python'))
print(str.index('Python'))

print(str.find('java'))    # -1
# print(str.index('java'))   #  Error

print(str.count('is'))

print(str.startswith('This'))
print(str.startswith('That'))

print(str.endswith('Class'))
print(str.endswith('Session'))

print(str.split(" "))
chars = list(str)
print(chars)
print(str.split("This"))

#str[start:end:step]
print(str[8:14]) 
print(str[8:]) 
print(str[:8]) 
print(str[:]) 
print(str[-5:]) 
print(str[::2]) # every second char
print(str[::-1]) # reverse
