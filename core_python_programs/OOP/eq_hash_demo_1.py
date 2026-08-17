class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def __eq__(self, other):
        return isinstance(other, User) and self.user_id == other.user_id

    def __hash__(self):
        return hash(self.user_id)

u1 = User(1, "Sanjay")
u2 = User(1, "Sanjay K")  # same id, different name
print(u1 == u2)  # True - equality is based on user_id, not object identity

users = {u1, u2}  # __hash__ lets it dedupe in a set
print(len(users))  # 1