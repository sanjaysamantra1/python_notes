# ============================================================
# DATA
# ============================================================

products = [
    {"pId": 201, "name": "laptop", "price": 55000, "category": "electronics", "inStock": True},
    {"pId": 203, "name": "shirt", "price": 1200, "category": "clothing", "inStock": False},
    {"pId": 202, "name": "phone", "price": 30000, "category": "electronics", "inStock": True},
    {"pId": 205, "name": "shoes", "price": 3500, "category": "clothing", "inStock": True},
    {"pId": 204, "name": "tablet", "price": 25000, "category": "electronics", "inStock": False}
]

medicines = [
    {"mId": 301, "name": "paracetamol", "price": 50, "company": "cipla", "expiryYear": 2025},
    {"mId": 303, "name": "ibuprofen", "price": 80, "company": "sun", "expiryYear": 2024},
    {"mId": 302, "name": "amoxicillin", "price": 120, "company": "cipla", "expiryYear": 2026},
    {"mId": 305, "name": "cetirizine", "price": 60, "company": "abbott", "expiryYear": 2026},
    {"mId": 304, "name": "azithromycin", "price": 150, "company": "sun", "expiryYear": 2025}
]

students = [
    {"sId": 401, "name": "ravi", "marks": 72, "grade": "B", "city": "delhi"},
    {"sId": 403, "name": "priya", "marks": 91, "grade": "A", "city": "mumbai"},
    {"sId": 402, "name": "arjun", "marks": 55, "grade": "C", "city": "delhi"},
    {"sId": 405, "name": "sneha", "marks": 88, "grade": "A", "city": "pune"},
    {"sId": 404, "name": "rohit", "marks": 40, "grade": "D", "city": "mumbai"}
]


# ============================================================
# Q1.
# Filter products where inStock is False
# and apply 20% price hike
# ============================================================

out_of_stock_products = [
    {
        **product,
        "price": product["price"] * 1.20
    }
    for product in products
    if not product["inStock"]
]

print("\nQ1. Out of stock products after 20% hike:")

for product in out_of_stock_products:
    print(product)


# ============================================================
# Q2.
# Filter medicines not yet expired (expiryYear > 2024)
# and sort by price ascending
# ============================================================

valid_medicines = [
    medicine
    for medicine in medicines
    if medicine["expiryYear"] > 2024
]

valid_medicines = sorted(
    valid_medicines,
    key=lambda medicine: medicine["price"]
)

print("\nQ2. Non-expired medicines sorted by price:")

for medicine in valid_medicines:
    print(medicine)


# ============================================================
# Q3.
# Add discountedPrice to every product
# 10% discount
# ============================================================

discounted_products = [
    {
        **product,
        "discountedPrice": product["price"] * 0.90
    }
    for product in products
]

print("\nQ3. Products with discounted price:")

for product in discounted_products:
    print(product)


# ============================================================
# Q4.
# Group products by category
# ============================================================

products_by_category = {}

for product in products:

    category = product["category"]

    if category not in products_by_category:
        products_by_category[category] = []

    products_by_category[category].append(product)


print("\nQ4. Products grouped by category:")
print(products_by_category)


# ============================================================
# Q5.
# Find total price of medicines by company "cipla"
# ============================================================

cipla_total = sum(
    medicine["price"]
    for medicine in medicines
    if medicine["company"] == "cipla"
)

print("\nQ5. Total price of Cipla medicines:")
print(cipla_total)

# 50 + 120 = 170


# ============================================================
# Q6.
# Merge products with stockInfo using pId
# ============================================================

stock_info = [
    {"pId": 201, "qty": 10},
    {"pId": 202, "qty": 0},
    {"pId": 203, "qty": 5},
    {"pId": 204, "qty": 3},
    {"pId": 205, "qty": 8}
]


# Create lookup dictionary
stock_lookup = {
    stock["pId"]: stock["qty"]
    for stock in stock_info
}


merged_products = [
    {
        **product,
        "qty": stock_lookup.get(product["pId"], 0)
    }
    for product in products
]


print("\nQ6. Products with stock quantity:")

for product in merged_products:
    print(product)


# ============================================================
# Q7.
# Count occurrence of each grade
# ============================================================

grade_count = {}

for student in students:

    grade = student["grade"]

    grade_count[grade] = grade_count.get(grade, 0) + 1


print("\nQ7. Grade occurrence:")
print(grade_count)

# Output:
# {'B': 1, 'A': 2, 'C': 1, 'D': 1}


# ============================================================
# Q8.
# Group students by city and find average marks per city
# ============================================================

city_marks = {}

for student in students:

    city = student["city"]

    if city not in city_marks:
        city_marks[city] = []

    city_marks[city].append(student["marks"])


city_average = {}

for city, marks in city_marks.items():
    city_average[city] = sum(marks) / len(marks)


print("\nQ8. Average marks by city:")
print(city_average)

# Output:
# {
#     'delhi': 63.5,
#     'mumbai': 65.5,
#     'pune': 88.0
# }


# ============================================================
# Q9.
# Find medicine with highest price
# WITHOUT sort()
# ============================================================

highest_price_medicine = max(
    medicines,
    key=lambda medicine: medicine["price"]
)

print("\nQ9. Medicine with highest price:")
print(highest_price_medicine)

# azithromycin - 150


# ============================================================
# Q10.
# Find product names where:
# inStock = True AND price > 20000
# ============================================================

product_names = [
    product["name"]
    for product in products
    if product["inStock"] and product["price"] > 20000
]


print("\nQ10. In-stock products above 20000:")
print(product_names)

# Output:
# ['laptop', 'phone']