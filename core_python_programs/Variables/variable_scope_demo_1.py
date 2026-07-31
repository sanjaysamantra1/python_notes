a = 10
b = 20
print('In Global Scope: ',a,b)

def fun1():
    message1 = "Hello" #local to this function
    print('In fun1 function: ', message1)
    print('In fun1 function: ',a,b)
    # print('In Greet function: ', message2)
fun1()

def fun2():
    message2 = "Hiiiii" #local to this function
    # print('In fun2 function: ', message1)
    print('In fun2 function: ', message2)
    print('In fun2 function: ',a,b)
fun2()

