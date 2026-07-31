x = "Global"   # G

def outer():
    x = "Enclosing"   # E

    def inner():
        x = "Local"   # L
        print(x)      # Local
        print(len([1, 2, 3]))  # Built-in (B)

    inner()
    print(x)          # Enclosing

outer()
print(x)              # Global