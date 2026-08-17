class ShoppingCart:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def add(self, item):
        self.items.append(item)

cart = ShoppingCart()
cart.add("Mouse")
cart.add("Keyboard")

print(len(cart))     # 2       -> triggers __len__
print(cart[0])        # Mouse  -> triggers __getitem__
cart[0] = "Wireless Mouse"  # triggers __setitem__

# Real-time use: Building a custom collection (e.g., a Cart, Playlist, Queue) that should behave like a native list in len(), indexing, and loops.