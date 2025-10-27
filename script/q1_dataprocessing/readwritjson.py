import json
# Reading JSON file
with open('example.json', 'r') as file:
    read = json.load(file)
    print("Data read from JSON file:")
    print(read)
#write data to json file
data = {
    "name" : "john",
    "age" : 24,
    "city" : "new york"

}

with open('example.json', 'w') as file:
    content = json.dump(data, file, indent=4)
print("Data written to JSON file successfully.")
with open('example.json', 'r') as file:
    read = json.load(file)
    print("Updated data read from JSON file:")
    print(read)