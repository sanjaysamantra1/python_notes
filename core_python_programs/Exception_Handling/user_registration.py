class InvalidAgeError(Exception):
    pass


def register_user(name, age):
    if not name:
        raise ValueError("Name cannot be empty")

    if age < 18:
        raise InvalidAgeError(
            "User must be 18 years or older"
        )

    return {
        "message": "User registered successfully",
        "name": name,
        "age": age
    }


try:
    user = register_user("Sanjay", 25)
    print(user)

except ValueError as e:
    print("Validation error:", e)

except InvalidAgeError as e:
    print("Age error:", e)

except Exception as e:
    print("Unexpected error:", e)

finally:
    print("Registration process finished")