# ============================================================
# 1. Print occurrence of each character in a string
# Input: entertainment
# Output: {'e': 3, 'n': 2, 't': 3, ...}
# ============================================================

text = "entertainment"
result = {}
for char in text:
    if char in result:
        result[char] += 1
    else:
        result[char] = 1
print("1. Character Occurrences:")
print(result)


# ============================================================
# 2. Print the character repeated maximum number of times
# Input: hello world
# Output: L
# ============================================================

text = "hello world"
result = {}
for char in text.lower():
    if char == " ":
        continue
    if char in result:
        result[char] += 1
    else:
        result[char] = 1
max_char = max(result, key=result.get)

print("\n2. Maximum repeated character:")
print(max_char.upper())


# ============================================================
# 3. Compress a String
# Input: aaabbc
# Output: a3b2c1
# ============================================================

text = "aaabbc"

result = ""
count = 1

for i in range(1, len(text)):

    if text[i] == text[i - 1]:
        count += 1

    else:
        result += text[i - 1] + str(count)
        count = 1

# Add the last character
result += text[-1] + str(count)

print("\n3. Compressed String:")
print(result)


# ============================================================
# 4. Expand a Compressed String
# Input: a3b2c4
# Output: aaabbcccc
# ============================================================

text = "a3b2c4"

result = ""

for i in range(0, len(text), 2):

    char = text[i]
    count = int(text[i + 1])

    result += char * count

print("\n4. Expanded String:")
print(result)


# ============================================================
# 5. Check if two strings are Anagrams
# Input: listen, silent
# Output: Anagram
# ============================================================

str1 = "listen"
str2 = "silent"

str1 = str1.lower()
str2 = str2.lower()

print("\n5. Anagram Check:")

if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not Anagram")


# ============================================================
# 6. Print abbreviation for a string
# Input: Rabindra Nath Tagore
# Output: R. N. Tagore
# ============================================================

name = "Rabindra Nath Tagore"

words = name.split()

result = ""

for word in words[:-1]:
    result += word[0].upper() + ". "

result += words[-1].title()

print("\n6. Abbreviation:")
print(result)


# ============================================================
# 7. Validate Parentheses
# Input: ([{}])
# Output: True
# ============================================================

text = "([{}])"

stack = []

pairs = {
    ")": "(",
    "]": "[",
    "}": "{"
}

valid = True

for char in text:

    # Opening bracket
    if char in "([{":
        stack.append(char)

    # Closing bracket
    elif char in ")]}":

        if len(stack) == 0:
            valid = False
            break

        top = stack.pop()

        if top != pairs[char]:
            valid = False
            break

# Stack should be empty at the end
if len(stack) != 0:
    valid = False

print("\n7. Parentheses Validation:")
print(valid)


# ============================================================
# 8. Print all permutations of a 3-letter word
# Input: ABC
# Output: ABC, ACB, BAC, BCA, CAB, CBA
# ============================================================

text = "ABC"

a = text[0]
b = text[1]
c = text[2]

print("\n8. Permutations:")

print(a + b + c)
print(a + c + b)

print(b + a + c)
print(b + c + a)

print(c + a + b)
print(c + b + a)


# ============================================================
# 9. Convert Integer to Roman Numeral
# Input: 9
# Output: IX
# ============================================================

number = 9

values = [
    1000, 900, 500, 400,
    100, 90, 50, 40,
    10, 9, 5, 4, 1
]

romans = [
    "M", "CM", "D", "CD",
    "C", "XC", "L", "XL",
    "X", "IX", "V", "IV", "I"
]

result = ""

temp_number = number

for i in range(len(values)):

    while temp_number >= values[i]:

        result += romans[i]

        temp_number -= values[i]

print("\n9. Integer to Roman:")
print(number, "=", result)


# ============================================================
# 10. Convert Roman Numeral to Integer
# Input: IX
# Output: 9
# ============================================================

roman = "IX"

values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

result = 0

for i in range(len(roman)):

    # If current Roman value is smaller than next value,
    # subtract it.
    #
    # Example:
    # IX
    # I < X
    # -1 + 10 = 9

    if (
        i + 1 < len(roman)
        and values[roman[i]] < values[roman[i + 1]]
    ):
        result -= values[roman[i]]

    else:
        result += values[roman[i]]

print("\n10. Roman to Integer:")
print(roman, "=", result)