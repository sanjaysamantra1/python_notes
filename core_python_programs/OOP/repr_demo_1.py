class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        # Used by developers - should be unambiguous, ideally eval-able
        return f"Product('{self.name}', {self.price})"

    def __str__(self):
        # Used by print() / str() - should be human-readable
        return f"{self.name} - ${self.price}"

p = Product("Laptop", 999)
print(p)        # Laptop - $999           (__str__)
print(repr(p))  # Product('Laptop', 999)  (__repr__)