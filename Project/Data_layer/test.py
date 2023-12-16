import json

# Data to be written
dictionary = {"name": "sathiyajith", "rollno": 56, "cgpa": 8.6, "phonenumber": "9976770500"}

# Serializing json
json_object = json.dumps(dictionary, indent=4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)

# # JSON string
# j_string = '{"name": "Bob", "languages": "English"}'

# # deserializes into dict and returns dict.
# y = json.loads(j_string)

# print("JSON string = ", y)
# print()

# f = open ('data.json', "r")

# data = json.loads(f.read())

# # Iterating through the json list
# for i in data:
#     print(i,':',data[i])

# # Closing file
# f.close()

# We can open the json file in 'read' mode,
# the way we do it with .txt and .csv files
# with open("example.json", "r", newline="") as file:
#     reader = json.load(file)
#     for row in reader:
#         print("row", row, reader[row])
with open("example.json", "r") as file:
    jsonData = json.load(file)

print("Type of JSON Object: ", type(jsonData))

# Traversing the json file
for name in jsonData:
    print("Name: ", name)
    print("Phone Number: ", jsonData[name]["number"])
    print("Age: ", jsonData[name]["age"])

    print("Address:")
    for line in jsonData[name]["address"]:
        print(line)
    print()
