fruitSet = {"apple", "banana", "cherry"}

fruitSet.remove("apple")
fruitSet.discard("banana")
print("fruitSet: ",fruitSet)

fruitSet.discard("banana")    # doesn't throw error even when the item is not found
# fruitSet.remove("banana")   # throws error when the item is not found
print("fruitSet: ",fruitSet)