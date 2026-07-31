count = 0  # global 

def increment():
    count += 1  # trying to modify global var inside a function
    print('inside increment count: ',count)
    
increment()
print('global scope: ',count)