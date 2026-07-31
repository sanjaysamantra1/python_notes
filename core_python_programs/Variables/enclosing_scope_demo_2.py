def outer():
    a = 10
    print('Outer: ',a)
    
    def inner():
        a = a+5
        print('inner: ',a)
        
    inner()
    
outer()