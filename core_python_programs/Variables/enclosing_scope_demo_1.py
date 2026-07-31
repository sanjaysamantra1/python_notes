def outer():
    a = 10
    print('Outer: ',a)
    
    def inner():
        b = 20 
        print('inner: ',a,b) # a is from enclosing scope, b is from local scope
        
    inner()
    
outer()