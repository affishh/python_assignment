# This script filters a list of dictionaries to find people older than 25
data = [{'name': 'Alice', 'age': 25, 'city': 'New York'},
        {'name': 'Bob', 'age': 30, 'city': 'Los Angeles'},
        {'name': 'Charlie', 'age': 22, 'city': 'Chicago'}, 
        {'name': 'David', 'age': 28, 'city': 'Houston'}]

filtered_data = [age for age in data if age['age'] > 25]
print("People older than 25:")
for person in filtered_data:
    print(f"{person['name']}, {person['age']}, {person['city']}")