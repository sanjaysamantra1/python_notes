country = 'India' # Global Variable

def greet():
    message = 'Good Morning' # Local to greet()
    print('inside greet function:', message)
    print('inside greet function:', country)
    
greet()
print('Global Scope: ', country)
# print(message)  # Error
# a local variable cann't be used outside the function
# a global variable can be used inside a function