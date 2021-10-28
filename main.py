# import json
#
# studentsList = []
# print("Started Reading JSON file which contains multiple JSON document")
# with open('data/example.json') as f:
#     for jsonObj in f:
#         studentDict = json.loads(jsonObj)
#         studentsList.append(studentDict)
#
# print(studentsList)
# import json

# with open('data/example.json') as json_file:
#     data = json.load(json_file)
#     print(data)

# import commentjson

# with open('data/example.json', 'r') as handle:
#     employee_data = commentjson.load(handle)

# print(employee_data)
# import json

# with open('data/example.json', 'r', encoding="utf8") as data_file:
#     json_data = data_file.read()

# data = json.loads(json_data)
import json
with open('data/example.json', encoding='utf-8') as fh:
    data = json.load(fh)

print(data)

# import json

# with open('data/example.json', 'r') as jsonfile:
#     jsondata = ''.join(line for line in jsonfile if not line.startswith('//'))
#     data = json.loads(jsondata)

# print(data)

# import json

# with open('data/example.json', 'r') as handle:
#     fixed_json = ''.join(line for line in handle if not line.startswith('/*'))
#     employee_data = json.loads(fixed_json)

# print(employee_data)
