# More specific exceptions must be caught before general ones

try:
    result = [1, 2, 3][10]
except IndexError:
    print("Index out of range")
except Exception:  # broad catch-all, placed last
    print("Some other error occurred")