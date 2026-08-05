# ========================================
# 1. Reverse a string
# ========================================

text = "sachin"
print("1.", text[::-1])


# ========================================
# 2. Reverse words
# ========================================

text = "This is javascript class"
words = text.split()
result = " ".join(words[::-1])

print("2.", result)


# ========================================
# 3. First non-repeated character
# ========================================

text = "entertainment"

for char in text:
    if text.count(char) == 1:
        print("3.", char)
        break


# ========================================
# 4. Title case
# ========================================

text = "this is javascript class"
print("4.", text.title())


# ========================================
# 5. Longest word
# ========================================

text = "this is javascript class"

words = text.split()
longest_word = max(words, key=len)

print("5.", longest_word)


# ========================================
# 6. Mask Account Number
# ========================================

account_number = "12345678987"

result = (
    account_number[:2]
    + "*" * (len(account_number) - 4)
    + account_number[-2:]
)

print("6.", result)


# ========================================
# 7. Format Credit Card Number
# ========================================

card_number = "1111222233334444"

result = "-".join(
    card_number[i:i+4]
    for i in range(0, len(card_number), 4)
)

print("7.", result)


# ========================================
# 8. Count vowels and consonants
# ========================================

text = "Hello World"

vowels = 0
consonants = 0

for char in text.lower():

    if char.isalpha():

        if char in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("8. Vowels:", vowels, ", Consonants:", consonants)


# ========================================
# 9. Remove special characters
# ========================================

text = "hello@#hi&"

result = ""

for char in text:
    if char.isalnum():
        result += char

print("9.", result)


# ========================================
# 10. Move special characters to end
# ========================================

text = "hello@#hi&"

normal_chars = ""
special_chars = ""

for char in text:

    if char.isalnum():
        normal_chars += char
    else:
        special_chars += char

result = normal_chars + special_chars

print("10.", result)