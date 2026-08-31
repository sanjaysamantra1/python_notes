import json

user = {"id": 101,"name": "John"}
json_data = json.dumps(user)
print(json_data)
print(type(json_data))


json_data = '{"id": 101, "name": "John"}'
user = json.loads(json_data)
print(user)
print(type(user))