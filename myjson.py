import json

string = '{"name": "nazish", "age": 25}'
data = json.loads(string)
print(data)
print(data["name"])

jsonstr = json.dumps(data)
print(jsonstr)