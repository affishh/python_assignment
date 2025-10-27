#1. Write Python scripts for basic file operations and data processing? 
#` This script creates a text file and writes some data into it.
with open ('file.txt', 'w') as file:
    file.write("Name,Age,City\n")
    file.write("Alice,25,New York\n")
    file.write("Bob,30,Los Angeles\n")
    file.write("Charlie,22,Chicago\n")

print("File 'file.txt' created and data written successfully.")

# To verify, you can read the file and print its contents
with open('file.txt', 'r') as file:
    content = file.read()
    print("File contents:")
    print(content)

# append data to the file
with open('file.txt', 'a') as file:
    file.write("David,28,Houston\n")
    print("Data appended successfully.")
    # To verify, you can read the file and print its contents again
with open('file.txt', 'r') as file:
    content = file.read()
    print("Updated file contents:")
    print(content)

#Read File Line by Line and Process Data

with open('file.txt', 'r') as file:
    lines = file.readlines()

header = lines[0].strip().split(",")
records = [line.strip().split(",") for line in lines[1:]]

print("people older than 24:")
for record in records:
    name, age, city = record
    if int(age) > 24:
        print(f"{name}, {age}, {city}")

